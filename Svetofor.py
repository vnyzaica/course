#coding:utf-8

import datetime
from datetime import datetime #импорт модуля

print(datetime.now()) #Время сейчас

a = datetime.now()
b = a.minute
print (b)
c = b % 5
if c < 4 :
    print ("зеленый")
else:
    print("красный")

print("Green" if c < 4 else "Red")#тернарный оператор




#другой способ
now = datetime.now()
print("red" if ((now.minute % 5) > 3) else "green")