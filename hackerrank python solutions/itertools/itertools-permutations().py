from itertools import permutations
arr=input().split()
s=arr[0]
n=int(arr[1])
l=sorted(list(permutations(s,n)))
r=''
for i in range(len(l)):
    for j in range(n):
        print(l[i][j],end="")
    print()
    
    