from re import Match
import lexer
file_error  = open('file.err', 'w')

def error():
    file_error.write('line:' + str(lexer.lineno) + ' syntax error')
    raise SystemExit