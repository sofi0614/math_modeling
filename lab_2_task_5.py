first = int(input(' Первое число '))
second = int(input(' Второе число'))
if second == 0:
    print(' Нет решений ')
elif first / second:
    a = first % second
    b = first / second
    print('Первое число делится на второе!Остаток от деления-',a 'Частное чисел-',b)