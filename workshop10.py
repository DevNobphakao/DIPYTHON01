print('================================')
print(' Promgra Money share V. 1.0.1 ')
print('================================')
amount = float(input('Please enter the amount (baht):'))
num_people = int(input('Please specify the num_ people'))
print('================================')
each_ceil = (amount / num_people)
paid_total = each_ceil * num_people
change = paid_total - amount
print('================================')
print(f'each {each_ceil:,} baht (collected) {paid_total:,.2f} baht')
print(f'Total change {change} baht - each {change / num_people:,.2f} baht')
print('================================')
