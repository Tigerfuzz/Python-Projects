currentnum = 0
primenums = []
while True:
    isPrime = True
    for dnum in range(1, currentnum):
        if currentnum % dnum == 0:
            if dnum != currentnum and dnum != 1:
                isPrime = False
                break
    if isPrime == True:
        primenums.append(currentnum)
        print(currentnum)
    currentnum = currentnum + 1
