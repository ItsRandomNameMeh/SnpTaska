"""
Класс десерт в конструкторе имеет значения по умолчанию для названия и калорий
(т.к. это не обязательные параметры)
 __ для указания на приватность полей
Калорий по умолчанию очень много, чтобы не было ложного срабатывания метода is_healthy
"""
class Dessert:
    def __init__(self, name = None, calories = None):
        if isinstance(name, str) and isinstance(calories, (int,float)):
            self.__name = name
            self.__calories = calories
        else:
            self.__name = None
            self.__calories = None
    def is_healthy(self):
        if (isinstance(self.__calories, (int,float)) and
                self.__calories < 200):
            return True
        else:
            return False
    def is_delicious(self):
        return True
    def get_callories(self):
        return self.__calories
    def get_name(self):
        return self.__name
    def set_name(self,name2):
        self.__name = name2
    def set_calories(self,calories2):
        self.__calories = calories2

someCake = Dessert("Maffin",calories=199.9999)
