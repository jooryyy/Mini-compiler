#lexer.py

import re
import parser
from symbol import lookup, insert, symbol_table

input_file = open("file.exp", "r")
input_text0 = input_file.read()


input_text = re.split(r'([\W])', input_text0)
input_text = [x for x in input_text if (x != '') and (x != '\t') and (x != ' ')]

input_index = 0
lineno = 1
tokenval = 0


def lexan():
    global input_index, lineno, tokenval

    while True:
        if input_index < len(input_text):

            t = input_text[input_index]
            input_index += 1



            if t.isdigit():
                tokenval = int(t)
                return 'NUM'

            elif t == '\n':
                lineno += 1

            elif t.isalnum():
                p = lookup(t)
                if p is None:
                    p = insert(t, 'ID')
                tokenval = p
                return symbol_table[p].token

            else:
                return t

        else:
            return 'EOF'
