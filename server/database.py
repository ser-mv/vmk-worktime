from abc import ABCMeta, abstractmethod, abstractproperty

class database():
    __metaclass__=ABCMeta
    
    @abstractmethod
    def save_employee(self, employee):
        pass
        
    @abstractmethod
    def load_employees(self, filters = None, sorting = 'id',
                       first_index = 0, last_index = 10000):
        pass
