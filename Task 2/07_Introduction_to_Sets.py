
def average(array):
    res = sum(set(array))/len(set(array))
    return res

if __name__ == '__main__':
    n = int(input("Enter the number of plants: "))
    arr = list(map(int, input("Enter the heigts of the plant(space-separeted): ").split()))
    result = average(arr)
    print(result)