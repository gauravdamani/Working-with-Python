n=int(input())
l=[]
for i in range(n):
    l+=input().split('\n')
s=set(l)
print(len(s))