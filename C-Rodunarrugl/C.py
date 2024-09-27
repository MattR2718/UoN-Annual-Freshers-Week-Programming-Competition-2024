n = int(input())
locations = input().split(" ")

for i, l in enumerate(locations):
    locations[i] = int(l)

print(locations)

at_want = {}

for i, v in enumerate(locations):
    #at_want.append((i + 1, v))
    at_want[i + 1] = v

print(at_want)

groups = [[]]

done = []
print(at_want.items())

for i in at_want.items():
    #done.append(i.)
    break

print(done)


for p in at_want:
    if p[0] != p[1]:
        for g in groups:
            if p[0] in g and not p[1] in g:
                g.append(p[1])
            #elif p[1] in g and not p[0] in g:
            #    g.append(p[0])
            elif not p[0] in g and not p[1] in g:
                g.append(p[1])
            #    g.append(p[0])
            

print(groups)