print('----------------------------------------')
print(' โปรแกรมคำนวณผลคูณ ')
print('----------------------------------------')

def get_input():
    """รับตัวเลขจำนวนเต็ม 2 จำนวนจากผู้ใช้"""
    a = int(input("ป้อนตัวเลขที่ 1: "))
    b = int(input("ป้อนตัวเลขที่ 2: "))
    return a, b

def multiply(a, b):
    """คำนวณผลคูณของตัวเลข 2 จำนวน"""
    return a * b

def display_result(a, b, result):
    """แสดงผลลัพธ์ของการคูณ"""
    print(f"{a} x {b} = {result}")

def is_over_limit(result, limit=5000):
    """ตรวจสอบว่าผลคูณมากกว่า limit หรือไม่"""
    return result > limit

def main():
    """ฟังก์ชันหลักของโปรแกรม"""
    while True:
        a, b = get_input()
        result = multiply(a, b)
        display_result(a, b, result)
        if is_over_limit(result):
            print("ผลคูณมากกว่า 5000 โปรแกรมหยุดทำงาน")
            break

if __name__ == "__main__":
    main()