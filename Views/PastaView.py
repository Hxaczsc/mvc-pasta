class PastaView:
    def __init__(self, controller):
        self.controller = controller


    def print_restaurant_menu(self):
        print(self.controller.get_restaurant_menu)

    def print_web_menu(self):
        print(self.controller.get_web_menu)