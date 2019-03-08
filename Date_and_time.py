#Напечатайте в консоль даты: вчера, сегодня, месяц назад
#Превратите строку "01/01/17 12:10:03.234567" в объект datetime

#import datetime
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL,'russian')

def minus_month(i_date):
    pass

#MAIN

#date_date=datetime.today()
date_str=input("Введите дату в формате YYYY MM DD: ")
try: 
    init_date=datetime.strptime(date_str,"%Y %m %d")
except ValueError:
    print("Дата введена неправильно")
    exit()
print(f'Исходная дата: {datetime.strftime(init_date, "%A %d %B %Y")}')
try:
    yesterday_date=init_date-timedelta(days=1)
except OverflowError:
    print("Комп говорит, что за день до указанной даты времени не было")
    exit()
print(f'Вчера от нее была дата: {datetime.strftime(yesterday_date, "%A %d %B %Y")}')
try:
    monthbefore_date=init_date-timedelta(days=30)
except OverflowError:
    print("Комп говорит, что за 30 дней до указанной даты времени не было")
    exit()   
print(f'30 дней назад от нее была дата: {datetime.strftime(monthbefore_date, "%A %d %B %Y")}')