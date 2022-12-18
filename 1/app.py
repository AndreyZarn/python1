print ('Введите число: ')
a = int(input())
if a<=0 or a>8:
    print('За диапазоном')
else:
    if a == 6 or a == 7:
        print('Да')
    else:
        print('Нет')