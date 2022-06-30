#!/usr/bin/python3
if __name__ == "__main__":
    
    from calculator_1 import add as sum, sub as diff, mul as dup, div as res
    from sys import argv, exit
    ops = ['+', '-', '*', '/']
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end='\n')
        exit(1)
        
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if operator == ops[0]:
        result = sum(a, b)
    elif operator == ops[1]:
        result = diff(a, b)
    elif operator == ops[2]:
        result = dup(a, b)
    elif operator == ops[3]:
        result = res(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /", end='\n')
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
    
        
    
    
