# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def our_programm():
    n1 = int(input('Введите первое число: '))
    n2 = int(input('Введите второе число: '))
    sum_1 = sum_digits(n1)
    sum_2 = sum_digits(n2)
    if sum_1 > sum_2:
        print(f'Наибольшее по сумме цифр, число - {n1}, с суммой {sum_1}')
    else:
        print(f'Наибольшее по сумме цифр, число - {n2}, с суммой - {sum_2}')


def sum_digits(n):
    sumd = 0
    while n > 0:
        n, d = divmod(n, 10)
        sumd += d
    return sumd


our_programm()
