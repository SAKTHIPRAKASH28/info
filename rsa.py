from math import gcd

def Totient(p, q):
    return (p-1)*(q-1)

def SmallestCoPrime(n):
    for i in range(2, n):
        if (gcd(i, n) == 1):
            return i
    return 0


def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def inverse(a, b):
    n = 1
    while True:
        if (a*n) % b == 1:
            return n
        n += 1


def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus

    return result

def Encrypt(m, e, n):
    return modular_exponentiation(m, e, n)

def Decrypt(c, d, n):
    return modular_exponentiation(c, d, n)


if __name__ == "__main__":
    p = int(input("Enter p (prime number): "))
    q = int(input("Enter q (a prime number): "))
    message = int(input("Enter a message: "))
   
    if not isPrime(p) or not isPrime(q):
        print("Non prime values")
        exit()
    n = p*q
    Tot = Totient(p, q)
    e=SmallestCoPrime(Tot)
    d=inverse(e,Tot)
    enc = Encrypt(message, e, n)
    dec = Decrypt(enc, d, n)
    print("The encrypted message:",enc)
    print("The decrypted message :",dec)
