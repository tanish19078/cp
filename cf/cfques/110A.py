n = input()
cnt = 0
for d in n:
    if d == '4' or d == '7':
        cnt += 1

if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")