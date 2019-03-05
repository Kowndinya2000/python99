import math
def isPrime(x):
    temp = int(math.sqrt(x))
    for y in range(2,temp+1):
        if(x % y == 0):
            return False
    return True
def gold(x):
     L = []
    for tmp in range(3,x):
        if(isPrime(tmp)):
            if(isPrime(x-tmp)):
                L.append(tmp)
                L.append(x-tmp)
                break
    length = len(L)
    if(length != 0):
        print(L)
def GoldBatch(x,y):
    for t in range(x+1,y):
        gold(t)

GoldBatch(10,30)
