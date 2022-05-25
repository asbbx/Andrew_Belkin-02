# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

our_number = int(input('Введите число: '))
counter_even = 0
counter_odd = 0
while our_number > 0:
    if our_number % 2 == 0:
        counter_even += 1
    else:
        counter_odd += 1
    our_number //= 10

print(f'Четных: {counter_even} Нечетных: {counter_odd}')
