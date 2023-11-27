try:
    print('Введите количество строк одним числом:')
    n = int(input())
    print('Введите количество столбцов одним числом:')
    m = int(input())
    matrix = []
    for i in range(n):
        print(f'Введите {m} элемента(ов) через пробел для строки {i + 1}:')
        row = list(map(int, input().split()))
        if len(row) != m:
            print('Количество введенных элементов не соответствует количеству столбцов ({m}).Программа выдаст неправильный результат, запустите программу заново ')
        else:
            matrix.append(row)
    for row in matrix:
        max_index = row.index(max(row))
        min_index = row.index(min(row))
        row[max_index], row[0] = row[0], row[max_index]
        if min_index == 0:
            min_index = max_index
        row[min_index], row[-1] = row[-1], row[min_index]
    print('Измененная матрица:')
    for row in matrix:
        print(row)
except ValueError:
    print('Читайте внимательно условия ввода! Вводите в первых двух случаях  по одному числу, потом через пробел .')