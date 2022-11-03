string: str = input('Введите строку: ')

def IsThreeWordsInARow(string):
    word = ''
    wordsNumberInARow = 0
    currentSymbolIndex = 0
    while currentSymbolIndex < len(string):

        # Get word
        while currentSymbolIndex < len(string):
            if string[currentSymbolIndex] == ' ':
                break
            word += string[currentSymbolIndex]
            currentSymbolIndex += 1

        if word.isalpha():
            wordsNumberInARow += 1
        else:
            wordsNumberInARow = 0

        if wordsNumberInARow == 3:
            return True

        word = ''
        currentSymbolIndex += 1

    return False

print(IsThreeWordsInARow(string))