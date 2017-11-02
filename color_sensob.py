from sensob import Sensob
from sensors.camera import Camera


class ColorSensob(Sensob):
    """A sensob that detects the amount of a given color in an image."""

    def __init__(self, color, threshold=0.3, cut_ratio=(0.5, 0.25, 0, 0.25)):
        """
        Initialize the sensob.

        Arguments:
        color     -- A RGB tuple of the color to look for
        threshold -- The amount of leeway for the color
        cut_ratio -- The amount of the image to crop before analysing.
                     This is a tuple of ratios of the image, beginning
                     at the top and going clockwise. For example, passing
                     (0.1, 0.2, 0.3, 0.4) will cut 10% off the top, 20%
                     off the right side, 30% off the bottom and 40% of the left.
        """
        super().__init__()
        self.color = color
        self.threshold = threshold
        self.cut_ratio = cut_ratio
        self.camera = Camera()

    def update(self):
        """Take a picture with the camera, and analyse its color values."""
        image = self.camera.update()
        width, height = image.size

        start_y = height * self.cut_ratio[0]
        stop_y = height * (1-self.cut_ratio[2])
        start_x = width * self.cut_ratio[3]
        stop_x = width * (1-self.cut_ratio[1])

        lower = [self.color[i] - 255*self.threshold for i in range(3)]
        upper = [self.color[i] + 255*self.threshold for i in range(3)]

        num_color_pixels = 0
        num_pixels = (stop_x - start_x) * (stop_y - start_y)

        for x in range(start_x, stop_x):
            for y in range(start_y, stop_y):
                pixel = image.get_pixel(x, y)
                for i in range(3):
                    if not lower[i] <= pixel[i] <= upper[i]:
                        break
                else:
                    num_color_pixels += 1

        self.value = num_color_pixels / num_pixels
