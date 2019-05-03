import ast


def traverse(node):
    if isinstance(node, ast.FunctionDef):
        print("Func Declare:\t" + node.name)
        print()
        for child in node.body:
            traverse(child)

    elif isinstance(node, ast.Assign):
        print(lines[node.lineno])
        print(ast.dump(node))
        print()


with open("target/romanToInt.py", "r") as source:
    code = source.read()
tree = ast.parse(code)
lines = [None] + code.splitlines()  # None at [0] so we can index lines from 1
test_namespace = {}

for node in tree.body:
    wrapper = ast.Module(body=[node])
    print()
    print(node.lineno)
    print(lines[node.lineno])
    #print(ast.dump(node))

    traverse(node)
    try:
        co = compile(wrapper, "<ast>", 'exec')
        exec(co, test_namespace)
    except AssertionError:
        print("Assertion failed on line", node.lineno, ":")
        print(lines[node.lineno])
        # If the error has a message, show it.
        if e.args:
            print(e)
        print()
