#have parameters have returns

'''
def  func_name(param, param, ..... ) :
    คำสั่ง
    คำสั่ง
    .......
    return ค่าที่ต้องการส่งกลับ
'''
 
def sum_number(n1, n2, n3) :
    total = n1 + n2 + n3
    return total
 
def welcome(name) :
    message = 'Hello ' + name
    return message
 
print(sum_number(1, 2, 3))
print(welcome('Pong'))
print(sum_number(10, 20, 30))
data = welcome('Mod')
print(data)