n = int(input())
arr = list(map(int, input().split()))

count5 = arr.count(5)
count0 = arr.count(0)

if count0 == 0:
    print(-1)
else:
    max_fives = (count5 // 9) * 9
    if max_fives == 0:
        print(0)
    else:
        print('5' * max_fives + '0' * count0)