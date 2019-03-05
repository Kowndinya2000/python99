import math
def isPrime(x):
    temp = int(math.sqrt(x))
    for y in range(2,temp+1):
        if(x % y == 0):
            return False
    return True

def GoldBatch(x,L):
    for tmp in range(3,x):
        if(isPrime(tmp)):
            if(isPrime(x-tmp)):
                L.append(tmp)
                L.append(x-tmp)
                break
    print(L)
lis = []
GoldBatch(10,lis)
lis2 = []
GoldBatch(30,lis2)
