w = int(input('Weight: '))
unit = input('(L)bs or (K)gs: ')

if unit.upper() == 'K':
    converted = 0.45 * w
    print(f'You are {converted} pounds')
else:
    converted = w / 0.45
    print(f'You are {converted} kgs')


