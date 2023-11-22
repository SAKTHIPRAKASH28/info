import sympy
def diffie(n):
    node=0
    for i in range(1,n):
        alpha=i
        if(primitive(n,alpha)):
            node=alpha
            break
    x=sympy.randprime(0,n+1)
    y=sympy.randprime(0,n+1)
    while True:
        if x!=y:
            a=(node**x)%n
            b=(node**y)%n
            if a==b:
                return "Error"
            else:
                k1=(b**x)%n
                k2=(a**y)%n
            break
        else:
           x=sympy.randprime(0,n+1)
           y=sympy.randprime(0,n+1)
    print(x,y,a,b,k1,k2,node)
    if(k1==k2):
        print("handshaking done")
        print("The keys are",k1,k2)
        return (x,y,node,a,b)
    else:
        return "Error"
def Man_in_Middle(n,x,y,node,a,b):
    x1=sympy.randprime(0,n+1)
    y1=sympy.randprime(0,n+1)
    while True:
        if x1!=y1:
            a1=(node**x1)%n
            b1=(node**y1)%n
            if a1==b1:
                return "Error"
            else:
                h_key1=(a**y1)%n
                h_key2=(b**x1)%n
                key1=(b1**x)%n
                key2=(a1**y)%n
            break
        else:
            x1=sympy.randprime(0,n+1)
            y1=sympy.randprime(0,n+1)
    print("The key2 of hacker and sender ",h_key1,key1)
    print("The key1 of hacker and receiver",h_key2,key2)     
def primitive(n,alpha):
    list=[]
    for i in range(1,n):
        list.append((alpha**i)%n)
    if(len(list)==len(set(list))):
        return True
    else:
        return False
n=int(input("enter a prime number:"))
print("Diffie algorithm")
list=diffie(n)
print("Man in the middle attack")
Man_in_Middle(n,list[0],list[1],list[2],list[3],list[4])