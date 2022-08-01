
n,m = list(map(int,input().split()))
happiness = 0
arr = list()
A,B = set(),set()

arr = list(map(int,input().strip().split()))
A = set(map(int,input().strip().split()))
B = set(map(int,input().strip().split()))

for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)
