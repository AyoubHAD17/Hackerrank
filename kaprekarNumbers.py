def kaprekarNumbers(p, q):
    table = list()
    for i in range(p, q+1):
        t = len(str(i))
        beta = (i**2) % (10**t)
        alpha = ((i**2) - beta) // (10**t)
        if beta + alpha == i:
            table.append(str(i))
    if table:
        print(" ".join(table))
    else:
        print("INVALID RANGE")


kaprekarNumbers(1, 99999)
