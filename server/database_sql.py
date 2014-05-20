sql_types = {'int':'INTEGER', 'long':'INTEGER', 'str':'TEXT', 'unicode':'TEXT', 'float':'REAL'}

from employee import Employee
import sqlite3
import psycopg2
import database
import traceback

class database_sql(database.database):
    def __init__(self):
        self.db = None
        self.cursor = None
        self.f = None
        
    def init_sqlite(self, filename):
        self.f = '?'
        self.db = sqlite3.connect(filename, check_same_thread = False)
        self.init_table()

    def init_postgresql(self, database, user, password, host, port):
        self.f = '%s'
        self.db = psycopg2.connect(database = database, user = user, password = password,
                                   host = host, port = port, async = 0)
        self.init_table()
        
    def init_table(self):
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
        
        request = 'UPDATE employees SET '
        for column in parameters.keys():
            request += column + '=' + self.f + ', '
        
        request = request[0:-2]
        request += " WHERE id = " + str(employee.id)

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
                request += key + ' = ' + self.f + ' AND '
            request = request[0:-5]
        #request += ' ORDER BY ' + sorting
        #request += ' LIMIT ' + str(limit)
        #request += ' OFFSET ' + str(offset)


        try:
            if filters != None and len(filters) != 0:
                self.cursor.execute(request, filters.values())
            else:
                self.cursor.execute(request)
            rows = self.cursor.fetchall()
        except Exception as e:
            print traceback.format_exc()
            print e
            rows = []

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
        try:
            print self.cursor.execute('SELECT max(id) FROM employees;')
            self.cursor.execute('SELECT max(id) FROM employees')
            max_id = self.cursor.fetchone()[0]
        except Exception as e:
            print e
            print traceback.format_exc()
            max_id = None
            
        if max_id == None:
            max_id = 0
        new_id = max_id + 1
        employee.id = new_id
        parameters = employee.to_dict()
        
        request = 'INSERT INTO employees ('
        for column in parameters.keys():
            request += column + ', '
        request = request[0:-2] + ') VALUES ('
        
        for column in parameters.keys():
            request += self.f + ','
        request = request[0:-1] + ')'

        self.cursor.execute(request, parameters.values())
        self.db.commit()
        return employee
        
        
