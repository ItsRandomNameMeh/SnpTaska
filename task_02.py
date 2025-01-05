def coincidence(list = [],range = (0,0)):#ставим значения по умолчанию
    massi = []
    mini = range[0]
    maxi = range[len(range)-1]
    for j in list:#проходим по списку элементв
            if (type(j) in [int,float])and((j <= maxi) and (j >= mini)):#если это число
                massi.append(j)#и оно находится в заданном интервали, добавим элемент
    return massi#в конец нового массива, а затем его вернем

print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
print(coincidence()) # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5 ]