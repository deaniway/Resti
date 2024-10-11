var is_modal_open = false;


function show_reqular_modal_form( url ) {
    $.ajax({
        type: 'GET',
        url: url,
        cache: false,
        success: function (response) {
            $('#modal-form-wrapper').html( response );

            $(document).ready( function(){
                $('#modal-form').each(function() {
                    this.showModal();
                });
                $('#modal-form-inner').each(function() {
                    this.setAttribute('action', url);
                });
                is_modal_open = true;
            });
        },
        error: function (response) {
            $('#modal-form-wrapper').html(
                '<dialog id="modal-form"><div class="alert">Не удалось получить информацию</div></dialog>'
            );
        }
    });
}


function show_list_action_modal_form( url_get ) {
    // modal form for update/delete action in list views
    $.ajax({
        type: 'GET',
        url: url_get,
        cache: false,
        success: function (response) {
            $('#modal-form-wrapper').html( response );

            $('#modal-form').each( function() {
                this.showModal();
                is_modal_open = true;
            });

            $("#modal-form-inner-update,#modal-form-inner-delete").submit( function(event) {
                event.preventDefault();
                var form = $(this);

                $.ajax({
                    type: "POST",
                    url: form.attr('action'),
                    data: form.serialize(),
                    success: function() {
                        close_modal_form();
                        refresh_data();
                    }
                });
            })
        },
        error: function (response) {
            $('#modal-form-wrapper').html(
                '<dialog id="modal-form"><div class="alert">Не удалось получить информацию</div></dialog>'
            );
        }
    });
}


$(window).on("click", function(event) {
    if ( (event.target == $('#modal-form')[0]) && is_modal_open) {
        close_modal_form();
    }
})


function close_modal_form() {
    $('#modal-form').each(function() {
        this.close();
        is_modal_open = false;
    });
}
