n = int(input())
faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

total = 0
for _ in range(n):
    poly = input().strip()
    total += faces[poly]

print(total)