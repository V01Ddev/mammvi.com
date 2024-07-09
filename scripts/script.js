
$(document).ready(function() {
    // on image click, shows the full sized image full screen
    $(".images-to-click img").click(function(){
        var path = $(this).attr("src").replace('thm/', '')
        console.log(path);
        $(".full-image").attr("src", path);
        $('.image-viewer').show();
        $('.image-viewer').css('display', 'flex');
    });

    // to hide the image if anywhere else other than the imaged is clicked 
    $(".image-viewer").on( "click", function() {
        $('.image-viewer').hide();
        $('.image-viewer').css('display', 'none');
        $(".full-image").attr("src", '');
    });

    $(".full-image").on( "click", function(reg) {
        reg.stopPropagation();
    });
});
