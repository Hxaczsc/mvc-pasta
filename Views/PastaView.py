class PastaView:
    def __init__(self, controller):
        self.controller = controller


    def print_restaurant_menu(self):
        print(self.controller.get_restaurant_menu)

    def print_web_menu(self):
        print(self.controller.get_web_menu)

    def set_ingredients(self, user_rights, new_ingredients):
        if type(new_ingredients) is not list:
            print("Неверный тип данных")
        elif self.controller.set_ingredients(user_rights, new_ingredients) == "forbidden":
            print("Нет права доступа")
        else:
            print(self.controller.set_ingredients(user_rights, new_ingredients))

    def set_price(self, user_rights, new_price):
        if new_price.isdigit is False:
            print("Неверный тип данных")
        elif self.controller.set_price(user_rights, new_price) == "forbidden":
            print("Нет права доступа")
        else:
            print(self.controller.set_price(user_rights, new_price))

    def set_weight(self, user_rights, new_weight):
        if new_weight.isdigit is False:
            print("Неверный тип данных")
        elif self.controller.set_weight(user_rights, new_weight) == "forbidden":
            print("Нет права доступа")
        else:
            print(self.controller.set_weight(user_rights, new_weight))