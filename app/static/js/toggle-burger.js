$(document).ready(function () {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function () {

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        [".navbar-burger", ".navbar-menu"].forEach((el) => {
            $(el).toggleClass("is-active");
        });
    });
});