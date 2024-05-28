document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll("button, a");
    buttons.forEach(button => {
        button.addEventListener("mouseover", function() {
            this.style.transform = "scale(1.1)";
        });
        button.addEventListener("mouseout", function() {
            this.style.transform = "scale(1)";
        });
    });
});
