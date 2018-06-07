import numpy as np
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(input().split())
a=np.array(l,int)
arr=np.min(a,axis=1)
print(np.max(arr))



