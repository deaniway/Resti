function toggle_filters_display() {
    var widget = $("#filters")[0];
    if (widget.style.display != 'none') {
        widget.style.display = 'none';
    } else {
        widget.style.display = 'block';
    }
}
