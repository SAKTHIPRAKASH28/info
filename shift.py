import random 
def encrpyt(s):
    res=''
    for i in range(len(s)):
        if s[i].isupper():
            res+=chr((ord(s[i])+key-65)%25 +65)
        elif s[i].islower():
            res+=chr((ord(s[i])+key-97)%25 +97)
            
    return res
def decrpyt(res):
    text=''
    for i in range(len(res)):
        if s[i].isupper():
            text+= chr((ord(res[i])-key-65)%25 +65)
        elif s[i].islower():
              text+= chr((ord(res[i])-key-97)%25 +97)
            
    return text
def brute(s,out):
    k=  k=ord(out[0])-ord(s[0])
    if k>0:
        return k 
    else:
        return k+25
    
s=input("Enter the plain text:")
key=random.randint(0,25)
out=encrpyt(s)
print("The encrpyted text is:" ,out)
print("The decrypted text is :" ,decrpyt(out))
print("The key is found is:" ,brute(s,out))
print("The original key is:",key)