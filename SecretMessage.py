encryptedMesseage: str = input('Введите сообщение: ')
decryptedMessage = ''

for i in range(len(encryptedMesseage)):
    if encryptedMesseage[i].isupper():
        decryptedMessage += encryptedMesseage[i]
print(decryptedMessage)
