"""
Класс десерт в конструкторе имеет значения по умолчанию для названия и калорий
(т.к. это не обязательные параметры)
 __ для указания на приватность полей
Калорий по умолчанию очень много, чтобы не было ложного срабатывания метода is_healthy
"""
class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories
    def is_healthy(self):
        if isinstance(self.__calories, (int,float)):
            return self.__calories<200
        return False

    @property
    def calories(self):
        return self.__calories
    @calories.setter
    def calories(self,calories2):
        self.__calories = calories2
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name2):
        self.__name = name2

    def is_delicious(self):
         return True

dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)

dessert.calories = 199.9999
print(dessert.is_delicious())
if not dessert.is_delicious(): raise Exception("Invalid method result")
print(dessert.calories)
print(dessert.is_healthy())
if not dessert.is_healthy(): raise Exception("Logical error. Method must return True")

