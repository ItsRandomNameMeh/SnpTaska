import re #импортируем библиотеку рег. выражений и с ее помощью убираем знаки препинания
def count_words(string):
    string = re.sub(r'[^\w\s]',"",string)#регулярнео выражение удаляющее знаки преминания
    string = string.lower()#переводим строку в нижний регистр
    word = string.split()#убираем пробелы
    new_dic = {}
    for i in word:
        if i in new_dic:#если такой ключ уже есть, увеличиваем число
            new_dic[i] = new_dic[i]+1
        elif i:#если нет - записываем по ключу 1
            new_dic[i] = 1
    return new_dic

print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1,
# #"canal": 1, "panama": 1, "plan": 1}
# print(count_words('Doo bee doo bee doo')) # => {"doo": 3, "bee": 2}
# print(count_words('fish file o fish')) # => {"doo": 3, "bee": 2}