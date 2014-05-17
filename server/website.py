from flask import render_template
from employee import Employee
import json
x: x[sorting-1])
        else:
            table = sorted(table, key = lambda x: x[-sorting-1], reverse = True)
    month_str = str(month % 100) + ' ' + str(month / 100)
    return render_template('table.html',
                           employees = table, filters = filters, month = month_str)


def edit_employee_page(employee_id, new_employee = False):
    if new_employee:
        values = Employee.to_dict()
        for key in values.keys():
            values[key] = ''
        values['working_months'] = {}
    else:
        employee = db.load_employees(filters = {'id':employee_id})[0]
        values = employee.to_dict()
        values['working_months'] = json.loads(values['working_months'])
        for key in values['working_months'].keys():
            values['working_months'][key] /= 3600
            
    render_template('edit_employee.html',
                    values = values)
