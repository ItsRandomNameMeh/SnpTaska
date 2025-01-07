import re #библиотека для работы с регулярными выражениями
def is_palindrome(test_string):
    if(type(test_string)!=str):
        test_string = str(test_string)
    test_string = test_string.replace(' ','')#игнорирование пробелов
    test_string = test_string.lower()#игнорирование регистра
    test_string = re.sub(r'[^\w\s]',"",test_string)#регулярнео выражение удаляющее знаки преминания
    if(test_string == test_string[::-1]):
        return True
    return False

print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra")) # => False
print(is_palindrome("AbbA")) # => True
