// script.js

$(document).ready(function() {
    $('#add_item').click(function() {
        // Add a new <li> element to UL.my_list
        $('<li>Item</li>').appendTo('.my_list');
    });

    $('#remove_item').click(function() {
        // Remove the last <li> element from UL.my_list
        $('.my_list li:last-child').remove();
    });

    $('#clear_list').click(function() {
        // Clear all elements from UL.my_list
        $('.my_list').empty();
    });
});
