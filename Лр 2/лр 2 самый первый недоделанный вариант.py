print('Введите целое число')
n = input()
b = ''
try:
    n = int(n)
    while n>0:
        b = str(n % 2)+ b
        n = n // 2
    print(b)
except:
    print('Это не целое число')
