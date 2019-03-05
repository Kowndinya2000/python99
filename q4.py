import math
def isPrime(x):
    temp = int(math.sqrt(x))
    for y in range(2,temp+1):
        if(x % y == 0):
            return False
    return True

def primeNumbers(lower,upper):
    answer = []
    for tmp in range(lower,upper+1):
        if(isPrime(tmp)):
            answer.append(tmp)
    print(answer)
primeNumbers(10,20)
primeNumbers(10,30)
        
