print("----------------------------------")
print("โปรแกรมคำนวณค่าคอมมิชชั่น")
print("----------------------------------")
emp_id = input("กรอกรหัสพนักงาน: ")
emp_name = input("กรอกชื่อพนักงาน: ")
sales = float(input("กรอกยอดขาย (บาท): "))
if sales <= 1000:
    commission = 0.0
elif sales <= 2000:
    commission = sales * 0.01
elif sales <= 3000:
    commission = sales * 0.03
else:
    commission = sales * 0.05
print("\nรหัสพนักงาน:", emp_id)
print("ชื่อพนักงาน:", emp_name)
print("ยอดขาย: {:.2f} บาท".format(sales))
print("ค่าคอมมิชชั่น: {:.2f} บาท".format(commission))