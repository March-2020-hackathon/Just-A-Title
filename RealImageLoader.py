"""
This file loads an images and read the words on that image.
Doing some comparisons maybe
"""
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class ImageReader:
    """
    This class reads images and stores the words on the image
    """
    def __init__(self):
        """
        Initializes an image reader.
        """
        self.content = dict()

    def read_image(self, image):
        """
        This function takes the name of an image and reads the image and stores the words
        of the image
        :param image: string
        :return: sentence: string
        """
        if image not in self.content:
            img = cv2.imread(image)
            text = pytesseract.image_to_string(img).lower()
            self.content[image] = text
            return text
        return self.content[image]
