def func(a, b):
    return a+b
class SegmentTree:
    def __init__(self, ls):
        self.n = len(ls)
        self.tree = [0]*self.n + ls
        for i in range(1, self.n)[::-1]:
            self.tree[i] = func(self.tree[i<<1|0], self.tree[i<<1|1])
    
    def get(self, l, r):
        lret = 0
        rret = 0
        l += self.n
        r += self.n
        while l < r:
            if l&1:
                lret = func(self.tree[l], lret)
                l+= 1
            if r&1:
                rret = func(self.tree[r-1], rret)
            l >>= 1
            r >>= 1
        return func(lret, rret)
    
    def update(self, i, x):
        i += self.n
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = func(self.tree[i<<1|0], self.tree[i<<1|1])
        
# n, q = map(int, input().split())
# l = list(map(int, input().split()))
# T = SegmentTree(l)
# ans = []
# for _ in range(q):
#     a, b, c = map(int, input().split())
#     if a == 1:
#         ans.append(T.get(b, c))
#     else:
#         x = T.get(b, b+1)
#         T.update(b, c+x)
# for i in ans:
#     print(i)




