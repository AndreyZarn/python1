print ('Введите четверть: ')
x = int(input())
if x < 1 or x > 4:
    print('Введите номер четверти')
elif x == 1:
    print('x > 0, y > 0')
elif x == 2:
    print('x < 0, y > 0')
elif x == 3:
    print('x < 0, y < 0')
elif x == 4:
    print('x > 0, y < 0')
