// script.js

$(document).ready(function() {
    // Function to fetch translation
    function fetchTranslation() {
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
    }

    // Listen for click event on #btn_translate
    $('#btn_translate').click(fetchTranslation);

    // Listen for keypress event on #language_code
    $('#language_code').keypress(function(event) {
        // Check if Enter key is pressed
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});
