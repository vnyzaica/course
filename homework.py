f = open('document.txt', "w")

lst = [
    ["Имя Фамилия 1", 20],
    ["Имя Фамилия 2", 25],
    ["Имя Фамилия 3", 19],
    ["Имя Фамилия 4", 12],
    ["Имя Фамилия 5", 16],
    ["Имя Фамилия 6", 34],
    ["Имя Фамилия 7", 76],
]
for i in range(0, len(lst), 1):

   print("Имя " + lst[i][0] + " Возраст " + str(lst[i][1]))
s =str(0)
q =str(len(lst[0]))
w =str(len(lst[1]))
e =str(len(lst[2]))
r =str(len(lst[3]))
t =str(len(lst[4]))
y =str(len(lst[5]))
u =str(len(lst[6]))

if q > 15:
    s +=1
if w > 15:
    s +=1
if e > 15:
    s +=1
if r > 15:
    s +=1
if t > 15:
    s +=1
if y > 15:
    s +=1
if u > 15:
    s +=1
 
q = lst[1][-1]
print (q)
print( s )
x = 10

f = open('document.txt', "w")

f.write(str(x) + '\n' + str(x))
f.close()