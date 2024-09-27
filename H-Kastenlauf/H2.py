import math
from collections import deque

num_t = int(input())

def print_all(house, store, pub):
    print("HOUSE POS: ", house[0], ", ", house[1])

    for i, p in enumerate(store):
        print("PUB ", i, ": ", p[0], ", ", p[1])

    print("PUB POS: ", pub[0], ", ", pub[1])

for turn_number in range(num_t):
    num_stores = int(input())
    
    # House
    house_pos = input().split()
    house_pos = (int(house_pos[0]) + 100000, int(house_pos[0]) + 100000)

    # Stores
    stores = []
    for store_num in range(num_stores):
        stores_str = input().split(" ")
        stores.append((int(stores_str[0]) + 100000, int(stores_str[1]) + 100000))
        
    # Pub
    pub_pos = input().split()
    pub_pos = (int(pub_pos[0]) + 100000, int(pub_pos[1]) + 100000)

    #print_all(house_pos, stores, pub_pos)

    # Create adjacency list
    adj = {}

    # House to stores
    adj["H"] = []
    for i, store_adj in enumerate(stores):
        dist = abs(house_pos[0] - store_adj[0]) / 50 + abs(house_pos[1] - store_adj[1]) / 50
        if(dist <= 20):
            adj["H"].append((str(i), dist))
    # House to end
    dist = abs(house_pos[0] - pub_pos[0]) / 50 + abs(house_pos[1] - pub_pos[1]) / 50
    if dist <= 20:
        adj["H"].append(("P", dist))

    # Stores to stores
    for i, store_adj1 in enumerate(stores):
        adj[str(i)] = []
        for j, store_adj2 in enumerate(stores):
            dist = abs(store_adj1[0] - store_adj2[0]) / 50 + abs(store_adj1[1] - store_adj2[1]) / 50
            if dist <= 20:
                adj[str(i)].append((str(j), dist))

    # Stores to Pub
    for i, store_adj in enumerate(stores):
        dist = abs(pub_pos[0] - store_adj[0]) / 50 + abs(pub_pos[1] - store_adj[1]) / 50
        if(dist <= 20):
            adj[str(i)].append(("P", dist))

    adj["P"] = []

    #print(adj)

    # depth first
    q = deque()
    visited = []
    q.append("H")

    while len(q):
        curr = q.pop()
        visited.append(curr[0])
        #print("VISITED: ", visited)
        for k in adj[curr[0]]:
            #print(k)
            if not k[0] in visited:
                q.append(k[0])

    #print("VISITED: ", visited)

    if "P" in visited:
        print("happy")
    else:
        print("sad")
