n = int(input())
scores = list(map(int, input().split()))

amazing = 0
max_score = scores[0]
min_score = scores[0]

for i in range(1, n):
    if scores[i] > max_score:
        amazing += 1
        max_score = scores[i]
    elif scores[i] < min_score:
        amazing += 1
        min_score = scores[i]

print(amazing)