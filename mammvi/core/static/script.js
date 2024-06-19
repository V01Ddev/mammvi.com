
$(document).ready(function() {
    $(".images-to-click img").click(function(){
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
