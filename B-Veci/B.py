import itertools

num = input()

digits = list(num)
digits.sort()

h = {}
for d in digits:
    h[d] = 1

sum = 0
for d in h:
    sum += 1

#print(h)
if sum == 2 and '0' in h:
    print(0)
    quit()


perm = list(itertools.permutations(digits))

valid = []
for p in perm:
    #print(list(p))
    if int(''.join(list(p))) > int(num):
        valid.append(int(''.join(list(p))))

if len(valid) == 0:
    print(0)
else:
    print(min(valid))