n=input()
m=input()
x=m[0]
c=0
for i in range(len(n)):
    if(n[i]==x and n[i:i+len(m)]==m):
        print("({}, {})".format(i,i+len(m)-1))
        c+=1
if(c==0):
    print("(-1, -1)")