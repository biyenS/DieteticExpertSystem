function calculateBMI() {
    // Your existing calculateBMI() function code here
}

function backToHome() {
    // Your existing backToHome() function code here
}

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        calculateBMI();
    });
});
