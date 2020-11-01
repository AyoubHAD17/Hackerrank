from math import inf




def biggerIsGreater(string):
    table = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    numbers = list()
    theBiggest = -inf
    for al in range(len(string)):
        if table[string[al]] > theBiggest:
            theBiggest = table[string[al]]
        numbers.append(table[string[al]])
    if numbers[0] == theBiggest:
        for i in range(-1, -len(numbers), -1):
            if numbers[i] > numbers[i-1]:
                temp = numbers[i-1]
                numbers[i-1] = numbers[i]
                numbers[i] = temp
                break
    elif numbers[-1] == theBiggest:
        temp = numbers[-1]
        numbers[-1] = numbers[-2]
        numbers[-2] = temp
    else:
        numbers.sort(reverse = True)
        temp = numbers[0]
        numbers[0] = numbers[1]
        numbers[1] = temp
        temp = numbers[1]
        numbers[1] = numbers[-1]
        numbers[-1] = temp

    finalOutput = ""

    for item in range(len(numbers)):
        finalOutput+=list(table.keys())[numbers[item]-1]

    return finalOutput

biggerIsGreater(input())