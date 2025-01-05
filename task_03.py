def max_odd(array):
    Good = [int, float]#массив подходящих нам значений (числа)
    maxi = -9998
    for i in array:
        if((type(i) in Good) and (i>maxi) and (i%2 != 0)):#если это число, оно нечетное и сейчас самое большое то сохраним
            maxi = i
    return int(maxi) if maxi != -9998 else None#если это не число по умолчанию - вернуть макисмальное, иначе None



print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4])) # => None