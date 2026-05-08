x=input()
y=input()
a,b=0,0
for i in range(len(x)):
    if x[i]==y[i]:
        a+=1
    elif x[i] in y:
        b+=1
print(a,b)
