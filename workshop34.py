# return คือ คำสั่ง ที่ใช้ส่งค่าข้อมูลใดๆ กลับไปยังจุดที่เรียกใช้ฟังก์ชัน/คำสั่ง retrun ยังเป็นการบอกว่าฟังก์ชันนั้นๆ ทำงานจบแล้ว
 
#no parameter have returns

'''
def  func_name( ) :
    คำสั่ง
    คำสั่ง
    .......
    return ค่าที่ต้องการส่งกลับ
'''
 
def func_e( ) :
    print('Hello...')
    return 'Hi...'
 
def func_f( ) :
    return 'Wow...', 'Woo...', 99999
 
print( func_e()  )
 
xx = func_e()
print(xx)
 
a, b, c = func_f()
print(a)
print(b)
print(c)