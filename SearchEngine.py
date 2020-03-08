from ImageLoader import *
from RealImageLoader import *
import re


class InputData:
    def __init__(self, im):
        self.image_reader = ImageReader()
        self.content = re.split('\n|,', self.image_reader.read_image(im))
        
    def is_ok(self, preference):
        database = FoodClasses()
        database.ingredient_loader()
        choice = True
        inappropriate = []
        print(self.content)
        for i in self.content:
            if not database.ingredient_to_classes(i):
                continue
            if preference not in database.ingredient_to_classes(i):
                choice = False
                inappropriate = self.content[i]
                break
        return choice, inappropriate


if __name__ == "__main__":
    image = "WIN_20200307_19_41_20_Pro.jpg"
    preference = "vegan"
    s = InputData(image)
    print(s.is_ok(preference))



