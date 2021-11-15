def eh_primo(n):
    num = 1
    cont_divisores = 0
    
    while num <= n:
        if n % num == 0:
            cont_divisores += 1
        num += 1 

    if cont_divisores > 2:
        return False
    else:
        return True

x = int(input())
y = int(input())

while x <= y:
    if eh_primo(x) == True:
        print(x)
    x += 1
    

