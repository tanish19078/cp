s=input()
x="hello"
i=0
for ch in s:
    if i < 5 and ch == x[i]:
        i += 1
if i == 5:
    print("YES")
else:
    print("NO")
    
