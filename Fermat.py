import math
def Fermat(a,p):
    if(isPrime(p) and a%p!=1):
        ans=(a**(p-1))%p
        if(ans==1):
            return True
        else:
            return False
def isPrime(n):
    if(n<=1):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True
a=int(input("Enter the value of a:"))
p=int(input("Enter the value of p:"))
print(Fermat(a,p))