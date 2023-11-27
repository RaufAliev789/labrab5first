try:
    print('Введите первый список')
    a = list(map(int, input().split()))
    print('Введите второй список')
    b = list(map(int, input().split()))
    import MASSIV
    print(MASSIV.m_dv_dl(a, b))
except ValueError:
    print('Введите числа без лишник знаков, просто через 1 пробел')