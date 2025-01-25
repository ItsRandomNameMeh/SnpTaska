"""
Класс десерт в конструкторе имеет значения по умолчанию для названия и калорий
(т.к. это не обязательные параметры)
 __ для указания на приватность полей
Калорий по умолчанию очень много, чтобы не было ложного срабатывания метода is_healthy
"""
class Dessert:
    def __init__(self, name: str = "NoName", calories: int = 2000000):
        self.__name = name
        self.__calories = calories

    def is_healthy(self):
        return self.__calories < 200

    def is_delicious(self):
        return True

    def get_calories(self):
        return self.__calories

    def get_name(self):
        return self.__name

    def set_name(self, name2):
        self.__name = name2

    def set_calories(self, calories2):
        self.__calories = calories2


"""
Класс желейных бобов в конструкторе имеет значения по умолчанию для названия, калорий и вкуса
(т.к. это не обязательные параметры)
 __ для указания на приватность полей
Калорий по умолчанию очень много, чтобы не было ложного срабатывания метода is_healthy
Вкус по умполчанию None, т.к. сказано что 'невкусные' бобы только черно-лакричные
"""

class JellyBean(Dessert):
    def __init__(self, name: str = "NoName", calories: int = 2000000, flavor: str = "someFlavor"):
        super().__init__(name, calories)
        self.__flavor = flavor

    def get_flavor(self):
        return self.__flavor

    def set_flavor(self, flavor):
        self.__flavor = flavor

    def is_delicious(self):
        return self.__flavor != "black licorice"




