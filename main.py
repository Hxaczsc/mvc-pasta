import os.path

from Models.PastaModel import PastaModel
from Controllers.PastaController import Pastacontroller
from Views.PastaView import PastaView

if __name__ == "__main__":
    ImagePath = os.path.abspath("D:/PastaCarbonara.jpg")
    print(ImagePath)
    Pasta_model = PastaModel(name="Карбонара",
                                 ingredients=["Спагетти", "оливковое масло", "чеснок", "ветчина", "яичный желток",
                                              "сыр пармезан", "сливки", "соль", "черный перец"],
                                 price=475,
                                 weight=350,
                                 picture=ImagePath,
                                 client_ingredients=[]
                                 )

    Pasta_controller = Pastacontroller(Pasta_model)
    Pasta_view = PastaView(Pasta_controller)
    Pasta_view.print_restaurant_menu()
    Pasta_view.print_web_menu()
    print("---")
    Pasta_view.set_ingredients("user", ["Спагетти", "оливковое масло", "ветчина", "яичный желток", "сыр пармезан", "сливки", "соль"])
    Pasta_view.set_ingredients("Admin",("Спагетти", "оливковое масло", "ветчина", "яичный желток", "сыр пармезан", "сливки","соль"))
    Pasta_view.set_ingredients("IsSuperoser",["Спагетти", "оливковое масло", "ветчина", "яичный желток", "сыр пармезан", "сливки","соль"])
    print("---")
    Pasta_view.set_price("user", "500")
    Pasta_view.set_price("IsStaff", "Пятьсот")
    Pasta_view.set_price("ISSuperuser", "500")
    print("---")
    Pasta_view.set_weight("user", "375")
    Pasta_view.set_weight("IsStaff", "Триста семьдесят пять")
    Pasta_view.set_weight("ISSuperuser", "375")
    print("---")
    Pasta_view.print_restaurant_menu()

