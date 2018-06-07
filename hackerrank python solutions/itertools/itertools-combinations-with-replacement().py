from itertools import combinations_with_replacement
arr=input().split()
s=sorted(arr[0])
n=int(arr[1])
l=sorted(list(combinations_with_replacement(s,n)))
for i in range(len(l)):
    for j in range(n):
        print(l[i][j],end="")
    print()
    
    