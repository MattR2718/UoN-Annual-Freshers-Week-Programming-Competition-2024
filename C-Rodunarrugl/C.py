n = int(input())
locations = input().split(" ")

for i, l in enumerate(locations):
    locations[i] = int(l)

#print(locations)

at_want = {}

for i, v in enumerate(locations):
    #at_want.append((i + 1, v))
    at_want[i + 1] = v

#print(at_want)

groups = [[]]

#print(at_want.items())

done = []
for i in range(1, n + 1):
    g = []

    if at_want[i] == i:
        done.append(i)
        continue

    if not i in done:
        n = i
        while not n in done:
            g.append(at_want[n])
            done.append(n)
            n = at_want[n]
        groups.append(g)            

#print(groups)

ans = 0
for g in groups:
    ans += len(g)

ans += len(groups) - 1
print(ans)