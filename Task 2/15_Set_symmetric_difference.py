

n = int(input("Enter the number of student who have subscribed for the English Newspaper: "))
nr = set(map(int, input("Enter the Roll numbers of those students(space-separeted): ").split()))
b = int(input("Enter the number of student who have subscribed for the French Newspaper: "))
br = set(map(int, input("Enter the roll numbers of those students(space-separeted): ").split()))
res = nr.symmetric_difference(br)
count = 0
for i in range(len(res)):
    count+=1
print("The total number of students who have subscribed either the English or the French newspaper but not both.: ",count)