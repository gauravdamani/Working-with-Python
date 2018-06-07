import numpy as np
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(input().split())
a=np.array(l,int)
arr=np.sum(a,axis=0)
s=1
for i in range(m):
    s*=arr[i]
print(s)



