def do_multi(string): #Метод выполняющий умножения и проверку, а были ли числа переданы
    multy = 1#в функцию вообще
    flag_None = True #Если передадим сюда None, то флаг не отработает и вернем None
    for i in string:
        try:
            multy *= int(i)
            flag_None = False
        except:
            continue
    return multy if flag_None==False else None
def multiply_numbers(inputs = None): #Основной метод вычисления
    sumi = -1#Изначально результат отрицательный, если он таким и останется то ничего не происходило
    if type(inputs)==str:
        sumi = do_multi(inputs)
    elif (type(inputs) == int) or (type(inputs) == float):#Случай, когда у нас уже передано число
        sumi = do_multi(str(inputs))
    elif inputs!=None:
        sumi = 1
        for i in inputs:
            sumi*=i
    print(sumi)
    return sumi if sumi != -1 else None


multiply_numbers() # => None #Тут вернет None, хотя принт выведет -1
multiply_numbers('ss') # => None
multiply_numbers('1234') # => 24
multiply_numbers('sssdd34') # => 12
multiply_numbers(2.3) # => 6
multiply_numbers([5, 6, 4]) # => 120