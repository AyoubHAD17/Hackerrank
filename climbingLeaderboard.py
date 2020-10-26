def binarySearchIterative(array, x):
    left = 0
    right = len(array) - 1
    index = [0, 0]
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            index[1] = array[mid]
            index[0] = True
            return index
        elif x > array[mid]:
            index[1] = array[mid]
            right = mid - 1
        else:
            index[1] = array[mid]
            left = mid + 1
    index[0] = False
    return index

def climbingLeaderboard(ranked, player):
    finalArray = list()
    table = dict()
    tracker = 0
    for item in range(len(ranked)):
        tracker+=1
        try:
            test = table[ranked[item]]
            tracker-=1
        except KeyError:
            table.setdefault(ranked[item], tracker)
    for i in range(len(player)):
        where = binarySearchIterative(ranked, player[i])
        if where[0]:
            finalArray.append(table[where[1]])
        else:
            if player[i] > where[1]:
                if table[where[1]] == 1:
                    finalArray.append(1)
                else:
                    finalArray.append(table[where[1]])
            else:
                finalArray.append(table[where[1]] + 1)
    return finalArray