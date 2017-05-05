
N = 100
eachNumber = 1

while eachNumber < 100:
    isPrime = True
    for advisor in range(2, int(eachNumber / 2) + 1):
        if eachNumber % advisor == 0:
            isPrime = False
            break
    if isPrime == True:
        print(str(eachNumber) + " ")
    eachNumber = eachNumber + 1