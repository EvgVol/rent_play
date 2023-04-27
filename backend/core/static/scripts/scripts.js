$(document).ready(function () {
    // отслеживаем событие отправки формы
    $('#id_username').keyup(function () {
        // создаем AJAX-вызов
        $.ajax({
            data: $(this).serialize(), // получаяем данные формы
            url: "validate_username",
            // если успешно, то
            success: function (response) {
                if (response.is_taken == true) {
                    $('#id_username').removeClass('is-valid').addClass('is-invalid');
                    $('#id_username').after('<div class="invalid-feedback d-block" id="usernameError">К сожалению это имя уже занято!</div>')
                }
                else {
                    $('#id_username').removeClass('is-invalid').addClass('is-valid');
                    $('#usernameError').remove();

                }
            },
            // если ошибка, то
            error: function (response) {
                // предупредим об ошибке
                console.log(response.responseJSON.errors)
            }
        });
        return false;
    });
})