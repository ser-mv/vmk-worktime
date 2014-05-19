sql_types = {'int':'INTEGER', 'long':'INTEGER', 'str':'TEXT', 'unicode':'TEXT', 'float':'REAL'}

from employee import Employee
import sqlite3
import database

class database_sqlite(database.database):
    def __init__(self, filename):
        self.db = sqlite3.connect(filename, check_same_thread = False)
        self.cursor = self.db.cursor()

        columns = Employee().to_dict()
        del columns['id']

        request = 'CREATE TABLE IF NOT EXISTS employees '
        request += "(id INTEGER PRIMARY KEY UNIQUE"
        for column, value in columns.items():
            request += ', ' + column + ' ' + \
                           sql_types[type(value).__name__]
        request += ")"
        
        self.cursor.execute(request)
        self.db.commit()
        
    def save_employee(self, employee):
        parameters = employee.to_dict()
        
        request = 'INSERT OR REPLACE INTO employees ('
        for column in parameters.keys():
            request += column + ', '
        request = request[0:-2] + ') VALUES ('
        
        for column in parameters.keys():
            request += '?,'
        request = request[0:-1] + ')'
        print "!!SAVE", request, parameters.values()

        self.cursor.execute(request, parameters.values())
        self.db.commit()

    def load_employees(self, filters = None, #sorting = 'id',
                       first_index = 0, last_index = 10000):

        limit = last_index - first_index + 1
        offset = first_index
        
        columns = Employee().to_dict().keys()
        request = 'SELECT '
        for column in columns:
            request += column + ', '
        request = request[0:-2] + ' FROM employees '
        if filters != None and len(filters) != 0:
            request = request + 'WHERE '
            for key in filters.keys():
                request += key + ' = ? AND '
            request = request[0:-5]
        #request += ' ORDER BY ' + sorting
        request += ' LIMIT ' + str(limit)
        request += ' OFFSET ' + str(offset)

        print request

        print request, filters.values()
        
        if filters != None and len(filters) != 0:
            rows = self.cursor.execute(request, filters.values()).fetchall()
        else:
            rows = self.cursor.execute(request).fetchall()

        employees = []
        for row in rows:
            values_dict = {}
            for i in xrange(len(columns)):
                values_dict[columns[i]] = row[i]
            employee = Employee()
            employee.set_values(values_dict)
            employees.append(employee)
        return employees
        
        
    def delete_employee(self, employee_id):
        
        request = 'DELETE FROM employees WHERE id = '
        request += str(employee_id)

        self.cursor.execute(request)
        self.db.commit()
        
        
    def add_employee(self, employee):
        max_id = self.cursor.execute('SELECT MAX(id) FROM employees').fetchone()[0]
        if max_id == None:
            max_id = -1
        new_id = max_id + 1
        employee.id = new_id
        self.save_employee(employee)
        return employee
        
        
