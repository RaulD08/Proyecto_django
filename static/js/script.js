
$(document).ready(function() {
   
    $(window).scroll(function () {
        if ($(this).scrollTop() > 20) {
            $('#scrollTopBtn').fadeIn();
        } else {
            $('#scrollTopBtn').fadeOut();
        }
    });

    $('#scrollTopBtn').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 600);
        return false;
    });

});
