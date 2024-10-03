
$(document).ready(function() {
    // On image click, shows the full sized image full screen
    $(".images-to-click img").click(function(){
        // On click view thm, to save loading time
        // var path = $(this).attr("src").replace('thm/', '')
        var path = $(this).attr("src")
        console.log(path);
        $(".full-image").attr("src", path);
        $(".image_link").attr("href", path.replace('thm/', ''));
        $('.image-viewer').show();
        $('.image-viewer').css('display', 'flex');
    });

    // To hide the image if anywhere else other than the imaged is clicked 
    $(".image-viewer").on( "click", function() {
        $('.image-viewer').hide();
        $('.image-viewer').css('display', 'none');
        $(".full-image").attr("src", '');
    });

    $(".full-image").on( "click", function(reg) {
        reg.stopPropagation();
    });
});
