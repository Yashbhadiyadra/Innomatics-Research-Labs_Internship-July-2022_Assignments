import re
for i in range(int(input())):
    a = input()
    if re.search(r'([789]\d{9}?)',a) and len(a) == 10:
        print ('YES')
    else:
        print('NO')