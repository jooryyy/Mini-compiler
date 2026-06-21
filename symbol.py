# symbo;.py

class entry:
    def __init__(self, string, token):
        self.string = string
        self.token = token


symbol_table = []


def lookup(string):
    for i, elm in enumerate(symbol_table):
        if elm.string == string:
            return i
    return None


def insert(string, token):
    symbol_table.append(entry(string, token))
    return len(symbol_table) - 1


keywords = [
    entry(string='div', token='DIV'),
    entry(string='mod', token='MOD'),
    entry(string='if', token='IF'),
    entry(string='then', token='THEN'),
    entry(string='while', token='WHILE'),
    entry(string='do', token='DO'),
    entry(string='begin', token='BEGIN'),
    entry(string='end', token='END'),
    entry(string='void', token='VOID'),
    entry(string='main', token='MAIN'),

]


def initialize():
    for elm in keywords:
        insert(elm.string, elm.token)

