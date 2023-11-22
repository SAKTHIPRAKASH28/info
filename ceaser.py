def encrpyt(s):
    res=''
    for i in range(len(s)):
        if s[i].isupper():
            res+=chr((ord[i]+3-65)%25 +65)
        elif s[i].islower():
            res+=chr((ord(s[i])+3-97)%25 +97)
            
    return res
def decrpyt(res):
    text=''
    for i in range(len(res)):
        if s[i].isupper():
            text+= chr((ord(res[i])-3-65)%25 +65)
        elif s[i].islower():
              text+= chr((ord(res[i])-3-97)%25 +97)
            
    return text
s=input("Enter the plain text:")
print("The encrpyted text is:" ,encrpyt(s))
print("The decrypted text is :" ,decrpyt(encrpyt(s)))