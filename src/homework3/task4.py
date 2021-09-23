# Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо
# посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

str_ = '3 1 1 1 1 2 2 3 3'
list_ = str_.split()
pair_ = 0
numbers_ = {num: list_.count(num) for num in list_}
for element in numbers_:
    count_ = (numbers_[element] * (numbers_[element] - 1)) / 2
    pair_ = pair_ + count_
print(int(pair_))
