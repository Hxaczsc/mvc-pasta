class Pasta:
    def __init__(self, name: str, ingredients: list, price: float, weight: float, client_ingredients: list = None):
        self.__name = name
        self.__ingredients = ingredients
        self.__price = price
        self.__weight = weight
        if client_ingredients is not None:
            self.__client_ingredients = client_ingredients
        else:
            self.__client_ingredients = []

    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight

    def get_client_ingredients(self):
        return self.__client_ingredients
