'''

Задание

    Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
    Превратите строку "01/01/25 12:10:03.234567" в объект datetime

'''

from datetime import datetime, timedelta

def main()
    delta_yesterday = timedelta(days=1)
    dt_yesterday = datetime.now() - delta_yesterday
    dt_yesterday = dt_yesterday.strftime('%d.%m.%Y')
    print(f'Вчерашняя дата: {dt_yesterday}')

    dt_now = datetime.now().strftime('%d.%m.%Y')
    print(f'Сегодняшняя дата: {dt_now}')

    delta_thirty_days_back = timedelta(days=30)
    dt_thirty_days_back = datetime.now() - delta_thirty_days_back
    dt_thirty_days_back = dt_thirty_days_back.strftime('%d.%m.%Y')
    print(f'Дата 30 дней назад: {dt_thirty_days_back}')

    dt_string = '01/01/25 12:10:03.234567'
    dt_date = datetime.strptime(dt_string, ('%d/%m/%y %H:%M:%S.%f'))
    print(dt_date)
    
if __name__ == "__main__":
    main()