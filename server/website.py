from flask import render_template

db = None

def index_page():
    return render_template('index.html', \
                           param1 = None, \
                           param2 = None)

def employees_page(filters, month, sorting):
    employees = db.load_employees(filters = filters)
    table = []
    for employee in employees:
        hours = employee.get_working_hours(month)
        salary = hours * employee.salary_per_hour
        table.append([employee.id, employee.name, employee.age, hours, salary])
    if sorting != None:
        if sorting > 0:
            table = sorted(table, key = lambda x: x[sorting-1])
        else:
            table = sorted(table, key = lambda x: x[-sorting-1], reverse = True)
    month_str = str(month % 100) + ' ' + str(month / 100)
    return render_template('table.html',
                           employees = table, filters = filters, month = month_str)
