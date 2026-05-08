s = input()
vowels = set("AOYEUIaoyeui")
result = []

for ch in s:
    if ch in vowels:
        continue
    result.append(".")
    result.append(ch.lower())

print("".join(result))
