from itertools import product
arr=map(int,input().split())
l=sorted(list(set(arr)))
ar=map(int,input().split())
p=sorted(list(set(ar)))
t=list(product(l,p))
for i in range(len(t)):
    print(t[i],end=" ")
