import pdb

def add_numbers(a, b):
    result = a + b
    pdb.set_trace()  # Set a breakpoint
    return result

add_numbers(2, 3)