#coding:utf-8
a = int(input("Введите количество тарелок "))

B = int(input("Введите количество средства "))

C = B/0.5

print (C)

if a == C :
    print("Все идеально")
else:
    if a>C :
        d = a-c
        print ("Осталось тарелок  ",d)
    else:
        d = a*0.5
        x = B-d
        print("Осталось средства  ",x)
