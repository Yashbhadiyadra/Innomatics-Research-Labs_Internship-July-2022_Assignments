
n = int(input("Enter the number of student records: "))
student_marks = {}
for i in range(n):
    name, *line = input("Enter the name and marks by giving spaces in between: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter the name you wants the average marks of: ")
total_marks = sum(student_marks[query_name])
average_marks = total_marks/3 
print("%.2f"%(average_marks))