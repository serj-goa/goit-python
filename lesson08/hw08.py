from datetime import datetime, timedelta


def get_birthday_per_week(users: list) -> None:
    """
    Iterate through the list of dictionaries and add valid data to the new list of dictionaries.
    Users and dates of birth who have a birthday next week.
    """
    current_year = datetime.now().year
    days_counter = 1

    while days_counter <= 7:
        valid_day = datetime.now() + timedelta(days=days_counter)

        for user in users:
            for key, value in user.items():
                if key == 'birthday' and value.month == valid_day.month and value.day == valid_day.day:
                    date = user['birthday']
                    valid_year = date.replace(year=current_year)
                    day = valid_year.strftime("%A")

                    if day == 'Saturday' or day == 'Sunday':
                        work_days['Monday'].append(user['name'])
                        continue
                    work_days[day].append(user['name'])

        days_counter += 1


def printing_names(work_days: dict) -> None:
    for day, name_lst in work_days.items():
        names = ', '.join(name_lst)
        if len(name_lst) != 0:
            print(f'{day}: {names}')


if __name__ == '__main__':
    users = [
        {'name': 'Dmytro', 'birthday': datetime(1998, 2, 17)},
        {'name': 'Anton', 'birthday': datetime(1998, 2, 5)},
        {'name': 'Petya', 'birthday': datetime(1998, 2, 26)},
        {'name': 'Alex', 'birthday': datetime(1998, 3, 30)},
        {'name': 'Tolya', 'birthday': datetime(1998, 3, 28)},
        {'name': 'Vasya', 'birthday': datetime(1998, 2, 23)},
        {'name': 'Iowa', 'birthday': datetime(1995, 2, 23)},
        {'name': 'Kate', 'birthday': datetime(1995, 2, 20)},
        {'name': 'Toma', 'birthday': datetime(1995, 2, 19)},
        {'name': 'Nick', 'birthday': datetime(1998, 2, 26)},
        {'name': 'Nikita', 'birthday': datetime(1998, 3, 31)},
        {'name': 'Sam', 'birthday': datetime(1998, 2, 25)},
        {'name': 'Sara', 'birthday': datetime(1998, 3, 1)},
        {'name': 'Vitaliy', 'birthday': datetime(1998, 3, 30)}
    ]

    work_days = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    get_birthday_per_week(users)
    printing_names(work_days)
