function toggle_filters_display() {
    var widget = document.getElementById("filters");
    if (widget.style.display != 'none') {
        widget.style.display = 'none';
    } else {
        widget.style.display = 'block';
    }
}
function refresh_workers(_business_id=0, _sorting=0, button_id=0) {
    if (_business_id != 0) { business_id = _business_id; }
    if (_sorting != 0) { sorting = _sorting; }

    $.ajax({
        type: 'GET',
        url: worker_list_data_url,
        cache: false,
        data: {
            'business_id': business_id,
            'ordering': sorting
        },
        success: function (response) {
            $('#workers-list').html( response );
        },
        error: function (response) {
            $('#workers-list').html( '<div class="alert">Не удалось получить информацию</div>' );
        }
    });
}
$(document).ready( refresh_workers() );
$("a.rb").click( function(event) {
    alert(event);
})
