print ('Введите x: ')
x = int(input())
print ('Введите y: ')
y = int(input())
print()
if x==0 or y==0:
    print('Не должны быть равны нулю')
elif x>0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
elif x>0 and y<0:
    print('4')