print('..................')
print('โปรแกรมคำนวณผลคูณ')
print('..................')
while True:
    num1 = int(input('ป้อนตัวเลขที่ 1: '))
    num2 = int(input('ป้อนตัวเลขที่ 2: '))
    product = num1 * num2
    print(f'ผลคูณของ {num1} และ {num2} คือ {product}')
    if product > 5000:
        print('ผลคูณมากกว่า 5000 โปรแกรมหยุดทำงาน')
        break

print('..................')