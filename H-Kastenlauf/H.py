import math
from collections import deque

num_t = int(input())

class Input:
    jHome = (0, 0)
    stores = []
    pub = (0, 0)

    nodes = {}

    def __init__(self):
        #self.jHome = a
        #self.stores = b
        #self.pub = c

        num_r = int(input())
        jhstr = input().split(" ")
        jh = (int(math.ceil(int(jhstr[0]) / 50)), int(math.ceil(int(jhstr[1]) / 50)))
        strs = []
        for r in range(num_r):
            txt = input().split(" ")
            pos = (int(math.ceil(int(txt[0]) / 50)), int(math.ceil(int(txt[1]) / 50)))
            strs.append(pos)
        pstr = input().split(" ")
        ps = (int(math.ceil(int(pstr[0]) / 50)), int(math.ceil(int(pstr[1]) / 50)))

        self.jHome = jh
        self.stores = strs
        self.pub = ps

        self.nodes["H"] = jh
        self.nodes["P"] = ps
        for i in range(len(self.stores)):
            self.nodes[str(i)] = self.stores[i]
        

    def print(self):
        #print("HOME AT: ", self.jHome[0], " ", self.jHome[1])
        #print("STORES AT: ")
        #for str in self.stores:
        #    print(str[0], " ", str[1])
        #print("PUB AT: ", self.pub[0], " ", self.pub[1])

        print(self.nodes)

    def solve(self):
        # Create graph
        # From: [to]
        adj = {}
        for key, value in self.nodes.items():
            adj[key] = []
            for key2, value2 in self.nodes.items():
                if(key != key2):
                    #print()
                    #print(key, " ", key2)
                    #print(self.nodes[key], "    ", self.nodes[key2])
                    
                    dist = abs(self.nodes[key][0] - self.nodes[key2][0]) + abs(self.nodes[key][1] - self.nodes[key2][1])

                    #print(dist)
                    if(dist <= 20):
                        adj[key].append(key2)
        #print("ADJ: ", adj)


        # depth first
        q = deque()
        visited = []
        q.append("H")

        while len(q):
            curr = q.pop()
            visited.append(curr)
            for k in adj[curr]:
                if not k in visited:
                    q.append(k)

        #print(visited)

        if "P" in visited:
            return "happy"
        else:
            return "sad"
        return


tests = []

for i in range(num_t):
    ip = Input()
    tests.append(ip.solve())   

for t in tests:
    print(t)
