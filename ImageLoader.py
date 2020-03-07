"""
This files takes the food classification database and loads the time for future use.
"""
import json


class FoodClasses:
    """
    A class representing the classes of foods
    """

    def __init__(self):
        """
        Initializes a FoodClass object which stores ingredients of foods to their corresponding classes
        """
        self._corresponding_classes = dict()
        self._corresponding_ingredients = dict()

    def ingredient_loader(self):
        """
        This function loads the food classification and loads
        :return: the loaded data in an efficient structure
        """
        with open('Database.json') as json_file:
            data = json.load(json_file)
            for key in data:
                if key not in self._corresponding_ingredients:
                    self._corresponding_ingredients[key] = data[key]
                for ingredients in data[key]:
                    if ingredients not in self._corresponding_classes:
                        self._corresponding_classes[ingredients] = [key]
                    else:
                        self._corresponding_classes[ingredients].append(key)
            for ingredients in self._corresponding_classes:
                self._corresponding_classes[ingredients] = set(self._corresponding_classes[ingredients])
                self._corresponding_classes[ingredients] = list(self._corresponding_classes[ingredients])

    def ingredient_to_classes(self, ingredient):
        """
        This function takes the name of an ingredient and returns
        a list of its corresponding classes. Return None if not found.
        :param ingredient: string
        :return: class: List
        """
        if ingredient in self._corresponding_classes:
            return self._corresponding_classes[ingredient]

    def class_to_ingredients(self, class_):
        """
        This function takes the name of the class and returns a list of
        corresponding ingredients. Return None if not found.
        :param class_: String
        :return: ingredient: List
        """
        if class_ in self._corresponding_ingredients:
            return self._corresponding_ingredients[class_]

    def get_corresponding_classes(self):
        """
        Returns a dictionary where key is the ingredients and values are the corresponding
        classes
        :return: dict
        """
        return self._corresponding_classes

    def get_corresponding_ingredients(self):
        """
        Returns a dictionary where key is the classes and values are the ingredients
        classes
        :return: dict
        """
        return self._corresponding_classes
    
            

