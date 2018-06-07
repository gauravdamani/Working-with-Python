arr=input().split()
n=int(arr[0])
x=int(arr[1])
a=[]
for i in range(x):
    a+=[map(float,input().split())]
for i in zip(*a):
    print(sum(i)/x)
    