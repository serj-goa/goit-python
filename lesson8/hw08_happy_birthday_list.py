import datetime


DAYS_OF_THE_WEEK = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Monday',
    7: 'Monday'
    }


def get_birthdays_per_week(users: list) -> None:
    result_users = {}
    present_day = datetime.datetime.today()

    valid_dates_span = get_valid_dates_span(present_day)
    valid_months_and_days = [get_valid_month_and_day(date) for date in valid_dates_span]
    print(valid_dates_span)
    print(valid_months_and_days)

    for user in users:
        birth_day = user['birthday'].day
        birth_month = user['birthday'].month
        
        if get_valid_month_and_day(user['birthday']) in valid_months_and_days:
            current_week_day = datetime.date(present_day.year, birth_month, birth_day).isoweekday()

            if not DAYS_OF_THE_WEEK[current_week_day] in result_users:
                result_users[DAYS_OF_THE_WEEK[current_week_day]] = [user['name']]
            else:
                result_users[DAYS_OF_THE_WEEK[current_week_day]].append(user['name'])

    print_results(present_day, valid_dates_span, result_users)


def get_valid_month_and_day(date: datetime) -> tuple:
    valid_month_and_day = (date.month, date.day)
    return valid_month_and_day


def get_valid_dates_span(present_day: datetime) -> list:
    if present_day.isoweekday() == 1:
        start_day = (present_day - datetime.timedelta(days=2))
        valid_dates_span = [(start_day + datetime.timedelta(days=i)) for i in range(7)]
    elif present_day.isoweekday() == 7:
        start_day = present_day
        valid_dates_span = [(start_day + datetime.timedelta(days=i)) for i in range(6)]
    else:
        start_day = present_day
        valid_dates_span = [(start_day + datetime.timedelta(days=i)) for i in range(7)]

    return valid_dates_span


def print_results(current_date: datetime, valid_dates: list, result_users: dict) -> None:
    print(f'Hello, today is {current_date.strftime("%d %B %Y")}.')

    if not len(result_users):
        print('Your contacts will not have birthdays during the week.')
        quit()

    print('During the week, you need to congratulate on your birthday:\n')

    for valid_date in valid_dates:
        valid_weekday = valid_date.strftime('%A')
        if valid_weekday in result_users:
            print(f'{valid_weekday}: {", ".join(result_users[valid_weekday])}')
    print()


if __name__ == '__main__':
    users = [
    {'name': 'Alex', 'birthday': datetime.date(1980, 7, 19)},
    {'name': 'Katy', 'birthday': datetime.date(1991, 7, 20)},
    {'name': 'Lilly', 'birthday': datetime.date(1989, 7, 16)},
    {'name': 'John', 'birthday': datetime.date(1989, 7, 15)},
    {'name': 'Billy', 'birthday': datetime.date(1985, 7, 22)},
    {'name': 'Andy', 'birthday': datetime.date(1994, 7, 17)},
    {'name': 'Olha', 'birthday': datetime.date(1990, 7, 23)},
    {'name': 'Sam', 'birthday': datetime.date(1989, 7, 18)},
    {'name': 'Anna', 'birthday': datetime.date(1989, 7, 21)},
    {'name': 'Vicky', 'birthday': datetime.date(1989, 7, 24)},
    {'name': 'Mike', 'birthday': datetime.date(1989, 7, 26)},
    {'name': 'Den', 'birthday': datetime.date(1989, 7, 25)},
    {'name': 'Robin', 'birthday': datetime.date(1985, 7, 30)},
    {'name': 'Lora', 'birthday': datetime.date(1994, 7, 31)},
    {'name': 'Tim', 'birthday': datetime.date(1990, 8, 1)},
    {'name': 'Danny', 'birthday': datetime.date(1989, 8, 2)},
    {'name': 'Tom', 'birthday': datetime.date(1989, 8, 3)},
    {'name': 'Gans', 'birthday': datetime.date(1989, 8, 4)},
    {'name': 'Rodrigo', 'birthday': datetime.date(1989, 8, 5)},
    {'name': 'Sancho', 'birthday': datetime.date(1989, 8, 6)},
    {'name': 'Robert', 'birthday': datetime.date(1989, 8, 18)},
]

    get_birthdays_per_week(users)
