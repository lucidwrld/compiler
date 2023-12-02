
class Debugger:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.breakpoints = set()
        self.current_line = 0

    def set_breakpoint(self, line_number):
        self.breakpoints.add(line_number)

    def run(self, asts):
        for ast in asts:
            self.current_line = ast.line_number  # Assuming each AST node has a line number attribute
            if self.current_line in self.breakpoints:
                print(f"Breakpoint hit at line {self.current_line}")
                self.interact()
            self.interpreter.execute_node(ast)

    def interact(self):
        # Interactive shell for debugging
        # Can be expanded to inspect variables, step through code, etc.
        pass

# Example usage
# debugger = Debugger(interpreter_instance)
# debugger.set_breakpoint(line_number)
# debugger.run(asts)
