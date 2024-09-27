ln1 = input().split(" ")
N = int(ln1[0])
K = int(ln1[1])

ass = []

for i in range(N):
    ln = input().split(" ")
    ass.append((i, int(ln[0]), int(ln[1])))

for a in ass:
    print(a)

# Find equals
# ai + K < aj but bi + K >= bj
# ai + K >= aj but bi + K < bj
equals = []
for i in range(N):
    for j in range(i, N):
        if(i == j):
            continue
        if (ass[i][1] + K < ass[j][1] and ass[i][2] + K >= ass[j][2]) or (ass[i][1] + K >= ass[j][1] and ass[i][2] + K < ass[j][2]):
            equals.append((i, j))
        elif ass[i][1] == ass[j][1] and ass[i][2] == ass[j][2]:
            equals.append((i, j))

print("EQUALS")
print(equals)

#ranks = [{equals[0][0], equals[0][1]}]
groups_of_equals = []
for eq in equals:
    added = False
    for r in groups_of_equals:
        if eq[0] in r or eq[1] in r:
            added = True
            r.add(eq[0])
            r.add(eq[1])
    if not added:
        groups_of_equals.append({eq[0], eq[1]})
        

print("groups_of_equals")
print(groups_of_equals)


# better
# (worse, better)
better = []
for i in range(N):
    for j in range(i, N):
        if(i == j):
            continue
        if (ass[i][1] + K < ass[j][1] or ass[i][2] + K < ass[j][2] or (ass[i][1] + K >= ass[j][1] and ass[i][2] + K >= ass[j][2]) and not((i, j) in equals) and not((j, i) in equals)):
            better.append((i, j))

print("BETTER")
print(better)

# better than n
better_than_n = []
for i in range(N):
    better_than_n.append([])
    for bet in better:
        if bet[0] == i:
            better_than_n[i].append(bet[1])

print("BETTER THAN N")
print(better_than_n)

s = set()
for bett in better_than_n:
    if len(bett):
        s.add("".join(map(str, bett)))
print(len(s) + 1 + len(groups_of_equals))