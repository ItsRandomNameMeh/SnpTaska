from task_11 import Dessert
"""
Класс желейных бобов в конструкторе имеет значения по умолчанию для названия, калорий и вкуса
(т.к. это не обязательные параметры)
 __ для указания на приватность полей
Калорий по умолчанию очень много, чтобы не было ложного срабатывания метода is_healthy
Вкус по умполчанию None, т.к. сказано что 'невкусные' бобы только черно-лакричные
"""

class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor):
        self.__flavor = flavor

    def is_delicious(self):
        return self.__flavor != "black licorice"

myJelly = JellyBean("RedBean")

print(myJelly.is_healthy())


