n = int(input())
num = 1

cont_divisores = 0
while num <= n:
    if (n % num) == 0:
        cont_divisores += 1 
    num += 1

if cont_divisores == 2:
    print(True)
else:
    print(False)