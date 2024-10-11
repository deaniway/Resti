var data_url = "";
var script_data = {};


function init_list_requests(_data_url, _script_data) {
    data_url = _data_url;
    script_data = _script_data;
}


function refresh_data(_script_data={}, button_id=0) {

    for (let [key, value] of Object.entries( _script_data )) {
        if (value != 0) {
            script_data[key] = value;
        }
    }

    $.ajax({
        type: 'GET',
        url: data_url,
        cache: false,
        data: script_data,
        success: function (response) {
            $('#data-list').html( response );
        },
        error: function (response) {
            $('#data-list').html( '<div class="alert">Не удалось получить информацию</div>' );
        }
    });
}


$(document).ready( function(){
    if ( $("#data-list").length ) {
        init_list_requests( LIST_DATA_URL, FILTERS );
        refresh_data();
    }
});
