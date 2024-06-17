$(document).ready(function() {
    $(".the-images img").click(function(){
        console.log( "document loaded" );
        $("#full-image").attr("src", $(this).attr("src"));
        $('#image-viewer').show();
    });

    $("#image-viewer .close").click(function(){
        $('#image-viewer').hide();
    });
});
