def add_time(start, duration, *args):

    # Get start hr and min
    s = start.split(':')
    start_hr = s[0]
    start_min = s[1].split(' ')[0]
    start_period = s[1].split(' ')[1]
    if start_period == "PM": start_hr = int(start_hr) + 12

    # Get duration hr and min
    d = duration.split(':')
    duration_hr = d[0]
    duration_min = d[1]

    # Calculate final minutes
    end_min = int(start_min) + int(duration_min)
    end_min_remainder = end_min // 60
    end_min = str(end_min % 60)
    if len(end_min) == 1: end_min = '0' + end_min

    # Calculate final hours
    end_hr = int(start_hr) + int(duration_hr) + end_min_remainder
    x_days_later = end_hr // 24
    end_hr_remainder = end_hr // 12
    end_hr = str(end_hr % 12)
    if end_hr == '0': end_hr = '12'

    # Calculate period
    if end_hr_remainder % 2 == 1:
        end_period = 'PM'
    elif end_hr_remainder % 2 == 0:
        end_period = 'AM'

    # Calculate day of week
    dow = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    if x_days_later > 1:
        if len(args) > 0:
            start_dow = args[0].title()
            dow_idx = dow.index(start_dow)
            new_dow_idx = (dow_idx + x_days_later) % 7
            end_dow = dow[new_dow_idx]
        end_text = f'({x_days_later} days later)'
    elif x_days_later > 0:
        if len(args) > 0:
            start_dow = args[0].title()
            dow_idx = dow.index(start_dow)
            new_dow_idx = (dow_idx + x_days_later) % 7
            end_dow = dow[new_dow_idx]
        end_text = '(next day)'
    else:
        if len(args) > 0:
            end_dow = args[0].title()
        end_text = ''

    # Get end time
    if len(args) > 0:
        end_time = end_hr + ':' + end_min + ' ' + end_period + ', ' + end_dow + ' ' + end_text
        end_time = end_time.rstrip()
    elif x_days_later > 0:
        end_time = end_hr + ':' + end_min + ' ' + end_period + ' ' + end_text
        end_time = end_time.rstrip()
    else:
        end_time = end_hr + ':' + end_min + ' ' + end_period

    print(end_time)
    return end_time

# add_time("3:00 PM", "3:10")
# add_time("11:30 AM", "2:32", "Monday")
# add_time("11:43 AM", "00:20")
# add_time("10:10 PM", "3:30")
# add_time("11:43 PM", "24:20", "tueSday")
# add_time("6:30 PM", "205:12")
# add_time("2:59 AM", "24:00", "saturDay")
add_time("3:30 PM", "2:12", "Monday")