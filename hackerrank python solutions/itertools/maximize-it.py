from itertools import product
import functools
arr=input().split()
k=int(arr[0])
m=int(arr[1])
s=0
l=[]
for i in range(k):
    x=(input().split())
    b=list(map(int,x))
    l.append(b[1:])
t=(list(product(*l)))
n=[]
for i in range(len(t)):
    n.append(sum(list(map(lambda x:x**2,t[i])))%m)
print(int(max(n)))
    