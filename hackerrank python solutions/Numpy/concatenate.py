import numpy as np
n,m,p=map(int,input().split())
l=[]
r=[]
for i in range(n):
    l.append(input().split())
a=np.array(l,int)
for i in range(m):
    r.append(input().split())
ar=np.array(r,int)
print(np.concatenate((a,ar),axis=0))




