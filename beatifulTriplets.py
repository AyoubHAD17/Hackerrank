def beautifulTriplets(d = 3, arr = [1,2,4,5,7,8,10]):
    count = 0
    table = dict()
    for item in range(len(arr)):
        table.setdefault(arr[item], item)
    print(table)

beautifulTriplets()
    


