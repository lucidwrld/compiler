from lexer import *
from parser_1 import *
from interpreter import *

from validator import Validator
from debugger import Debugger
import sys

def main():
    source = sys.argv[1]
    new_lexer = Lexer(source)

    tokens = new_lexer.getTokens()
    new_parser = Parser(tokens)
    
    validator = Validator(new_lexer, new_parser)
    is_valid, message = validator.validate(source)
    if not is_valid:
        print(f"Validation Error: {message}")
        return
    else:
        asts = new_parser.runParse()
        debug_mode = "--debug" in sys.argv
        new_interpreter = Interpreter(asts)
        if debug_mode:
            debugger = Debugger(new_interpreter)
            # Set breakpoints as needed, e.g., debugger.set_breakpoint(5)
            debugger.run(asts)
        else:
            new_interpreter.execute()

main()