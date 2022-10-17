# Определить, как часто встречается определенная буква в строке.
def get_count_char(str_):
    default = 0
    no_spaces = "".join(str_.split())
    lowercase = no_spaces.lower()
    letter_dict = {}
    for letter in lowercase:
        if letter.isalpha():
            letter_dict[letter] = letter_dict.get(letter, default) + 1
    return letter_dict
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
