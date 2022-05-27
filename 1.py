# Написать программу, которая будет складывать,
# вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться
# при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

our_operator = 1

while our_operator != 0:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    our_operator = input("Введите знак вычисления (+, -, *, /): ")
    if our_operator == '+':
        plus = first_number + second_number
        print(plus)
    elif our_operator == '-':
        minus = first_number - second_number
        print(minus)
    elif our_operator == '*':
        multiplication = first_number * second_number
        print(multiplication)
    elif our_operator == '/':
        try:
            division = first_number / second_number
            print(division)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
    else:
        print("Неверный знак операции.")
