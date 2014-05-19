from flask import render_template
from employee import Employee
import json

db = None

def index_page(info_text = ''):
    return render_template('index.html', \
                           info_text = info_text)

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
    month_str = month
    return render_template('table.html',
                           employees = table, filters = filters, month = month_str)



def edit_employee_page(employee_id, new_employee = False):
    if new_employee:
        values = Employee().to_dict()
        for key in values.keys():
            values[key] = ''
        values['working_months'] = {}
    else:
        employee = db.load_employees(filters = {'id':employee_id})[0]
        values = employee.to_dict()
        values['working_months'] = json.loads(values['working_months'])
        for key in values['working_months'].keys():
            values['working_months'][key] /= 3600
            
    return render_template('edit_employee.html',
                    values = values)

def save_employee(values):
    values['age'] = int(values['age'])
    values['salary_per_hour'] = int(values['salary_per_hour'])
    if values['id'] == '':
        values['id'] = 0
        employee = Employee(values)
        db.add_employee(employee)
    else:
        values['id'] = int(values['id'])
        employee = db.load_employees(filters = {'id':values['id']})[0]
        for key, value in values.items():
            employee.setattr(key, value)
        db.save_employee(employee)
    return index_page(info_text = 'Employee was saved')
