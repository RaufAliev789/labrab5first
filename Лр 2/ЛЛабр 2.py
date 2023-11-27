n = input('Введите целое число: ')
b= ''
neg = False
try:
    n = int(n)
except:
    print("Введено не целое число")
    exit()

if (n < 0):
    n= n *(-1)
    neg = True
while(n > 0):
    b = str(n % 2) + b
    n = n // 2
if neg:
    negfix = ''
    mnulls = 8 - len(b)%8
    for i in range(mnulls):
        b = "0" + b
    for i in range(len(b)):
        num = "0" if b[i] == "1" else "1"
        negfix += num
    temp_num = int(negfix, 2)
    temp_num += 1
    negfix = ''
    while (temp_num > 0):
        negfix = str(temp_num % 2) + negfix
        temp_num = temp_num // 2
    b = negfix
print(b)
