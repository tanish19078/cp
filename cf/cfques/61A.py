a = input().strip()
b = input().strip()

result = []
for i in range(len(a)):
    if a[i] != b[i]:
        result.append('1')
    else:
        result.append('0')

print(''.join(result))