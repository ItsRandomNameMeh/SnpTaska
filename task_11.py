"""
Класс десерт в конструкторе имеет значения по умолчанию для названия и калорий
(т.к. это не обязательные параметры)
 __ для указания на приватность полей
Калорий по умолчанию очень много, чтобы не было ложного срабатывания метода is_healthy
"""
class Dessert:
    def __init__(self, name: str = "NoName", calories: int=2000000):
        self.__name = name
        self.__calories = calories
    def is_healthy(self):
        if self.__calories < 200:
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

someCake = Dessert("Maffin",calories=20)
coconat_cake = Dessert()

