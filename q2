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
                while(x % tmp == 0):
                    x = x/tmp
                answer.append(tmp)
    print(answer)
primeFactors(270)
primeFactors(45)
print(isPrime(2))
print(isPrime(45))
