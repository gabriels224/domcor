import re

class validar():
    def __init__(self):
        pass

    def nome_correto(self, name):
        if not isinstance(name, str):
            return None
        if len(name.strip(), ) < 2:
            return None
        if not all(c.isalpha() or c.isspae() or c in "-'." for c in name):
            return None
        return True
    
    def validar_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$'
        return re.match(pattern, email) is not None
    
    def validar_senha(self, password):
        if not isinstance(password, str):
            return False
        if len(password) < 8:
            return False
        if not all(c.isdigit() for c in password):
            return False
        return True