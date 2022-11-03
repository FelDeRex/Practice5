numberStr: str = input('Введите целое число (оно должно быть от 1 до 9): ')
number: int = int(numberStr)

if(number >= 1) & (number <= 9):
    tempNumber = '1'
    numberSequence = ''
    for i in range(number):
        numberSequence += tempNumber
        tempNumber = chr(ord(tempNumber)+1)
    print(numberSequence)
else:
    print('Число должно быть от 1 до 9')