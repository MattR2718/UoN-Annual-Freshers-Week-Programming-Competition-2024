n = int(input())
animals = []
for i in range(0,n):
    cur = input()
    if cur == "Z":
        animals.append("1")
    else:
        animals.append("0")

ani = "".join(animals)

d_ans = int(ani, 2)

ans = (2**n - 1)

print(ans - d_ans)