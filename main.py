import parser
import emitter
from symbol import *
import lexer

def main():
    front_end()
    back_end()


def front_end():

    emitter.file_output = open('file.il', 'w')
    emitter.file_output2 = open('file.obj', 'w')

    parser.parse()

    emitter.file_output.close()
    emitter.file_output2.close()


def back_end():
    pass


if __name__ == '__main__':
    main()
