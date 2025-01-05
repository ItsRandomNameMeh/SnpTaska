"""
Класс желейных бобов в конструкторе имеет значения по умолчанию для названия, калорий и вкуса
(т.к. это не обязательные параметры)
 __ для указания на приватность полей
Калорий по умолчанию очень много, чтобы не было ложного срабатывания метода is_healthy
Вкус по умполчанию None, т.к. сказано что 'невкусные' бобы только черно-лакричные
"""
class JellyBean:
    def __init__(self, name: str = "NoName", calories: int=2000000, flavor: str = None):
        self.__name = name
        self.__calories = calories
        self.__flavor = flavor
    def is_healthy(self):
        if self.__calories < 200:
            return True
        else:
            return False
    def is_delicious(self):
        return False if self.__flavor=="black licorice" else True

    def get_callories(self):
        return self.__calories
    def get_name(self):
        return self.__name
    def set_name(self,name2):
        self.__name = name2
    def set_calories(self,calories2):
        self.__calories = calories2
    def get_flavor(self):
        return self.__flavor
    def set_flavor(self,flavor2):
        self.__name = flavor2

someCake = JellyBean("Maffin",calories=20)
coconat_cake = JellyBean()
someCake.get_flavor()
print(someCake.is_delicious())

