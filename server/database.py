from abc import ABCMeta, abstractmethod, abstractproperty

class database():
    __metaclass__=ABCMeta
    
    @abstractmethod
    def save_employee(employee):
        pass
        
    @abstractmethod
    def load_employees(filters):
        pass
