n = int(input())

m = []

for i in range(n):
    m.append(input())

#print(m)

houses = []
for r in range(len(m)):
    for c in range(len(m[r])):
        if m[r][c] == 'H':
            houses.append((r, c))

dists = []
for r in range(len(m)):
    for c in range(len(m[r])):
        if m[r][c] == 'S':

            ds = []
            for h in houses:
                ds.append(abs(h[0] - r) + abs(h[1] - c))
            dists.append(min(ds))
            
print(max(dists))