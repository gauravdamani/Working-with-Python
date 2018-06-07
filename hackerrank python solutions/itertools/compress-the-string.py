s=input()
c=0
if s.isdigit() and len(s)<=10000:
    for i in range(len(s)-1):
        if s[i+1]==s[i]:
            c+=1
        else:
            print("({}, {})".format(c+1,s[i]),end=" ")
            c=0
    if s.count(s[0])==len(s):
        print("({}, {})".format(len(s),s[0]))
    else:   
        if(s[-1]==s[-2]):
            print("({}, {})".format(2,s[-1]),end=" ")
        else:
            print("({}, {})".format(1,s[-1]))
        
    