class Pastacontroller:
    def __init__(self, model):
        self.model = model

    def get_restaurant_menu(self):
        pasta_data = (f"Паста :: {self.model.get_name()}\n"
                      f"Цена :: {self.model.get_price()}\n"
                      f"Вес :: {self.model.get_weight()}\n"
                      f"Состав :: {", ".join(self.model.get_ingredients())}\n")
        return pasta_data

    def get_web_menu(self):
        pasta_data = (f"Паста :: {self.model.get_name()}\n"
                      f"Цена :: {self.model.get_price()}\n"
                      f"Вес :: {self.model.get_weight()}\n"
                      f"Состав :: {", ".join(self.model.get_ingredients())}\n"
                      f"Фото :: {self.model.get_picture}")
        return pasta_data

    def set_ingredients(self, user_rights, new_ingredients):
        if user_rights in ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_ingredients(new_ingredients)
            return "Рецепт успешно изменен"
        else:
            return "Нет права доступа"

    def set_price(self, user_rights, new_price):
        if user_rights in ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_price(new_price)

    def set_weight(self, user_rights, new_weight):
        if user_rights in ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_weight(new_weight)

    def set_picture(self, user_rights, new_picture):
        if user_rights in ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_picture(new_picture)
