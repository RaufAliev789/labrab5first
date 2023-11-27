def SL(a, b, reverse):
    c = []
    N = len(a)
    M = len(b)
    i = 0
    j = 0
    while i < N and j < M:
        if (reverse and a[i] <= b[j]) or (not reverse and a[i] >= b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c
