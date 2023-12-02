from lexer import Lexer
from parser_1 import Parser
class Validator:
    def __init__(self, lexer, parser):
        self.lexer = lexer
        self.parser = parser

    def validate(self, source_code):
        # Lexical Analysis
        self.lexer = Lexer(source_code)
        tokens = self.lexer.getTokens()

        # Syntax Analysis
        self.parser = Parser(tokens)
        ast = self.parser.runParse()
        if ast is None:
            return False, "Syntax Error"

        # Semantic Analysis (can be expanded as needed)
        # Example: Check for undefined variables, type mismatches, etc.

        return True, "No errors detected"

# Example usage
# validator = Validator(lexer_instance, parser_instance)
# is_valid, message = validator.validate(source_code)
