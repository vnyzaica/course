lst = [
    ["А", 20],
    ["Б", 25],
    ["В", 19],
]
for i in range(0, len(lst), 2):

   print("Имя " + lst[i][0] + " Возраст " + str(lst[i][1]))