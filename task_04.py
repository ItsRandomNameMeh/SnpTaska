def sort_list(list = []):
    if (len(list) == 0):
        print(list)
        return list
    maxi = max(list)#выбираем максимальный и минимальный элементы массива
    mini = min(list)
    for i in range(len(list)):
        if list[i] == mini:#если встретили минимальный - заменяем максимальным
            list[i] = maxi
        elif list[i] == maxi:#если встретили максимальный - заменяем минимальным
            list[i] = mini
    list.append(mini)#добавляем любой минимальный в конец, даже для списка с 1 элементом (он минимален по умолчанию)
    print(list)
    return list

sort_list([]) # => []
sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
sort_list([1]) # => [1, 1]
sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]