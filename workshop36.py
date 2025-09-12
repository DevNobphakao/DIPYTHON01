def sen_pa() :
    print('-------------------------------')
    

def show_program_name( ):
    print('-------------------------------')
    print(' ตรวจสอบควันคำ ')
    print('-------------------------------')


def input_car_info( ) :
    car_owner = input('Enter name use cat :')
    car_number = input('Enter vehicle ragistration :')
    car_carbon = float(input('Enter carbon gas volume :'))
    return car_owner, car_number, car_carbon

def show_result(car_owner, car_number, car_carbon, result):
    print(f'คุณ {car_owner} รถทะเบียน {car_number}')
    print(f'ปริมาณควันคำ {car_carbon} สรุป: {result}')

def check_carbon(car_owner, car_number, car_carbon):
    if car_carbon > 678.55:
        show_result(car_owner, car_number, car_carbon, 'ไม่ผ่านเกณฑ์')
    else:
        show_result(car_owner, car_number, car_carbon, 'ผ่านเกณฑ์')


show_program_name( )
car_owner, car_number, car_carbon = input_car_info( )
sen_pa()
check_carbon(car_owner, car_number, car_carbon)
sen_pa()


