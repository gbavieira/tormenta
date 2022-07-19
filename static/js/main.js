(function ($) {
    'use strict';
    function counter() {
        var oTop;
        if ($('.counter').length !== 0) {
          oTop = $('.counter').offset().top - window.innerHeight;
        }
        if ($(window).scrollTop() > oTop) {
          $('.counter').each(function () {
            var $this = $(this),
              countTo = $this.attr('data-count');
            $({
              countNum: $this.text()
            }).animate({
              countNum: countTo
            }, {
              duration: 1000,
              easing: 'swing',
              step: function () {
                $this.text(Math.floor(this.countNum));
              },
              complete: function () {
                $this.text(this.countNum);
              }
            });
          });
        }
      }
})(jQuery);