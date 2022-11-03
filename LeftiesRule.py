stringArr = ["left", "bright aright", "left", "stop"]

def ReplaceRightWithLeft(string):
    return string.replace("right", "left")

def GlueTheLines(stringArr):
    string = stringArr[0]
    for i in range(1, len(stringArr)):
        string += ',' + ReplaceRightWithLeft(stringArr[i])
    return string

print(GlueTheLines(stringArr))

