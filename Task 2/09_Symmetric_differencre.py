
M = int(input())
m = set(map(int, input().split()))
N = int(input())
n = set(map(int, input().split()))
mdeff = m.difference(n)
ndeff = n.difference(m)
f_out = mdeff.union(ndeff)
for i in sorted(list(f_out)):
    print(i)