t=int(input())
cf="codeforces"
for i in range(t):
    s=input()
    n=len(s)
    if s in cf and n==1 and s.islower():
            print("YES")
    else:
        print("NO")