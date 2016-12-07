f = 1
x = int(30)
y = int(30)
z = int(1)

def menu(): 
    global x,y,z
    a = int(input('Введите число столов: '))
    b = int(input('Введите число стульев: '))
    c = int(input('Введите число досок: '))
    x = x + a
    y = y + b 
    z = z + c
    print(x)
    print(y)
    print(z)

while f > 0 :
    menu()
    f += 1

