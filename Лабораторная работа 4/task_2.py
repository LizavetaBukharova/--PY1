def get_count_char(str_1):
    str_1 = "".join(str_1.split())  # избавляемся от пробелов
    str_1 = str_1.lower() # нижний регистр
    dict_ = {}
    deafil_ = 0
    for letter in str_1:
        if letter.isalpha() == True:
            dict_[letter] = dict_.get(letter, deafil_) + 1

    return dict_

def get_count_proc(str_1):
    # str_2 = "".join(str_2.split())  # избавляемся от пробелов
    # str_2 = str_2.lower()  # нижний регистр
    # dict_2 = {}
    # deafil_2 = 0
    len_ = len(str_1)
    dict_2 = []
    # for lett in str_2:
    #     dict_2[lett] = dict_2.get(lett, deafil_2) + 1
    for i, kol in get_count_char(str_1):
        get_count_char(str_1)[i] = kol * 100 // len_
        dict_2 = get_count_char(str_1)
    return dict_2


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(get_count_proc(main_str))
