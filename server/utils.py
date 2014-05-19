import datetime

def current_month():
    now = datetime.datetime.now()
    return str(now.month) + ' ' + str(now.year * 100)
    
