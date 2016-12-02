#coding:utf-8

import math

a = int(input("Координата Х у А "))
a2 = int(input("Координата Y у А "))
b = int(input("Координата Х у B "))
b2 = int(input("Координата Y у B "))
c = int(input("Координата Х у C "))
c2 = int(input("Координата Y у C "))

if a<b :
    A1 = (b-a)
else:
    A1 = (a-b)

if a2<b2 :
    A2 = (b2-a2)
else:
    A2 = (a2-b2)

if a<c :
    B1 = (c-a)
else:
    B1 = (c-b)

if a2<c2 :
    B2 = (c2-a2)
else:
    B2 = (a2-c2)

if b<c :
    C1 = (c-b)
else:
    C1 = (b-c)

if b2<c2 :
    C2 = (c2-b2)
else:
    C2 = (b2-c2)





A = math.sqrt(A1*A1 + A2*A2)
B = math.sqrt(B1*B1 + B2*B2)
C = math.sqrt(C1*C1 + C2*C2)
print (A)
print (B)
print (C)

if A>B and A>C and A*A==B*B+C*C :
    print ("прямоугольный")
else:
    if B>C and B>A and B*B==A*A+C*C:
        print("Прямоугольный")
    else:
        if C>A and C>B and C*C==A*A+C*C:
            print("Прямоугольный")
        else:
            print("не прямоугольный")  

 