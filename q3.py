import math
def isPrime(x):
    temp = int(math.sqrt(x))
    for y in range(2,temp+1):
        if(x % y == 0):
            return False
    return True

def primeFactors(x):
    answer = []
    for tmp in range(2,x):
        if(isPrime(tmp)):
            if(x % tmp == 0):
                count = 0;
                lis = []
                while(x % tmp == 0):
                    count = count + 1
                    x = x/tmp
                lis.append(tmp)
                lis.append(count)
                answer.append(lis)
    print(answer)
primeFactors(270)
primeFactors(45)
