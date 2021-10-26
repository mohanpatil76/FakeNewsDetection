

(function ($) {
    $('.hamburger, .close-mob,#closeit').click(function () {
        $('.mobile-nav').toggleClass('open');
        $('body').toggleClass('overflow-hidden');
    });
    sticky_header();
    window.onscroll = function () {
        sticky_header();
    };

    function sticky_header() {
        var header = $('.header-nav-wrap');
        offset = window.innerWidth > 992 ? 35 : 0;
        if (window.pageYOffset > offset) {
            header.addClass('sticky');
        } else {
            header.removeClass('sticky');
        }
    }
})(jQuery);