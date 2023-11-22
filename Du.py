arr=[1,2,2,3,4,4,4,5,5]
i=0
j=1
while(j<=len(arr)-1):
    if(arr[i]==arr[j]):
        print(arr[i])
        j+=1
    else:
        print(arr[i])
        i+=1
        j=+1
    
    
    