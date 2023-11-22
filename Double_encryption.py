def encrpyt(s):
    res=''
    for i in range(len(s)):
        if s[i].isupper():
            res+=chr((ord(s[i])+3-65)%25 +65)
        elif s[i].islower():
            res+=chr((ord(s[i])+3-97)%25 +97)
            
    return res
def decrpyt(res):
    text=''
    for i in range(len(res)):
        if res[i].isupper():
            text+= chr((ord(res[i])-3-65)%25 +65)
        elif res[i].islower():
              text+= chr((ord(res[i])-3-97)%25 +97)
            
    return text
def encrypt1(s,k):
    val=''
    for i in range(len(s)):
        val+=chr(ord(s[i])^ord(k[i%len(k)]))
    return val
def decrpyt1(s,k):
    ans=''
    for i in range(len(s)):
        ans+=chr(ord(s[i])^ord(k[i%len(k)]))
    return ans 
msg=input("Enter the plain text:")
k=input("Enter the key2:")
c1=encrpyt(msg)
c2=encrypt1(c1,k)
d2=decrpyt1(c2,k)
print("The 1st level Cipher text :",c1)
print("The 2nd level Cipher text is :",c2)
print("The 2nd level Decipher Text is:",d2)
print("The plain Text is :",decrpyt(d2))