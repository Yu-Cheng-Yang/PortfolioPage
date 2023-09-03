from flask import Flask, render_template, request,jsonify, send_from_directory
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('portfolio.html')  

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
     
        # Save the message to a file
        with open(os.path.join("data", "messages.txt"), "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Message: {message}\n")
            file.write("="*40 + "\n") 
        

        return jsonify({'message': 'Thanks for your message!'}), 200
    else:
        return jsonify({'message': 'Form submission failed.'}), 400
from flask import send_from_directory

@app.route('/docs/<filename>')
def send_file(filename):
    return send_from_directory('documents', filename)

if __name__ == '__main__':
    app.run(debug=True)
