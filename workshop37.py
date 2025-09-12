print('..................')
print("โปรแกรมคำนวณอายุ")
print('..................')
def input_name():
    return input("กรุณาป้อนชื่อ: ")

def input_year():
    return int(input("กรุณาป้อนปีเกิด (พ.ศ.): "))

def calculate_age(year):
    current_year = 2568  
    return current_year - year

def show_result(age):
    if age >= 55:
        print("คุณแก่แล้ว...")
    else:
        print("คุณยังไม่แก่...")


name = input_name()
year = input_year()
age = calculate_age(year)
show_result(age)