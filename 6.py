# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint

count = 10
our_random_number = randint(1, 100)
while count != 0:
    numb = int(input("Введите число от 1 до 100: "))
    count -= 1
    if our_random_number == numb:
        print('Вы угадали число!')
        break
    elif numb > our_random_number:
        print('Ваше число больше.')
    elif numb < our_random_number:
        print('Ваше число меньше.')
    if count == 0:
        print(f'Вы проиграли, заданное число было - {our_random_number}')
