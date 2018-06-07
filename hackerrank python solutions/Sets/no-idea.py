lst=list(map(int,input().split()))
lst1=list(map(int,input().split()))
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
s=0
for i in range(len(lst1)):
    if lst1[i] in s1:
        s+=1
    elif lst1[i] in s2:
        s-=1
print(s)
        