<p><strong>Colorwheel</strong> is a package for generating colorwheels with different numbers of colors.</p>

<h1>How to install this package : </h1>

<p><code>pip install colorwheel</code></p>
<em>Don't forget to <code>pip install pathlib</code> if you don't have it installed</em>

<h1>How to use this package : </h1>

<p>When instantiating the class, there is a parameter <code>side</code>, which is responsible for the height of the picture. The default value for side is 768 and the width of the picture is proportioned so that the picture fills the screen of a 15.6 inch laptop. For other screen sizes you can instantiate the class with another value for <code>side</code> and also another value for the parameter <code>screen_portion</code>. <code>screen_portion</code> default value is 1.778 which is portion of width to height of a 15.6 inch laptop. For other screen sizes you should calculate the value for <code>screen_portion</code> yourself.</p>

<p>After instantiating the Colorwheel class, just execute <strong>show()</strong> method on the object to see the colorwheel. By default the colorwheel will have 12 colors but you can change the number by giving value to parameter <code>color_number</code> when instantiating the class. Note that only numbers in the formats below are acceptable :
3*2, 3*4, 3*8, 3*16, 3*32, ... and 12, 12*2, 12*3, 12*4, ...</p>

<p>Also if you want to save a picture of the colorwheel, just press <strong>'s'</strong> on your keyboard while the picture window is open.</p>

<p>There are some other features that come with the final picture. <em>Like lines between colors</em>, <em>a small white circle in the center of colorwheel</em>, <em>the direction of the colors</em> and <em>rotation angel for the colors in the colorwheel</em>.
<p> 

<p>For each feature there is a parameter responsible for changing or canceling that feature :</p>

<ol>
<li>Lines between colors : By default you should have lines between colors, but if you set parameter <code>lines</code> to False when instantiating the class then this feature will be cancelled.</li>

<li>White circle in the center of colorwheel : If you dont like it just instantiate the class with parameter <code>center_circle</code> with value of False.</li>

<li>Direction of the colors : If you want to change the direction of the colors in the colorwheel just instantiate the class with parameter <code>reversing</code> with value of True.</li>

<li>Rotation angel for the colors : By default <code>rotation</code> parameter is 0, but if you want the colors to rotate ,then instantiate the class with parameter <code>rotation</code> set to a degree [0, 360].</li>
</ol>

<h2>Example</h2>
<p>from colorwheel import ColorWheel</p>
<p>cw = ColorWheel()</p>
<p>cw.show()</p>
<img src="#" alt="12 colored colorwheel"></img>

<h3>Github address</h3>
<a href="https://github.com/aliloloee">github.com/aliloloee</a>


