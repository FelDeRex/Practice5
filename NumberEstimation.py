numberStr: str = input('Введите целое число: ')
number: int = int(numberStr)

if number % 2 == 0:
    if (number >= 2) & (number < 5):
        print('Неплохо')
    elif (number >= 6) & (number <= 20):
        print('Так себе')
    elif (number > 20):
        print('Отлично')
else:
    print('Плохо')