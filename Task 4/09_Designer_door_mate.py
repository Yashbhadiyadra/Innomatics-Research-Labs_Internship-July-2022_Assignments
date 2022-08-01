N, M = map(int, input().split())
d = ".|."
for i in range(N//2):
    print((d*i).rjust(M//2-1,'-') + d + (d*i).ljust(M//2-1,'-'))
print("WELCOME".center(M,'-'))
for j in range(N//2+2,N+1):
    print((d*(N-j)).rjust(M//2-1,'-') + d + (d*(N-j)).ljust(M//2-1,'-'))