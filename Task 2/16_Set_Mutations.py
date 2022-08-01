
A = int(input())
Aset = set(map(int, input().split()))
N = int(input())
for i in range(N):
    ip = input().split()
    if ip[0] == 'intersection_update':
        Bset = set(map(int, input().split()))
        Aset.intersection_update(Bset)
    elif ip[0] == 'update':
        Bset = set(map(int, input().split()))
        Aset.update(Bset)
    elif ip[0] == 'symmetric_difference_update':
        Bset = set(map(int, input().split()))
        Aset.symmetric_difference_update(Bset)
    elif ip[0] == 'difference_update':
        Bset = set(map(int, input().split()))
        Aset.difference_update(Bset)
    else:
        print("Enter a valid operation")
print(sum(Aset))