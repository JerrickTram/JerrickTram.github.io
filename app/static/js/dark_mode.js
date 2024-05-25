document.addEventListener("DOMContentLoaded", function() {
    // Set dark mode by default
    document.body.classList.add('dark-mode');

    const toggleButton = document.getElementById('dark-mode-toggle');
    toggleButton.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
    });
});
