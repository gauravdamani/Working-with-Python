n=int(input())
arr=list(set(map(int,input().split())))
c=0
if(all([x>0 for x in arr])):
    c=0
    for i in range(len(arr)):
        temp=arr[i]
        rev=0
        while(arr[i]>0):
            dig=arr[i]%10
            rev=rev*10+dig
            arr[i]=arr[i]//10
        if(temp==rev):
            c+=1
    if c>0:
        print("True")
    else:
        print("False")
else:
    print("False")