from hashlib import sha256

def check_password(employee, password):
    valid_hash = employee.password_hash
    h = sha256()
    h.update('eoijfo3ir09jdf')
    h.update(password)
    new_hash = h.hexdigest()
    return valid_hash == new_hash
    

def set_password(employee, new_password):
    h = sha256()
    h.update('eoijfo3ir09jdf')
    h.update(new_password)
    password_hash = h.hexdigest()
    employee.password_hash = password_hash
