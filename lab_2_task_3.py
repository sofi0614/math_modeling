a = int(input('Введите год:'))
if a % 4 == 0 or a % 100 == 0 and a % 400 == 0:
    print('a - высокосный')
else:
    print('a - невысокосный')