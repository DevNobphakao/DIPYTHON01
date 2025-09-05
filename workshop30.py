from random import randint

print('..................')
print('เกมส์ทายตัวเลขที่มีค่าอยู่ที่ 1 - 100 กันเถอะ')
print('..................')
num_rand = randint(1, 100)
num_user = 0
while num_user != num_rand:
    num_user = int(input('ป้อนตัวเลขที่ท่านคิดว่าใช่ : '))
    if num_user < num_rand:
        print('ตัวเลขที่ท่านป้อนน้อยเกินไป')
    elif num_user > num_rand:
        print('ตัวเลขที่ท่านป้อนมากเกินไป')
    else:
        print('เยี่ยมมาก ทายถูกต้องแล้ว')

print('..................')
print('ขอบคุณที่เล่นเกมส์กับเรา')
print('..................')