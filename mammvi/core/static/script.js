
console.log("Loading page...")

$(document).ready(function() {
    console.log("Page loaded")
    $(".images-to-click img").click(function(){
        console.log("Image clicked")
        $(".full-image").attr("src", $(this).attr("src"));
        $('.image-viewer').show();

    });

    $(".image-viewer").on( "click", function() {
        $('.image-viewer').hide();
    });

    $(".full-image").on( "click", function(reg) {
        reg.stopPropagation();
    });
});
