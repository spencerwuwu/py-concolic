#!/usr/bin/env python3

import sys
import os

class Parameter:
    def __init__(self, name, p_type):
        self.name = name
        self.p_type = p_type
        #print("Type: \t" + name + ": "  + p_type)

def parse_type(line):
    content = line.split(":type ")[1]
    name = content.split(":")[0]
    p_type = content.split(": ")[1]
    if "List" in p_type:
        if p_type != "List[int]" and p_type != "List[str]":
            return None
    return Parameter(name, p_type)

def get_param_type(code):
    params = []
    for line in code.splitlines():
        if ":type" in line:
            param = parse_type(line)
            if param is None:
                return None
            params.append(param)
    return params

def get_function(code):
    function = []
    start_recording = 0
    for line in code.splitlines():
        if str.strip(line).startswith('#'):
            continue
        elif len(line) == 0:
            continue
        else:
            if start_recording is 1:
                if "if __name__ " in line:
                    break
                line = line.replace("self,", "")
                line = line.replace("self.", "")
                function.append(line[4:])
            else:
                if "def " in line:
                    start_recording = 1
                    line = line.replace("self,", "")
                    function.append(line[4:])
    return function


def replace_params(params, code):
    params_todo = []
    for param in params:
        if "List" in param.p_type:
            params_todo.append(param)

    new_def = code[0]
    in_no = 0
    for param in params_todo:
        in0 = "in" + str(in_no)
        in_no += 1
        in1 = "in" + str(in_no)
        in_no += 1
        new_def = new_def.replace(param.name , in0 + ", " + in1)
        code.insert(1, "    " + param.name + " = [" + in0 + ", " + in1 + "]")
        if "int" in param.p_type:
            params.append(Parameter(in0, "int"))
            params.append(Parameter(in1, "int"))
        else:
            params.append(Parameter(in0, "str"))
            params.append(Parameter(in1, "str"))
        params.remove(param)
    code[0] = new_def
    return code


def gen_pyex_code(function, params):
    code = []
    code.append("from symbolic.args import symbolic, concrete")

    for param in params:
        if param.p_type == "str":
            code.append("@symbolic(" + param.name + "=" + '\"abcdefg\")')

    for line in function:
        code.append(line)

    return code


def get_gencode(code):
    params = get_param_type(code)
    if params is None:
        return None

    function = get_function(code)
    function = replace_params(params, function)
    return gen_pyex_code(function, params)



def main(py):
    print(py)
    print("---")
    with open(py, "r") as source:
        code = source.read()
    gencode = get_gencode(code)
    if gencode is None:
        print("Can't do")
    else:
        for line in gencode:
            print(line)
    print("=========")



if __name__ == "__main__":
    dirs = os.listdir("leetcode_python/")
    for py in dirs:
        if ".py" in py:
            main("leetcode_python/" + py)
