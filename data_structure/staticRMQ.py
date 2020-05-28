# staticRMQ = "static range minimum query'

class RMQ:
    def __init__(self, arr):
        self.n = n = len(arr)
        self.double = d = [list(arr)]
        ii = 1
        while ii < n:
            row = d[-1].copy()
            for j in range(n - ii):
                row[j] = min(row[j], row[j + ii])
            d.append(row)
            ii <<= 1

    def get(self, l, r):
        """ min value of [l, r) """
        k = r - l
        i = 0
        j = l
        d = self.double
        result = float('inf')
        while k:
            if k & 1:
                result = min(result, d[i][j])
                j += 1 << i
            i += 1
            k >>= 1
        return result


n, q = map(int, input().split())
l = list(map(int, input().split()))
dbl = RMQ(l)
for _ in range(q):
    l,r = map(int, input().split())
    print(dbl.get(l,r))

