def isprime(number,primes):
    if number == 1:
        return False
    
    for j in primes:
        if j*j>number:
            break
        elif number%j == 0:
            return False
    return True

def ispalindrome(number):
    if str(number)==str(number)[::-1]:
        return True
    return False


n = int(input())
primes=[]

for number in range(2,1100000):
    if isprime(number,primes):
        primes.append(number)
        if ispalindrome(number) and number>=n:
            print(number)
            break
