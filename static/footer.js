$(function () {
    function footerPosition() {
        $("footer").removeClass("fixed-bottom");
        var contentHeight = document.body.scrollHeight, winHeight = window.innerHeight;
        if (!(contentHeight > winHeight))
            $("footer").addClass("fixed-bottom");
    }

    footerPosition();
    $(window).resize(footerPosition);
});