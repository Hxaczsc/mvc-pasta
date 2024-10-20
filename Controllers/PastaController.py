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
            return "forbidden"

    def set_price(self, user_rights, new_price):
        int_price = int(new_price)
        if user_rights in ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_price(int_price)
            return "цена изменена"
        else:
            return "forbidden"

    def set_weight(self, user_rights, new_weight):
        int_weight = int(new_weight)
        if user_rights in ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_weight(int_weight)
            return "вес изменен"
        else:
            return "forbidden"

    def set_picture(self, user_rights, new_picture):
        if user_rights in ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_picture(new_picture)
            return "картинка изменена"
        else:
            return "forbidden"
