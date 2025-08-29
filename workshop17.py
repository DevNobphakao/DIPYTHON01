from datetime import datetime

print('=================================')
print(' Promgra Calculate age')
print('=================================')
you_name =input('Entername :')
you_yearborn =int(input('Enterbrd :'))
print('=================================')

you_age = (datetime.now().year + 543) -you_yearborn

if you_age >=55 :
    print('you {} age {} year'. format(you_name,you_age))
    print('you sure')
else :
    print('you {} age {} year'. format(you_name,you_age))
    print('nc')

print('=================================')