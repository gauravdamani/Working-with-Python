arr=input().split()
x=(arr[0])
k=int(arr[1])
p=input()
p=p.replace('x',x)
t=(eval(p))
if(t==k):
    print("True")
else:
    print("False")