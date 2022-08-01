
n = int(input())
s = set(map(int,input().split()))
num = int(input())
for i in range(num):
    opt = input().split()
    if opt[0]=="remove":
        s.remove(int(opt[1]))
    elif opt[0]=="discard":
        s.discard(int(opt[1]))
    else :
        s.pop()
print(sum(list(s)))