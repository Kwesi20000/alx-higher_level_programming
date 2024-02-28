// script.js

$(document).ready(function() {
    $('#btn_translate').click(function() {
        var languageCode = $('#language_code').val();

        // Fetch translation from API
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            data: { lang: languageCode },
            success: function(response) {
                // Display translation in DIV#hello
                $('#hello').text(response.hello);
            },
            error: function() {
                $('#hello').text('Translation not found');
            }
        });
    });
});
