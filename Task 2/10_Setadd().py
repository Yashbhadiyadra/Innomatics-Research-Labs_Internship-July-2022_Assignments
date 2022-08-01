

N = int(input("enter the total number of country: "))
s = set()
count = 0
print("Enter the country names: ")
for i in range(N):
    s.add(input())
print(len(s))