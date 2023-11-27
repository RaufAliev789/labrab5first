summa = 0 #Вычислить сумму и число положительны
# элементов матрицы A[N, N], находящихся над главной диагональю.
count = 0
a = []
try:
    print('Введите размер матрицы')
    n = int(input())
    for i in range(n):
        b= []
        for j in range(n):
            print('Введите элемент a[i][j]: ')
            element = int(input())
            b.append(element)
        a.append(b)
    for i in range(n):
        for j in range(n):
            if i < j:
                summa = a[i][j] + summa
                if a[i][j] > 0:
                    count += 1
    print("Сумма положительных элементов над главной диагональю:", summa)
    print("Количество положительных элементов над главной диагональю:", count)
except ValueError:
    print('Введите одно число без пробелов')