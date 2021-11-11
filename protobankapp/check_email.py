import re

def ama(email:str) ->str:
    '''
        ama is a function that takes email as an args and check if
        it is a valid email address.
    '''
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    matches = re.finditer(pattern, email)
    for i in matches:
        return i.group(0)

def nums(num)->str:
    pattern = re.compile(r'[0-9]')
    matches = re.finditer(pattern, num)
    for i in matches:
        return i.group(0)