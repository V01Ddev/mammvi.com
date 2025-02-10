<!DOCTYPE html>

<html>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" /> 


    <!-- landing page -->
    <head>
        <section class="landing">
            <link rel="stylesheet" type="text/css" href="styles/style.css">

            <!-- Loading Jquery -->
            <script src='scripts/jquery-3.7.1.js'></script>
            <script src='scripts/script.js'></script>

            <h1>I am MAMMVI</h1>
            <h2>welcome to my photography journal</h2>
            <h4>Please rotate your phone for the best viewing experience</h4>


            <img src='images/down.svg' class='down-sym'>
        </section>
    </head>

    <!--
<section class="{DATE}">
<h3>{TITLE}</h3>
<h5>{DAY}th {MONTH} {YEAR}</h5>
<p></p>
<div class="images-to-click">
<ul>
<?php
render_images("{DATE}", "{alttext}")
?>
</ul>
</section>
-->

    <body>
<?php
function render_images($dirname, $alttext = "")
{
    $path = 'images/' . $dirname . '/thm/*';
    $files = glob($path);
    foreach ($files as $file) {
        echo "<li><div class='image-div'><img src='{$file}' class='the-images' loading='lazy' alt='{$alttext}'></div></li>";
    }
}
?>

        <section class="24_06_27">
            <h3>Spain</h3>
            <h5>27th June 2024</h5>
            <p>Pictures of the Alhambra palace in Granada</p>
            <div class="images-to-click">
                <ul>
<?php
    render_images("24_06_27", "The Alhambra palace in Granada")
?>
                </ul>
            </div>
        </section>

        <section class="24_06_24">
            <h5>24th June 2024</h5>
            <p>Images taken in Córdoba of the Mosque-Cathedral</p>
            <div class="images-to-click">
                <ul>
<?php
    render_images("24_06_24", "Córdoba of the Mosque-Cathedral")
?>
            </div>
        </section>

        <section class="23_01_27">
            <h5>20th June 2024</h5>
            <div class="images-to-click">
                <ul>
<?php
    render_images("24_06_20", "Turkish Arilines Plane")
?>
            </div>
        </section>

        <section class='23_06_29'>
            <h3>Turkey 2023</h3>
            <h5>29th June 2023</h5>
            <p>
                Random street photography in Istanbul
            </p>
            <div class="images-to-click">
                <ul>
<?php
    render_images("23_06_29", "Street photography in Istanbul")
?>
                </ul>
            </div>
        </section>

        <section class="23_01_27">
            <h3>Qatar Racing Club</h3>
            <h5>27th January 2023</h5>
            <p>
                Photos from Qatar Racing Club
            </p>
            <div class="images-to-click">
                <ul>
                    <li>
<?php
    render_images("23_01_27", "Cars drifting at Qatar Racing Club")
?>
                </ul>
            </div>
        </section>

        <!-- Image full screen view -->
        <div class="image-viewer">
            <img class="full-image">
            <u><a class="image_link" target="_blank">full image</a></u>
        </div>
    </body>
</html>
