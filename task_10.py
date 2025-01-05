import re #импортируем библиотеку рег. выражений и с ее помощью убираем знаки препинания
def count_words(string):
    string = re.sub(r'[^\w\s]',"",string)#регулярнео выражение удаляющее знаки преминания
    string = string.lower()#переводим строку в нижний регистр
    massi_word = string.split(" ")#убираем пробелы
    new_dic = {}
    for i in massi_word:
        print(i)
        if i in new_dic:#если такой ключ уже есть, увеличиваем число
            new_dic[i] = new_dic[i]+1
        else:#если нет - записываем по ключу 1
            new_dic[i] = 1
    print(new_dic)

count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,
#"canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}