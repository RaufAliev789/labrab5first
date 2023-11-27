try:
    import Cl
    print('Введите первый список, отсортированный по убыванию')
    a = list(map(int, input().split()))
    if any(a[i] < a[i + 1] for i in range(len(a) - 1)):
        print('Программа выдаст неправильный ответ. Введите числа по убыванию')
    else:
        print('Введите второй список, отсортированный по убыванию')
        b = list(map(int, input().split()))
        if any(b[i] < b[i + 1] for i in range(len(b) - 1)):
            print('Программа выдаст неправильный ответ. Введите числа по убыванию')
        else:
            print("Отсортированный массив после слияния:")
            print(Cl.SL(a, b))
except ValueError:
    print('Введите числа без лишних знаков, просто через один пробел')