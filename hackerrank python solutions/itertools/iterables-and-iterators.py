from itertools import combinations
n=int(input())
arr=input().split()
l=list((arr))
l2=list(range(1,n+1))
k=int(input())
l1=list(combinations(l2,k))
c=0
for i in range(len(l1)):
    for j in range(k):
        if(l[l1[i][j]-1])=='a':
            c+=1
            break
    else:
        continue
    
print(c/len(l1))