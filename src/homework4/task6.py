# Слова
# Во входной строке записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки (\n).
# Определите, сколько различных слов содержится в этом тексте.


def quantity_different_words():
    str_ = 'слова слова разделены  одним или большим числом пробелов ' \
           '\nили символами конца строки \n'
    print(str_)
    new_str = set(str_.split())
    return print('в тексте содержится', len(new_str), 'различных слов')
