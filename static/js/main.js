document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function () {
            alert('Formulario enviado. ¡Gracias por contactarnos!');
        });
    }
});
