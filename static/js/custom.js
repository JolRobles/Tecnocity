jQuery(document).ready(function ($) {


    "use strict";



    $(function () {
        $("#tabs").tabs();
    });


    // Page loading animation

    $("#preloader").animate({
        'opacity': '0'
    }, 600, function () {
        setTimeout(function () {
            $("#preloader").css("visibility", "hidden").fadeOut();
        }, 300);
    });


    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        var box = $('.header-text').height();
        var header = $('header').height();

        if (scroll >= box - header) {
            $("header").addClass("background-header");
        } else {
            $("header").removeClass("background-header");
        }
    });
    if ($('.owl-clients').length) {
        $('.owl-clients').owlCarousel({
            loop: true,
            nav: false,
            dots: true,
            items: 1,
            margin: 30,
            autoplay: true,
            smartSpeed: 700,
            autoplayTimeout: 6000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 3,
                    margin: 20
                },
                992: {
                    items: 5,
                    margin: 30
                }
            }
        });
    }
    if ($('.owl-testimonials').length) {
        $('.owl-testimonials').owlCarousel({
            loop: true,
            nav: false,
            dots: true,
            items: 1,
            margin: 30,
            autoplay: true,
            smartSpeed: 700,
            autoplayTimeout: 6000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 2,
                    margin: 20
                },
                992: {
                    items: 2,
                    margin: 30
                }
            }
        });
    }
    if ($('.owl-banner').length) {
        $('.owl-banner').owlCarousel({
            loop: true,
            nav: false,
            dots: true,
            items: 1,
            margin: 0,
            autoplay: true,
            smartSpeed: 700,
            autoplayTimeout: 6000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 1,
                    margin: 20
                },
                992: {
                    items: 1,
                    margin: 30
                }
            }
        });
    }

    $(".Modern-Slider").slick({
        autoplay: true,
        autoplaySpeed: 10000,
        speed: 600,
        slidesToShow: 1,
        slidesToScroll: 1,
        pauseOnHover: false,
        dots: true,
        pauseOnDotsHover: true,
        cssEase: 'linear',
        // fade:true,
        draggable: false,
        prevArrow: '<button class="PrevArrow"></button>',
        nextArrow: '<button class="NextArrow"></button>',
    });

    // $('.filters ul li').click(function () {
    //     $('.filters ul li').removeClass('active');
    //     $(this).addClass('active');
    //     console.log("si se quito");

    //     var data = $(this).attr('data-filter');
    //     console.log(data);
    //     $grid.isotope({
    //         filter: data
    //     });
    //     setPagination();
    // });
    // var itemSelector = '.product-item'; 

    // var $grid = $(".grid").isotope({
    //     itemSelector: itemSelector,
    //     percentPosition: true,
    //     // masonry: {
    //     //     columnWidth: ".all"
    //     // }
    // });

    // //Ascending order
    // var responsiveIsotope = [
    //     [480, 4],
    //     [720, 6]
    // ];

    // var itemsPerPageDefault = 3;
    // console.log(itemsPerPageDefault);
    // var itemsPerPage = defineItemsPerPage();
    // var currentNumberPages = 1;
    // var currentPage = 1;
    // var currentFilter = '*';
    // var filterAtribute = 'data-filter';
    // var pageAtribute = 'data-page';
    // var pagerClass = 'isotope-pager';

    // function changeFilter(selector) {
    //     $grid.isotope({
    //         filter: selector
    //     });
    // }

    // function getFilterSelector() {
    //     var selector = itemSelector;
    //     if (currentFilter != '*') {
    //         selector += `[${filterAtribute}~="${currentFilter}"]`
    //     }
    //     return selector;
    // }

    // function goToPage(n) {
    //     currentPage = n;

    //     var selector = getFilterSelector();
    //     selector += `[${pageAtribute}="${currentPage}"]`;

    //     changeFilter(selector);
    // }

    // function defineItemsPerPage() {
    //     var pages = itemsPerPageDefault;

    //     for (var i = 0; i < responsiveIsotope.length; i++) {
    //         if ($(window).width() <= responsiveIsotope[i][0]) {
    //             pages = responsiveIsotope[i][1];
    //             break;
    //         }
    //     }
    //     return pages;
    // }

    // function setPagination() {
    //     var SettingsPagesOnItems = function () {
    //         // var itemsLength = $grid.children(itemSelector).length;
    //         var itemsLength = $('.product-item:not([style*="display: none"])').length;
    //         console.log("gaa " + itemsLength);
    //         var pages = Math.ceil(itemsLength / itemsPerPage);
    //         var item = 1;
    //         var page = 1;
    //         var selector = getFilterSelector();

    //         $grid.children(selector).each(function () {
    //             if (item > itemsPerPage) {
    //                 page++;
    //                 item = 1;
    //             }
    //             $(this).attr(pageAtribute, page);
    //             item++;
    //         });

    //         currentNumberPages = page;

    //     }();

    //     var CreatePagers = function () {

    //         var $isotopePager = ($('.' + pagerClass).length == 0) ? $('<div class="' + pagerClass + '"></div>') : $('.' + pagerClass);

    //         $isotopePager.html('');

    //         for (var i = 0; i < currentNumberPages; i++) {
    //             var $pager = $('<a href="javascript:void(0);" class="pager" ' + pageAtribute + '="' + (i + 1) + '"></a>');
    //             $pager.html(i + 1);

    //             $pager.click(function () {
    //                 var page = $(this).eq(0).attr(pageAtribute);
    //                 goToPage(page);
    //             });

    //             $pager.appendTo($isotopePager);
    //         }
    //         $grid.after($isotopePager);
    //     }();
    // }

    // setPagination();
    // goToPage(1);

    // //Adicionando Event de Click para as categorias
    // // $('.filters a').click(function () {
    // //     var filter = $(this).attr(filterAtribute);
    // //     currentFilter = filter;
    // //     setPagination();
    // //     goToPage(1);
    // // });

    // //Evento Responsivo
    // $(window).resize(function () {
    //     itemsPerPage = defineItemsPerPage();
    //     setPagination();
    //     goToPage(1);
    // });


    $(document).ready(function () {

        var itemSelector = '.grid-item';

        var $container = $('#container').isotope({
            itemSelector: itemSelector,
            masonry: {
                // columnWidth: itemSelector,
                // isFitWidth: true
            }
        });

        //Ascending order
        var responsiveIsotope = [
            [480, 4],
            [720, 6]
        ];

        var itemsPerPageDefault = 5;
        var itemsPerPage = defineItemsPerPage();
        var currentNumberPages = 1;
        var currentPage = 1;
        var currentFilter = '*';
        var filterAtribute = 'data-filter';
        var pageAtribute = 'data-page';
        var pagerClass = 'isotope-pager';

        function changeFilter(selector) {
            $container.isotope({
                filter: selector
            });
        }

        function getFilterSelector() {
            var selector = itemSelector;
            if (currentFilter != '*') {
                selector += `[${filterAtribute}~="${currentFilter}"]`
            }
            return selector;
        }

        function goToPage(n) {
            currentPage = n;

            var selector = getFilterSelector();
            selector += `[${pageAtribute}="${currentPage}"]`;

            changeFilter(selector);
        }

        function defineItemsPerPage() {
            var pages = itemsPerPageDefault;

            for (var i = 0; i < responsiveIsotope.length; i++) {
                if ($(window).width() <= responsiveIsotope[i][0]) {
                    pages = responsiveIsotope[i][1];
                    break;
                }



            }

            return pages;
        }

        function setPagination() {

            var SettingsPagesOnItems = function () {

                var itemsLength = $container.children(itemSelector).length;

                var pages = Math.ceil(itemsLength / itemsPerPage);
                var item = 1;
                var page = 1;
                var selector = getFilterSelector();

                $container.children(selector).each(function () {
                    if (item > itemsPerPage) {
                        page++;
                        item = 1;
                    }
                    $(this).attr(pageAtribute, page);
                    item++;
                });

                currentNumberPages = page;

            }();

            var CreatePagers = function () {

                var $isotopePager = ($('.' + pagerClass).length == 0) ? $('<div class="' + pagerClass + '"></div>') : $('.' + pagerClass);

                $isotopePager.html('');

                for (var i = 0; i < currentNumberPages; i++) {
                    var $pager = $('<a href="javascript:void(0);" class="pager" ' + pageAtribute + '="' + (i + 1) + '"></a>');
                    $pager.html(i + 1);

                    $pager.click(function () {
                        var page = $(this).eq(0).attr(pageAtribute);
                        goToPage(page);
                    });

                    $pager.appendTo($isotopePager);
                }

                $container.after($isotopePager);

            }();

        }

        setPagination();
        goToPage(1);

        //Adicionando Event de Click para as categorias
        $('.filters a').click(function () {
            var filter = $(this).attr(filterAtribute);
            currentFilter = filter;

            setPagination();
            goToPage(1);


        });

        //Evento Responsivo
        $(window).resize(function () {
            itemsPerPage = defineItemsPerPage();
            setPagination();
            goToPage(1);
        });
    });

    $('.accordion > li:eq(0) a').addClass('active').next().slideDown();

    $('.accordion a').click(function (j) {
        var dropDown = $(this).closest('li').find('.content');

        $(this).closest('.accordion').find('.content').not(dropDown).slideUp();

        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
        } else {
            $(this).closest('.accordion').find('a.active').removeClass('active');
            $(this).addClass('active');
        }

        dropDown.stop(false, true).slideToggle();

        j.preventDefault();
    });

});
