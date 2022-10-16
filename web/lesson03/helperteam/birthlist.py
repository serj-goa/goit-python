from phonebook import AddressBook, Birthday, Name, Record

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


def get_birthdays_per_week(phonebook: AddressBook) -> None:
    """
    Gets a list of birthdays for the current week.
    """
    result_users = {}
    present_day = datetime.datetime.today()

    valid_dates_span = get_valid_dates_span(present_day)
    valid_months_and_days = [get_valid_month_and_day(
        date) for date in valid_dates_span]

    # phonebook['Serj'].birthday -> datetime(11-09-1983)
    for contact, record in phonebook.items():
        birth_day = record.birthday.value.day
        birth_month = record.birthday.value.month

        if get_valid_month_and_day(record.birthday.value) in valid_months_and_days:
            current_week_day = datetime.date(
                present_day.year, birth_month, birth_day).isoweekday()

            if not DAYS_OF_THE_WEEK[current_week_day] in result_users:
                result_users[DAYS_OF_THE_WEEK[current_week_day]] = [contact]
            else:
                result_users[DAYS_OF_THE_WEEK[current_week_day]].append(
                    contact)

    print_results(present_day, valid_dates_span, result_users)


def get_valid_month_and_day(date: datetime) -> tuple:
    """
    Gets the day and month of the contact's birth.
    """
    valid_month_and_day = (date.month, date.day)
    return valid_month_and_day


def get_valid_dates_span(present_day: datetime) -> list:
    """
    Gets the date range for the current week.
    """
    if present_day.isoweekday() == 1:
        start_day = (present_day - datetime.timedelta(days=2))
        valid_dates_span = [(start_day + datetime.timedelta(days=i))
                            for i in range(7)]

    elif present_day.isoweekday() == 7:
        start_day = (present_day - datetime.timedelta(days=1))
        valid_dates_span = [(start_day + datetime.timedelta(days=i))
                            for i in range(7)]

    else:
        start_day = present_day
        valid_dates_span = [(start_day + datetime.timedelta(days=i))
                            for i in range(7)]

    return valid_dates_span


def print_results(current_date: datetime, valid_dates: list, result_users: dict) -> None:
    """
    Display a list of contacts whose birthdays will be in the current week.
    """
    print(f'\nHello, today is {current_date.strftime("%d %B %Y")}.')

    if not len(result_users):
        print('Your contacts will not have birthdays during the week.')

    else:
        print('Happy birthday within a week:\n')

        for valid_date in valid_dates:
            valid_weekday = valid_date.strftime('%A')
            if valid_weekday in result_users:
                print(
                    f'{valid_weekday}: {", ".join(result_users[valid_weekday])}')
        print()
