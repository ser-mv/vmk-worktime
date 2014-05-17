import user_authorization

db = None

def check_authorization(employee_id, password):
    employee = db.load_employees(filters = {'id':employee_id})[0]
    return user_authorization.check_password(employee, password)

def add_working_seconds(employee_id, working_seconds, password):
    employee = db.load_employees(filters = {'id':employee_id})[0]
    if not user_authorization.check_password(employee, password):
        return 'wrong user password'
    employee.add_working_seconds(working_seconds)
    db.save_employee(employee)
    return 'ok'
    
