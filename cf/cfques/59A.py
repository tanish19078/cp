s=input()
cntl=sum((1 for c in s if c.islower()))
cntu=sum((1 for c in s if c.isupper()))
if cntl>=cntu:
    print(s.lower())
else:
    print(s.upper())