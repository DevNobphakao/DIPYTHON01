print("----------------------------------")
print("โปรแกรมแสดงข้อความต้อนรับนักศึกษา")
print("----------------------------------")
name = input("กรอกชื่อ: ")
year = int(input("กรอกชั้นปี: "))
if year == 1:
    print("Welcome Freshman", name)
elif year == 3:
    print("Welcome Junior", name)
elif year == 4:
    print("Welcome Senior", name)
else:
    print("Oh, no ....", name)
print("----------------------------------")
