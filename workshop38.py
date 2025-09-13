print('..................')
print("โปรแกรมค้นหาสายรถเมล์")
print('..................')

def input_bus_line():   
    return input("กรุณาป้อนสายรถเมล์: ")

def get_bus_info(line):
    info = {
        "57": "สาย 57 ไปปิ่นเกล้า บางขุนนนท์",
        "3": "สาย 3 ไปสนามหลวง ลาดพร้าว",
        "71": "สาย 71ไปหัวลำโพง เยาวราช",
        "56": "สาย 56 ไปบางลำพู สะพานกรุงธน",
        "539": "สาย 539 ไปอนุสวรีย์ชัย สามเสน"
    }
    return info.get(line, "ยังไม่มีข้อมูลสายรถเมล์ที่สอบถาม")

def show_result(message):
    print(message)


bus_line = input_bus_line()
result = get_bus_info(bus_line)
show_result(result)