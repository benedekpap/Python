def add_time(start_time, duration_time, week_start=None):

    time, period = start_time.split()
    s_hours, s_minutes = map(int,time.split(':'))
    d_hours, d_minutes = map(int,duration_time.split(':'))

    #convert everything to 24hour format
    if period == 'PM':
        s_hours = s_hours + 12

    new_hour24 = (s_hours + d_hours)
    new_minutes = s_minutes + d_minutes

    # convert the remaining minutes to hours
    if new_minutes > 60:
        new_hour24 = new_hour24 + round((new_minutes / 60)/1)
        new_minutes = new_minutes % 60

    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',\
                'Friday', 'Saturday', 'Sunday']

    #dealing with days passed
    if new_hour24 > 24:
        days_passed = round((new_hour24 / 24)/1)
        new_hour24 = new_hour24 % 24
    else:
        days_passed = 0

    if week_start !=None:  # add the day of the week
        day = week_start.strip().capitalize()
        selected_day = int((week_days.index(day) + days_passed) % 7)
        current_day = week_days[selected_day]

    #converting back to the 12 hour format
    if new_hour24 > 12:
        new_hour12 = new_hour24 - 12
        period = 'PM'
    if new_hour24 == 12:
        new_hour12 = 12
        period = 'PM'
    if new_hour24 < 12:
        if new_hour24 == 0:
            new_hour12 = 12
            period = 'AM'
        else:
            new_hour12 = new_hour24
            period = 'AM'

    if new_minutes <10:
        new_minutes = f'0{new_minutes}'

    if days_passed < 1:

        if week_start == None:

            new_time = f'{new_hour12}:{new_minutes} {period}'
        else:
            new_time = f'{new_hour12}:{new_minutes} {period}, {current_day}'

    if days_passed > 0:
        if days_passed == 1:
            if week_start == None:
                new_time = f'{new_hour12}:{new_minutes} {period} (next day)'

            else:
                new_time = f'{new_hour12}:{new_minutes} {period}, {current_day} (next day)'
        else:
            if week_start == None:
                new_time = f'{new_hour12}:{new_minutes} {period} ({days_passed} days later)'

            else:
                new_time = f'{new_hour12}:{new_minutes} {period}, {current_day} ({days_passed} days later)'

    return new_time

result = add_time("8:16 PM", "466:02", 'tuesday')
print(result)

 #with "8:16 PM", "466:02", "tuesday" to return "6:18 AM, Monday (20 days later)"
