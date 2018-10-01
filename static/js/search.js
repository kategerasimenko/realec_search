function enumerate_fields (input_form, n, first_load=false) {
    $(input_form).find('input').each(function () {
        var name = $(this).attr('name');
        if (first_load) {
            var new_name = name + '_' + n;
        } else {
            var new_name = name.split('_').slice(0, -1).join('_') + '_' + n;
        };
        $(this).attr('name', new_name)
    });
    $(input_form).addClass('last_word')
    $(input_form).attr('num', n)
}

function add_word () {
    var last = $('.last_word');
    if ($(last).is(":hidden")) {
        $(last).show()
    } else {
        var n = parseInt($(last).attr('num'), 10) + 1;
        var new_word = $(last).clone();
        enumerate_fields(new_word, n, false);
        $(new_word).insertAfter(last);
        $(last).removeClass('last_word')
    }
}
    
window.onload = function () {
    enumerate_fields($('.firstword'), 0, true);
    enumerate_fields($('.nextword'), 1, true)
}