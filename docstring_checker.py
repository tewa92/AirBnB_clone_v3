#!/usr/bin/env python3
import ast

class DocstringChecker(ast.NodeVisitor):
    def __init__(self, file_path):
        self.file_path = file_path
        self.missing_docstrings = []

    def check_file(self):
        with open(self.file_path, "r") as file:
            tree = ast.parse(file.read())
        self.visit(tree)
        return self.missing_docstrings

    def visit_Module(self, node):
        if not ast.get_docstring(node):
            self.missing_docstrings.append(("Module", ""))
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        if not ast.get_docstring(node):
            self.missing_docstrings.append(("Class", node.name))
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if not ast.get_docstring(node):
            self.missing_docstrings.append(("Function", node.name))
        self.generic_visit(node)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python docstring_checker.py <python_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    checker = DocstringChecker(file_path)
    missing_docstrings = checker.check_file()

    if missing_docstrings:
        print("The following elements are missing docstrings:")
        for element_type, name in missing_docstrings:
            print(f"{element_type}: {name}")
    else:
        print("All modules, classes, and functions are well-documented.")
