print('=================================')
print('Truck Weight Checker')
print('=================================')
truck_id = input("ป้อนทะเบียนรถบรรทุก: ")
truck_weight = float(input("ป้อนน้ำหนักรถบรรทุก (กิโลกรัม): "))
if truck_weight > 1000:
    print(f"รถทะเบียน {truck_id} น้ำหนักรถไม่ผ่านเกณฑ์")
else:
    print(f"รถทะเบียน {truck_id} น้ำหนักรถผ่านเกณฑ์")
print('=================================')
