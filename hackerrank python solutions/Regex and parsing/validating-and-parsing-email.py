n=int(input())
for i in range(n):
    s=input()
    if '@' in s and '.' in s:
        s1=s[0:s.index('<')]
        s2=s[s.index('<')+1:s.index('@')]
        s3=s[s.index('@')+1:s.index('.',s.index('@'))]
        s4=s[s.index('.',s.index('@'))+1:s.index('>')]
        c=0
        for i in range(len(s2)):
            if s2[i].isalpha() or s2[i]=='-' or s2[i]=='_' or s2[i]=='.' or s2[i].isdigit():
                c+=1
        if c==len(s2) and s3.isalpha() and s4.isalpha() and 1<=len(s4)<=3 and not(s2[0]=='_' or s2[0]=='-' or s2[0]=='.'):
            print(s)
    