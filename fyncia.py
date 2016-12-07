# Название функции
def fff():
    print('Hello world!')
#Запуск функции
fff()
fff()
fff()




import datetime

f = open('log.txt','w')


def log_time():
    now = datetime.datetime.now()
    f.write(str(now)+ '\n' )


log_time()
log_time()
log_time()

















