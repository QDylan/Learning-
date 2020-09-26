# -*- coding: utf-8 -*-


# while True:
#     try:
#     except:
#         break
# for line in sys.stdin:
#     strs = line.split()
#
# n = int(sys.stdin.readline().strip())
# for i in range(n):
#     line = sys.stdin.readline().strip()

# sys.setrecursionlimit(500*500)
#
#
import sys

if __name__ == '__main__':
    n, p = map(int, input().split())
    items = []
    for i in range(n):
        items.append(list(map(int, input().split())))


    class solu:
        def res(self, p, items):
            self.res = 0

            def dfs(cur, i, rest):
                if i == n or rest < items[i][1]:
                    self.res = max(self.res, cur)
                    return
                for j in range(items[i][0] + 1):
                    if j * items[i][1] > rest: break
                    dfs(cur + j * items[i][2], i + 1, rest - j * items[i][1])

            dfs(0, 0, p)
            return self.res


    items.sort(key=lambda x: x[1])
    s = solu()
    print(s.res(p, items))
