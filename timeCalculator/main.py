def add_time(start, duration, start_day=None):
    # Define days of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert start time to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add duration to start time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60
    end_minute %= 60
    end_day_count = end_hour // 24
    end_hour %= 24

    # Convert end time back to 12-hour format
    if end_hour == 0:
        period = 'AM'
        end_hour = 12
    elif 1 <= end_hour < 12:
        period = 'AM'
    elif end_hour == 12:
        period = 'PM'
    else:
        period = 'PM'
        end_hour -= 12

    # Calculate the day of the week
    if start_day:
        start_day_index = days_of_week.index(start_day.capitalize())
        end_day_index = (start_day_index + end_day_count) % 7
        end_day = days_of_week[end_day_index]
        end_day_str = f", {end_day}"
    else:
        end_day_str = ""

    # Calculate the number of days later
    if end_day_count == 1:
        day_later_str = " (next day)"
    elif end_day_count > 1:
        day_later_str = f" ({end_day_count} days later)"
    else:
        day_later_str = ""

    # Format the end time
    end_time = f"{end_hour}:{end_minute:02d} {period}{end_day_str}{day_later_str}"

    return end_time

# Example usage:
print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM
print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)
