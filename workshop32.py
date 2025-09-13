# parameter คือ ตัวแปรประเภทหนึ่ง ที่เขียนอยู่ในวงเล็บหลังชื่อฟังก์ชัน และจะใช้ได้เฉพาะในฟังก์ชันนั้นๆ เท่านั้น
 
# return คือ คำสั่ง ที่ใช้ส่งค่าข้อมูลใดๆ กลับไปยังจุดที่เรียกใช้ฟังก์ชัน/คำสั่ง retrun ยังเป็นการบอกว่าฟังก์ชันนั้นๆ ทำงานจบแล้ว
 
#no parameter no return

'''
def  func_name( ) :
    คำสั่ง
    คำสั่ง
    .......
'''
def func_a( ) :
    print('Hello...')
    print('Hi...')
 
def func_b( ) :
    print('Wow wow wow')
 
print('Bye bye....')
func_a( )  #call function
func_a( )
func_a( )
func_b( )
func_a( )