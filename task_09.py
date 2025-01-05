'''
метод сортировки уже объединенного словаря
'''
def sorted(dict):
    new_value = []
    new_dcit = {}
    for values in dict.values():#все значения (по которым и будет сортировка)
        new_value.append(values)#мы считываем в массив, а затем массив сортируем
    new_value.sort()
    for i in new_value:#проходим по отсортированному массив и подбираем ему ключ
        for k,v in dict.items():#в полученном из вне словаре
            if v == i:#когда нашли его ключ, записываем их в новый словарь
                new_dcit[k] = i#т.к. мы идем по массиву по возрастанию, то все ключи
                del dict[k]#со значениями пишутся тоже по возрастанию
                break
    return new_dcit

'''
метод соединения 2 словарей в один
'''
def connect_dicts(dict1, dict2):
    sum_first = 0
    sum_second = 0
    new_dictionary = {}
    for i in dict1:
        sum_first+=dict1[i]
    for j in dict2:
        sum_second+=dict2[j]
    new_dict1 = {k:v for k,v in dict1.items() if v > 10}#сохраняем все пары, где значение > 10
    new_dict2 = {k: v for k, v in dict2.items() if v > 10}#для второго сейм
    if sum_second>=sum_first:#если сумма 2 больше или равны приоритет все равно второму
        for k,v in new_dict2.items():
            new_dictionary[k] = v#в новый словарь по ключу добавляем значения из dict2
        for k,v in new_dict1.items():
            if k not in new_dictionary:#по остаточному принципу из dict1, т.к. он не приоритет
                new_dictionary[k] = v
    else:#в случаи когда сумма 1 больше, то все наоборот
        for k, v in new_dict1.items():
            new_dictionary[k] = v
        for k, v in new_dict2.items():
            if k not in new_dictionary:
                new_dictionary[k] = v
    new_dictionary = sorted(new_dictionary)
    print(new_dictionary)
    return new_dictionary

connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # =>
#{ "c": 11, "b": 12 }
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # =>
#{ d: 11, "c": 12, "a": 13 }
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) # =>
#{ "c": 11, "b": 12, "a": 15 }