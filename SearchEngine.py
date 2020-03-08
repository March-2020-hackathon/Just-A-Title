from ImageLoader import *
from RealImageLoader import *
import re, json


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
                inappropriate.append(i)
                break
        to_ret = {'bool': choice, 'violation': inappropriate}
        return to_ret


if __name__ == "__main__":
    image = "test_1.jpg"
    preference = "halal"
    s = InputData(image)
    print(s.is_ok(preference))


