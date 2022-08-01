

k = int(input())
rooms = list(map(int, input().split()))
a = set()
b = set()
for rm in rooms:
    if rm not in a:
        a.add(rm)
        b.add(rm)
    else:
        b.discard(rm)
print(list(b)[0])