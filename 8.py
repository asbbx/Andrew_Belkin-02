# 8. Посчитать, сколько раз встречается
# определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра,
# которую необходимо посчитать, задаются вводом с клавиатуры.

num = input('Введите последовательность чисел: ')
curr_num = input('Введите число, которое надо посчитать: ')
counter = 0
for i in num:
    if i == curr_num:
        counter += 1
print(f'В заданной последовательности, '
      f'цифра {curr_num} встречается {counter} раз(а)')
