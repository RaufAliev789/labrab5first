print('Введите целое число')
n = input()
b= ''
try:
    ## Проверка на целое число
    n = int(n)
    if n < 0:

        n = n*(-1)

        ## Перевод в двоичную систему
        while n > 0:
            b = str(n % 2) + b
            n = n // 2

        ## Добавляем нули
        mn = 8 - len(b) % 8
        for i in range(mn):
            b = '0' + b

        ## Инвертирование 1 и 0
        b = b.replace('1', '2').replace('0', '1').replace('2', '0')

        ## Перевод из двоичной системы в десятичную и добавление 1
        tn = int(b, 2)
        tn += 1

        ## Перевод из десятичной системы обратно в двоичную
        b = ''
        while (tn > 0):
            b = str(tn % 2) + b
            tn = tn // 2

    else:

        while n > 0:
            b = str(n % 2) + b
            n = n // 2

    ## Вывод результата
    print(b)

except:
    print('Это не целое число')