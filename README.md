# Mini Compiler (Python)

A small compiler built in Python from scratch — no parser-generator libraries, no external dependencies. It implements a full front-end pipeline: lexical analysis, recursive-descent parsing, symbol table management, and code emission to a stack-based intermediate language.

## Overview

This project compiles a small procedural language — function declarations, a `main` block, assignment, `if/then`, `while/do`, function calls, and arithmetic expressions (`+ - * / mod div`, parentheses) — into stack-based intermediate code, the same way a real compiler front end lowers source code before final code generation.

```
Source (file.exp)  -->  Lexer  -->  Parser  -->  Emitter  -->  IL + Object output
                            |            |
                      Symbol table   Error handler
```

## Language features

- Function declarations: `void name() begin ... end;`
- Program entry point: `main() begin ... end.`
- Assignment: `x = expr;`
- Function calls: `name();`
- Conditionals: `if (expr) then stmt`
- Loops: `while (expr) do stmt`
- Block statements: `begin ... end`
- Arithmetic expressions with standard precedence: `+ - * / mod div` and parentheses
- Identifiers and numeric literals

## Pipeline stages

**Lexer (`lexer.py`)**
Reads the raw input and breaks it into tokens (`NUM`, `ID`, keywords, operators, `EOF`). Identifiers and reserved keywords are looked up or interned in the symbol table; numbers carry their value in `tokenval`.

**Symbol table (`symbol.py`)**
A list-backed table (`lookup` / `insert`) storing identifiers and reserved keywords (`div`, `mod`, `if`, `then`, `while`, `do`, `begin`, `end`, `void`, `main`) along with their token type.

**Parser (`parser.py`)**
A recursive-descent parser implementing the grammar:

```
parse      -> FuncDec*
FuncDec    -> void restFunc
restFunc   -> ID ( ) begin CS end ;
            | main ( ) begin CS end .
CS         -> (stmt ;)*
stmt       -> ID restID
            | if ( expr ) then stmt
            | while ( expr ) do stmt
            | begin CS end
restID     -> = expr
            | ( )
expr       -> term moreterms
moreterms  -> + term moreterms | - term moreterms | ε
term       -> factor morefactors
morefactors-> * factor morefactors | / factor morefactors
            | div factor morefactors | mod factor morefactors | ε
factor     -> ( expr ) | NUM | ID
```

Operator precedence is encoded directly in the grammar — `*`, `/`, `div`, `mod` bind tighter than `+`, `-`.

**Emitter (`emitter.py`)**
Called by the parser as each grammar rule is reduced. Emits:
- A readable postfix/object trace (`file.obj`)
- Stack-based intermediate code (`file.il`) — e.g. `push 3`, `pop r1`, `add r2, r1`, conditional jumps (`cmp`, `be`), loop labels, function labels, `call`, `ret`

**Error handler (`error.py`)**
Reports syntax errors with the current line number to `file.err` and halts compilation.

## Example

Input (`file.exp`):
```
void main()
begin
  x = 3 + 4 * 2;
  if (x) then
    x = x - 1;
end.
```

Generated intermediate language (`file.il`, excerpt):
```
main:
push 3
push 4
push 2
pop r1
pop r2
mul r2, r1
push r2
pop r1
pop r2
add r2, r1
push r2
pop x
push x
pop r2
cmp r2,0
be else
push x
push 1
pop r1
pop r2
sub r2, r1
push r2
pop x
else:
exit
```

## Project structure

```
.
├── main.py        # Entry point — opens output files, drives front end / back end
├── lexer.py        # Tokenizer
├── parser.py        # Recursive-descent parser + grammar rules
├── symbol.py        # Symbol table (identifiers, keywords)
├── emitter.py        # Code generation to IL and object trace
├── error.py        # Syntax error reporting
├── file.exp        # Sample input program
├── file.il        # Generated intermediate language (output)
├── file.obj        # Generated object trace (output)
└── file.err        # Syntax error log (output)
```

## Running it

```bash
python main.py
```

Reads `file.exp`, and writes `file.il`, `file.obj`, and `file.err`.

## What this demonstrates

- Hand-written lexical analysis (regex-based tokenization)
- Recursive-descent parsing and grammar design for a small procedural language
- Symbol table design for identifiers and keywords
- Intermediate code generation (stack-based IL) including control flow (conditionals, loops) and function calls
- Clean separation of compiler phases (lexer / parser / symbol table / emitter / error handling)

## Possible extensions

- AST construction instead of direct emission
- A back-end that translates the IL to real assembly or bytecode
- Type checking and scoping rules
- Function parameters and return values
- `else` branch support for conditionals

---
Built as a learning project to understand how compilers work end-to-end, from characters to executable intermediate code.
