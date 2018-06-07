
def fun(s):
    s1=s[0:s.find('@')]
    s2=s[s.find("@")+1:s.find(".")]
    s3=s[s.find(".")+1:]
    if(s.find('@')>0 and s.find('.')>0 and len(s1)>0):
        c=0
        for i in s1:
            if i.isalnum() or i=='-' or i=='_':
                c+=1
        if c==len(s1):
            if s2.isalnum() and len(s3)<=3:
                return(True)

            