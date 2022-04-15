def linearCongruential(Xo, m, a, c,
                             randomNums,
                             numberOfRandom):
    randomNums.append(Xo)
    for i in range(1, numberOfRandom):
        randomNums.append(((randomNums[i - 1] * a) +
                                         c) % m)
    
    
def customRandom(number):
    a=1
    c=1
    prandomNums = []
    nrandomNums =[]
    Xo = -20
    m =100
    a =4
    c = 3
    # numberOfRandom = 50
    numberOfRandom = int(number)
    linearCongruential(Xo, m, a, c,
                            prandomNums,
                            numberOfRandom)
    Xo = 100
    m = -100

    linearCongruential(Xo, m, a, c,
                            nrandomNums,
                            numberOfRandom)

    z=1
    randoms=[]
    for i in range(0,len(prandomNums)):
        randoms.append(prandomNums[i])
        for j in range(i,z):
            randoms.append(nrandomNums[j])
            z=z+1
    return randoms

print(customRandom(50))
