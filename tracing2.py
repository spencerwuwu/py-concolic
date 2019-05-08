
import sys
import ast


lines = []

def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    #print('  %s line %s' % (func_name, line_no))
    if line_no < len(lines) and "def " in lines[line_no]:
        func_name = str.strip(lines[line_no])
        print(func_name + "\t" + filename)
        #print('%s' % lines[line_no])

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    #print('Call to %s on line %s of %s' % (func_name, line_no, filename))
    if ".py" in filename:
        with open(filename, "r") as source:
            code = source.read()
        global lines
        lines = [None] + code.splitlines()  # None at [0] so we can index lines from 1
        return trace_lines


    """
    if func_name in TRACE_INTO:
        # Trace into this function
        return trace_lines
    """
    return

import urllib3

"""
with open("target/romanToInt.py", "r") as source:
    code = source.read()
lines = [None] + code.splitlines()  # None at [0] so we can index lines from 1
"""

TRACE_INTO = ['romanToInt']
sys.settrace(trace_calls)
http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r.data)
