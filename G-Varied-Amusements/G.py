from functools import cache
ln = input().split(" ")
n = int(ln[0])
a = int(ln[1])
b = int(ln[2])
c = int(ln[3])

@cache
def rec(n, a, b, c, lastChoice, depth):
    if depth == n:
        return 1
    if lastChoice == "a":
        return b * rec(n, a, b, c, "b", depth + 1) + c * rec(n, a, b, c, "c", depth + 1)
    if lastChoice == "b":
        return a * rec(n, a, b, c, "a", depth + 1) + c * rec(n, a, b, c, "c", depth + 1)
    if lastChoice == "c":
        return b * rec(n, a, b, c, "b", depth + 1) + a * rec(n, a, b, c, "a", depth + 1)
    else:
        return a * rec(n, a, b, c, "a", depth + 1) + b * rec(n, a, b, c, "b", depth + 1) + c * rec(n, a, b, c, "c", depth + 1)
    
print(rec(n, a, b, c, "", 0) % (1000000007))