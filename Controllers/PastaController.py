class Pastacontroller:
    def __init__(self, model):
        self.model = model

    def restaurant_menu(self):
        pasta_data = (f"Паста :: {self.model.get_name()}\n"
                      f"Цена :: {self.model.get_price()}\n"
                      f"Вес :: {self.model.get_weight()}\n"
                      f"Состав :: {", ".join(self.model.get_ingredients())}\n")
        return pasta_data

    def web_menu(self):
        pasta_data = (f"Паста :: {self.model.get_name()}\n"
                      f"Цена :: {self.model.get_price()}\n"
                      f"Вес :: {self.model.get_weight()}\n"
                      f"Состав :: {", ".join(self.model.get_ingredients())}\n"
                      f"Фото :: {self.model.get_picture}")
        return pasta_data

