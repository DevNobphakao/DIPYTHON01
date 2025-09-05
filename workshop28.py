from datetime import datetime   

print('..................')
print(' โปรแกรมคำนวนอายุพนักงานโรงงาน ')
print('..................')

while True :
    emp_name = input(' ชื่อพนักงาน : ')
    if emp_name.upper() == 'SAU' :
        break
    emp_year = int(input(' ปีเกิดพนักงาน : '))
    emp_age = (datetime.now().year) - emp_year
    print(f' พนักงาน {emp_name} มีอายุ {emp_age} ปี ')
    print('..................')

print('..................')
print('ขอบคุณที่ใช้บริการ')
print('..................')