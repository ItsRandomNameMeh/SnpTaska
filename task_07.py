def combine_anagrams(words_array):
    massi = {}#создаем словарь (в котором дальше будут массивы)
    i = 0
    for word in words_array:
        miniWord = ''.join(sorted(word.lower()))#превращаем слово в последовательность букв в алфавитном порядке
        if miniWord in massi:#если такой ключ есть, то в его массив добавляем исходное слово
            massi[miniWord].append(word)
        else:
            massi[miniWord] = [word]
    print(list(massi.values()))
    return list(massi.values())#возвращаем список значений ключей (т.е сами слова)

combine_anagrams(["cars", "racs","for", "potatoes",  "four", "scar", "creams", "scream"])
# => [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"] ]

