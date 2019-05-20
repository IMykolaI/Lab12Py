import re

reader = open('access_log_Jul95', encoding='latin1')

try:

    request_list = reader.readlines()

    date_pattern = '01/Jul/1995'
    type_pattern = '.html'
    error_pattern = '\s4\d{2}\s'
    time_pattern = '\d{4}:\d{2}:\d{2}'
    hour_pattern = ':\d{2}:'
    minute_pattern = ':\d{2}\s'
    digit_pattern = '\d{2}'
    min_hour = 2
    max_hour = 7
    min_minute = 19
    max_minute = 55

    count = 0

    print('\nStarting an application...')

    for request in request_list:

        if re.search(date_pattern, request) and re.search(type_pattern, request) and re.search(error_pattern, request):
            if re.search(time_pattern, request):

                time = re.search(time_pattern, request).group() + ' '
                hour = re.search(hour_pattern, time).group()
                minute = re.search(minute_pattern, time).group()

                if int(re.search(digit_pattern, hour).group()) == min_hour:
                    if int(re.search(digit_pattern, minute).group()) >= min_minute:
                        count += 1
                if min_hour < int(re.search(digit_pattern, hour).group()) < max_hour:
                    count += 1
                if int(re.search(digit_pattern, hour).group()) == max_hour:
                    if int(re.search(digit_pattern, minute).group()) <= max_minute:
                        count += 1

    print(f'Number of unsuccessful GET/POST requests between 2:19 and 7:55 of 01/Jul/1995 is {count}')
finally:

    reader.close()
