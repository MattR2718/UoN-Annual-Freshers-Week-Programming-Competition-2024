n = int(input())

words = []
for i in range(n):
    words.append(input())

words.sort()

shortest = words[0]

vals = [0]

starti = 0
while starti < len(shortest):
    giveup = False
    for j in range(1, len(shortest) - starti + 1):
        currTest = shortest[starti:starti+j]
        for word in words:
            if not currTest in word:
                giveup = True
                break
        if giveup:
            break
        else:
            vals.append(j)
    starti += 1


print(max(vals))