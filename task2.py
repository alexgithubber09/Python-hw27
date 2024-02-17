import string
from string import punctuation

ourString = "uhfn,/.784j?klvHH jkhUI jFD 97 //"
listOfMarks = []

def lower_chars(ourString):
    return print('Количество строчных букв: ' + str(sum(map(str.islower, ourString))))

def upper_chars(ourString):
    return print('Количество прописных букв: ' + str(sum(map(str.isupper, ourString))))

def digits(ourString):
    return print('Количество цифр: ' + str(sum(map(str.isdigit, ourString))))

def punctuation_number(ourString):
    for i in ourString:
        if i in string.punctuation:
            listOfMarks.append(i)
    count = len(listOfMarks)
    return print('Количество знаков пунктуации: ' + str(count))


lower_chars(ourString)
upper_chars(ourString)
digits(ourString)
punctuation_number(ourString)
