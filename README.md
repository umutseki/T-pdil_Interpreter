# T-pdil_Interpreter
This project is an interpreter for a custom toy programming language called “Tüpdil,” implemented in Python. The interpreter reads a .tup input file, checks it for compile-time errors, executes valid instructions, and produces the corresponding output. It supports variable declarations, type checking, arithmetic expressions, jumps, printing, and runtime error handling according to the rules defined for the language. The interpreter also performs lexical validation, whitespace checks, and detailed error reporting, ensuring that both compile-time and runtime errors are caught accurately.
Requirements:
Python 3.8 or later
A valid .tup input file (e.g., input.tup)
No external libraries are required; the project uses only core Python features.
How to run:
Place input.tup and the Python interpreter script (e.g., tup_interpreter.py) in the same folder.
Run the interpreter with:
python3 tup_interpreter.py
After execution, the program will create an output.txt file containing either the final output or the corresponding error message.
The interpreter enforces all language rules, including type constraints, variable usage, expression validation, jump boundaries, and print operations. It is designed to closely follow the behavior described in the original project specification.
