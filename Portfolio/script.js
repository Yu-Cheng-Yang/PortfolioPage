document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll("a");

    links.forEach(function(link) {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            const targetSection = document.querySelector(this.getAttribute("href"));
            scrollToSection(targetSection);
        });
    });

    function scrollToSection(targetSection) {
        window.scrollTo({
            top: targetSection.offsetTop,
            behavior: "smooth"
        });
    }
});
