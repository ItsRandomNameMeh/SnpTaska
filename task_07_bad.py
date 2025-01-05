def index_word(string, array):
    flag = True
    j = 0
    for find_char in array[j]:#берем первое слово из каждого "подмассива"
        for char in string:#построчно идем по новому слову
            print(char, find_char)
            if char in find_char:#если буквы нового слова есть в текщуем "подмассиве",все ок
                continue
            elif(j+1 < len(array)):#если нет и подмассивы не кончились, дальше
                j+=1
                print(f"увеличили j, теперь смотрим {array[j]}")
                continue
            else:#если нет и кончились подмассивы, то такой анаграммы еще нет
                flag = False
                break
    return flag, j


def combine_anagrams(words_array):
    massi = []
    for word in words_array:
        word = word.lower()
        if (len(massi) == 0):
            massi.append([word])
        else:
            c = index_word(word, massi)
            print(c, word, massi)
            if(c[0] == True):
                massi[c[1]].append(word)
            else:
                massi.append([word])
    print(massi)

combine_anagrams(["cars", "racs","for", "potatoes",  "four", "scar", "creams", "scream"])
# => [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"] ]

