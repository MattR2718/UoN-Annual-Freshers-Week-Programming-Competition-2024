import math
inp = input().split(" ")
n = int(inp[0])
k = int(inp[1])

found = math.log(n, 2)


if(found <= k):
    print("Your wish is granted!")
else:
    print("You will become a flying monkey!")