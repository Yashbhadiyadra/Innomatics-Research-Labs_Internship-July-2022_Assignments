

n = int(input("Enter the number of integers: "))
arr = list(set(map(int, input("Enter the "+str(n)+" integers values following by spaces: ").split())))
arr.sort()
print(arr[-2])