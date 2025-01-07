import datetime#библиотека для работы с датой и временем

def date_in_future(integer):
    now = datetime.datetime.now()#получаем текущую дату
    if(type(integer)==int):
        now += datetime.timedelta(days=integer)#прибавляем "разницу" в целых днях
    now = now.strftime("%d-%m-%Y %H:%M:%S")#приводим в требуемомум формату
    print(now)
    return now

date_in_future([]) # => текущая дата
date_in_future(2) # => текущая дата + 2 дня
date_in_future(6.5) # => текущая дата