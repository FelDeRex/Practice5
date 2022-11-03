numberStr: str = input('Введите целое число: ')
number: int = int(numberStr)

if number > 0:
    if (number % 3 == 0) & (number % 5 == 0):
        print('Fizz Buzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
else:
    print('Число должно быть положительным')