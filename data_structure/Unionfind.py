class Uninonfind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    def check(self, x, y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False
    def find(self, x):
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

if __name__ == '__main__':
    n,q = map(int, input().split())
    uf = Uninonfind(n)

    for _ in range(q):
        t, u, v = map(int, input().split())
        if t == 0:
            uf.union(u, v)
        else:
            print(1 if uf.check(u,v) else 0 )