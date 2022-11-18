(function ($) {
  // Header mobile menu
  $(".mobile-menu-btn").click(function () {
    $("body").addClass("mobile-menu-opened");
    $(".mobile-menu").addClass("opened");
  });

  // Left sidebar menu
  $(".left-sidebar-menu-btn").click(function () {
    $("body").addClass("mobile-left-sidebar-menu-opened");
    $(".left-sidebar-menu").addClass("opened");
  });

  // Right sidebar menu
  $(".right-sidebar-menu-btn").click(function () {
    $("body").addClass("right-sidebar-menu-opened");
    $(".right-sidebar-menu").addClass("opened");
  });

  // $('.mobile-menu, .mobile-menu-btn, .left-sidebar-menu, .left-sidebar-menu-btn, .right-sidebar-menu, .right-sidebar-menu-btn').click(function(e) {
  //     e.stopPropagation();
  // });
  $(".mobile-menu-btn, .left-sidebar-menu-btn, .right-sidebar-menu-btn").click(
    function (e) {
      e.stopPropagation();
    }
  );

  $(document).click(function () {
    // Header menu
    $(".mobile-menu").removeClass("opened");
    $("body").removeClass("mobile-menu-opened");

    // Left sidebar menu
    $(".left-sidebar-menu").removeClass("opened");
    $("body").removeClass("mobile-left-sidebar-menu-opened");

    // Right sidebar menu
    $(".right-sidebar-menu").removeClass("opened");
    $("body").removeClass("right-sidebar-menu-opened");
  });

  // Boostrap dropdown hold on click
  $(document).on("click", ".dropdown-menu.hold-on-click", function (e) {
    e.stopPropagation();
  });

  // Chat mobile
  $(".chat__contacts-btn").click(function () {
    $(this).toggleClass("active");
    $(".chat__contacts").toggleClass("active");
  });

  // Accordion
  $(".accordion__btn").click(function () {
    $(this).toggleClass("rotate");
    $(this).parents(".accordion").toggleClass("closed");
    $(this).parents(".accordion").find(".accordion__body").slideToggle("fast");
  });

  // Teachers slider
  $("#slider_teachers").owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    navContainer: "#slider_teachers_nav",
    dots: false,
    responsive: {
      0: {
        items: 1,
      },
      800: {
        items: 2,
      },
      1000: {
        items: 3,
      },
      1200: {
        items: 4,
      },
    },
  });

  // Circle Progress bar percent
  $(".progress-circle .progress").each(function () {
    var progressCirclePercent = $(this).data("percent");
    $(this).css("stroke-dashoffset", 1.95 * (100 - progressCirclePercent));
  });

  $(".progress-circle-big .progress").each(function () {
    var progressCirclePercent = $(this).data("percent");
    $(this).css("stroke-dashoffset", 3.78 * (100 - progressCirclePercent));
  });

  // Scrolling to center the Current item of the Test Pagination
  var testPaginationCurrentItemPosition = $(
    ".test__pagination ul li.current"
  ).position();
  var testPaginationWidth = $(".test__pagination").outerWidth();
  $(".test__pagination")
    .stop()
    .animate(
      {
        scrollLeft:
          testPaginationCurrentItemPosition.left -
          (testPaginationWidth / 2 - 36),
      },
      0
    );

  // Sortable - Sort the parents

  // Chat body scroll to bottom
  // $(window).load(function() {
  //     var chatBodyHeight = $('.chat__body').height();
  //     $('.chat__body').scrollDown(chatBodyHeight);
  // });
})(jQuery);
