from itertools import combinations
arr=input().split()
s=sorted(arr[0])
n=int(arr[1])
for k in range(1,n+1):
    l=sorted(list(combinations(s,k)))
    for i in range(len(l)):
        for j in range(k):
            print(l[i][j],end="")
        print()
    
    