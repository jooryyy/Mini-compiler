from symbol import *

file_output = None
file_output2 = None


# import lexer
def emit(token, attribute=None):
    match token:

        case '+':
            file_output2.write('+ ')
            file_output.write('pop r1\npop r2\nadd r2, r1\npush r2\n')

        case '-':
            file_output2.write('- ')
            file_output.write('pop r1\npop r2\nsub r2, r1\npush r2\n')

        case '*':
            file_output2.write('* ')
            file_output.write('pop r1\npop r2\nmul r2, r1\npush r2\n')

        case '/':
            file_output2.write('/ ')
            file_output.write('pop r1\npop r2\ndiv r2, r1\npush r2\n')

        case 'MOD':
            file_output2.write('mod ')
            file_output.write('pop r1\npop r2\nmod r2, r1\npush r2\n')

        case 'DIV':
            file_output2.write('idiv ')
            file_output.write('pop r1\npop r2\nidiv r2, r1\npush r2\n')

        case 'NUM':
            file_output2.write(str(attribute) + ' ')
            file_output.write('push ' + str(attribute) + '\n')

        case 'ID':
            file_output2.write(symbol_table[attribute].string + ' ')
            file_output.write('push ' + symbol_table[attribute].string + '\n')

        case 'ASSIGN':
            file_output.write('pop ' + symbol_table[attribute].string + '\n')

        case 'call':
            file_output.write('call ' + symbol_table[attribute].string + '\n')

        case 'IF':
            file_output.write('pop r2 \ncmp r2,0 \nbe else\n')

        case 'ELSE':
            file_output.write('else:\n')

        case 'WHILE':
            file_output.write('while:\n')

        case 'WHILE2':
            file_output.write('pop r2 \ncmp r2,0 \nbe endwhile\n')

        case 'WHILE3':
            file_output.write('b while\nendwhile\n')

        case 'func_id':
            file_output.write(symbol_table[attribute].string + ':\n')
        case 'ret':
            file_output.write('ret\n')
        case 'main':
            file_output.write('main:\n')
        case 'exit':
            file_output.write('exit\n')

        case _:
            pass