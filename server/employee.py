import utils
import json

class employee():
    def __init__(self, init_values = None):
        self.id = -1
        self.name = ""
        self.age = 0
        self.password_hash = 'abcd_fake_initial_password'
        self.salary_per_hour = 0
        self.working_months = json.dumps({}) #stores working seconds for each month
        
        if init_values != None:
            for key in init_values.keys:
                setattr(self, key, init_values[key])

    def add_working_seconds(self, working_seconds):
        working_months = json.loads(self.working_months)
        current_month = utils.current_month()
        
        if current_month not in working_months:
            working_months[current_month] = working_seconds
        else:
            working_months[current_month] += working_seconds

        self.working_months = json.dumps(working_months)
            

    def get_working_hours(self, month):
        working_months = json.loads(self.working_months)
        if month not in working_months:
            return 0
        else:
            return working_months[month] / (60*60)

    def to_dict(self):
        return self.__dict__
        
