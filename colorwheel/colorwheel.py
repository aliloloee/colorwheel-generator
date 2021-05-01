import cv2 as cv
import numpy as np
import math
from pathlib import Path

class ColorWheel() :
    """
    Colorwheel is a package for generating colorwheels with different numbers of colors.
    
    How to use this package :

    When instantiating the class, there is a parameter 'side', which is responsible for the height of the picture. The default value for side is 768 and the width of the picture is proportioned so that the picture fills the screen of a 15.6 inch laptop. For other screen sizes you can instantiate the class with another value for 'side' and also another value for the parameter 'screen_portion'. 'screen_portion' default value is 1.778 which is portion of width to height of a 15.6 inch laptop. For other screen sizes you should calculate the value for 'screen_portion' yourself.

    After instantiating the Colorwheel class, just execute 'show()' method on the object to see the colorwheel. By default the colorwheel will have 12 colors but you can change the number by giving value to parameter 'color_number' when instantiating the class. Note that only numbers in the formats below are acceptable :
    3*2, 3*4, 3*8, 3*16, 3*32, ... and 12, 12*2, 12*3, 12*4, ... .

    Also if you want to save a picture of the colorwheel, just press 's' on your keyboard while the picture window is open.

    There are some other features that come with the final picture. Like lines between colors, a small white circle in the center of colorwheel, the direction of the colors and rotation angel for the colors in the colorwheel.

    For each feature there is a parameter responsible for changing or canceling that feature :

    Lines between colors : By default you should have lines between colors, but if you set parameter 'lines' to False when instantiating the class then this feature will be cancelled.

    White circle in the center of colorwheel : If you dont like it just instantiate the class with parameter 'center_circle' with value of False.

    Direction of the colors : If you want to change the direction of the colors in the colorwheel just instantiate the class with parameter 'reversing' with value of True.

    Rotation angel for the colors : By default 'rotation' parameter is 0, but if you want the colors to rotate ,then instantiate the class with parameter 'rotation' set to a degree [0, 360].
    """
    def __init__(self, side=768, *args, **kwargs) :
        self.reversing = kwargs.get('reversing', False)
        self.rotation = kwargs.get('rotation', 0)
        self.lines = kwargs.get('lines', True)
        self.center_circle = kwargs.get('center_circle', True)
        self.arcNumber = kwargs.get('color_number', 12)
        self.screenPortion = kwargs.get('screen_portion', 1.778)

        self.arcDegree = 360/self.arcNumber     
        self.side = side
        self.width = int(round(self.screenPortion * self.side))
        self.colors = self.__buildColors()
        self.picture = self.__buildWheel()
        self.__baseAddress = Path(__file__).resolve().parent

    def __buildColors(self) :
        teta = 360/self.arcNumber
        alpha = int(120/teta)
        beta = int(60/teta)
        red = []
        for i in range(alpha+1) :
            red.append(0)
        for i in range(beta-1) :
            red.append( (i+1) * (255/beta) )
        for i in range(alpha+1) :
            red.append(255)
        for i in range(beta-1, 0, -1) :
            red.append( i * (255/beta) )
        red = np.array(red)
        green = np.roll(red, alpha)
        blue = np.roll(green, alpha)
        colors = []
        for i in range(self.arcNumber) :
            a = (int(round(red[i])), int(round(green[i])), int(round(blue[i])))
            colors.append(a)
        if self.reversing :
            colors.reverse()
        return colors

    def __buildWheel(self) :
        image = np.ones((self.side, self.width, 3), np.uint8)*255
        image = self.__putBorderCircles(image)
        image = self.__putArcs(image)
        if self.rotation == 0 and self.lines:
            image = self.__putArcBorders(image)
        if self.center_circle :
            image = self.__putCentringCircle(image)
        return image

    def __putBorderCircles(self, image) :
            cv.circle(image, (int(self.width/2), int(self.side/2)), int(self.side/3) + int(self.side/50), (240, 247, 247), -1)
            cv.circle(image, (int(self.width/2), int(self.side/2)), int(self.side/3) + int(self.side/100) , (255, 255, 255), -1)
            return image

    def __putArcs(self, image) :
        for i in range(self.arcNumber) :
            cv.ellipse(image,
                        (int(self.width/2), int(self.side/2)),
                        (int(self.side/3), int(self.side/3)),
                        self.rotation,
                        self.arcDegree*i, self.arcDegree*(i+1), self.colors[i], -1)
        return image

    def __putArcBorders(self, image) :
        for i in range(self.arcNumber) :
            x = int(self.width/2 + (self.side/3)*math.cos(math.radians((i)*self.arcDegree)))
            y = int(self.side/2 + (self.side/3)*math.sin(math.radians((i)*self.arcDegree)))
            cv.line(image, (int(self.width/2), int(self.side/2)), (x,y), (255, 255, 255), 1)
        return image

    def __putCentringCircle(self, image) :
        cv.circle(image, (int(self.width/2), int(self.side/2)), int(self.side/30), (255, 250, 250), -1)
        return image

    def show(self) :
        cv.imshow('ColorWheel', self.picture)
        while (1) :
            k = cv.waitKey()
            if k in (-1, 27) :
                break
            elif k == ord('s') :
                path = str(self.__baseAddress / f'colorWheel{self.side}-{self.arcNumber}.png')
                cv.imwrite(path, self.picture)
                break
        cv.destroyAllWindows()
