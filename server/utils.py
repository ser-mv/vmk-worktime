import datetime

def current_month():
    now = datetime.datetime.now()
    return now.year * 100 + now.month
    
