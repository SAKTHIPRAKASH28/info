import hashlib
def encrypt(msg,k):
    res=''
    for i in range(len(msg)):
        res+=chr(ord(msg[i])^ord(k[i%len(k)]))
    return res
def decrypt(msg,k):
    out=''
    for i in range(len(msg)):
        out+=chr(ord(msg[i])^ord(k[i%len(k)]))
    return out
def authenticate(ans,hc,n):
    key=ans[:n]
    str=ans[n:]

    print("the decrypted message is:",key)
    if str==hc:
        print("authentication pass")
    else:
        print("failed")
msg=input("enter the string:")
n=len(msg)
k=input("enter the key")
h=hashlib.sha256()
h.update(msg.encode())
hc=h.hexdigest()
msg=msg+hc
enc=encrypt(msg,k)
print("the encrypted text is :",enc)
dec=decrypt(enc,k)
authenticate(dec,hc,n)