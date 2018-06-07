n=int(input())
arr = map(int, input().split())
s=set(arr)
m=int(input())
ar = map(int, input().split())
r=set(ar)
p=s&r
print(len(p))