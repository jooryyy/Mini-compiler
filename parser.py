import error
import symbol
import emitter
import lexer

file_input = open('file.exp', 'r')

input_text0 = file_input.read()

lookahead = ''

tok = 0


def match(token):
    global lookahead
    if lookahead == token:
        lookahead = lexer.lexan()
    else:
        error.error()


def parse():
    global lookahead
    symbol.initialize()
    lookahead = lexer.lexan()
    while lookahead != 'EOF':
        FuncDec()


def FuncDec():
    match('VOID')
    restFunc()


def restFunc():
    global lookahead

    if lookahead == 'ID':
        emitter.emit('func_id', lexer.tokenval)
        match('ID')
        match('(')
        match(')')
        match('BEGIN')
        CS()
        match('END')
        match(';')
        emitter.emit('ret')

    elif lookahead == 'MAIN':
        match('MAIN')
        emitter.emit('main')
        match('(')
        match(')')
        match('BEGIN')
        CS()
        match('END')
        match('.')
        emitter.emit('exit')

    else:
        error.error()


def restID():
    global lookahead, tok
    if lookahead == '=':
        match('=')
        expr()
        emitter.emit('ASSIGN', tok)
    elif lookahead == '(':
        match('(')
        match(')')
        emitter.emit('call', tok)
    else:
        error.error()


def stmt():
    global lookahead, tok

    if lookahead == 'ID':
        tok = lexer.tokenval
        match('ID')
        restID()

    elif lookahead == 'IF':
        match('IF')
        match('(')
        expr()
        match(')')
        emitter.emit('IF')

        match('THEN')
        stmt()

        emitter.emit('ELSE')

    elif lookahead == 'WHILE':
        emitter.emit('WHILE')

        match('WHILE')
        match('(')
        expr()
        match(')')
        emitter.emit('WHILE2')

        match('DO')
        stmt()
        emitter.emit('WHILE3')

    elif lookahead == 'BEGIN':
        match('BEGIN')
        CS()
        match('END')

    else:
        error.error()


def CS():
    global lookahead
    while lookahead != 'END':
        stmt()
        match(';')


def expr():
    term()
    moreterms()


def term():
    factor()
    morefactors()


def morefactors():
    if lookahead == '*':
        match('*')
        factor()
        emitter.emit('*')
        morefactors()

    elif lookahead == '/':
        match('/')
        factor()
        emitter.emit('/')
        morefactors()

    elif lookahead == 'DIV':
        match('DIV')
        factor()
        emitter.emit('DIV')
        morefactors()

    elif lookahead == 'MOD':
        match('MOD')
        factor()
        emitter.emit('MOD')
        morefactors()


def moreterms():
    if lookahead == '+':
        match('+')
        term()
        emitter.emit('+')
        moreterms()

    elif lookahead == '-':
        match('-')
        term()
        emitter.emit('-')
        moreterms()


def factor():
    global lookahead

    match lookahead:
        case '(':
            match('(')
            expr()
            match(')')

        case 'NUM':
            emitter.emit('NUM', lexer.tokenval)
            match('NUM')

        case 'ID':
            emitter.emit('ID', lexer.tokenval)
            match('ID')

        case _:
            error.error()
