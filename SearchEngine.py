from ImageLoader import *
from RealImageLoader import *

class InputData:
    def __init__(self, image):
        data = ImageReader(image);
        
    def is_ok(self, preference):
        database = FoodClasses()
        database.ingredient_loader()
        choice = True
        for i in self.data:
            if preference not in database.ingredient_to_classes(i):
                choice = False
                break;  
        return choice
        
if __name__ == "__main__":
    image = "test_1.jpg"
    preference = "vegan"
    s = InputData(image)
    print(s.is_ok(preference))



