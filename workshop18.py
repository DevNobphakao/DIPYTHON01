print('=================================')
print('Product Price Calculator')
print('=================================')
pro_id = input('Enter id product :')
pro_name = input('Enter name product :')
pro_type = input('Enter type product :')
pro_price = float(input('Enter price product :'))
print('=================================')
if pro_type == 'F'or pro_type == 'f' :
    pro_price_net = pro_price - (pro_price * 2 / 100)
    print(f'price product {pro_name} on {pro_price_net:,.2f} bath')
elif pro_type == 'W' or pro_type == 'w'  :
    pro_price_net = pro_price - (pro_price * 4 / 100)
    print(f'price product {pro_name} on {pro_price_net:,.2f} bath')
elif pro_type == 'M' or pro_type == 'm'  :
    pro_price_net = pro_price - (pro_price * 4 / 100)
    print(f'price product {pro_name} on {pro_price_net:,.2f} bath')
elif pro_type == 'K' or pro_type == 'k' :
    pro_price_net = pro_price - (pro_price * 4 / 100)
    print(f'price product {pro_name} on {pro_price_net:,.2f} bath')
else :
    print('Error')

print('=================================')