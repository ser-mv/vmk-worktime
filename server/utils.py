import datetime

def current_month():
    now = datetime.datetime.now()
    return now.month_str + ' ' + str(now.year * 100)
    
