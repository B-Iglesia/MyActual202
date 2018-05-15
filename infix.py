#comment
from stack import *
""" Create a precedence where * / have the highest, + - have middle, ( ) have the lowest
this problem requires two stacks to be created
an operator stack
an operand stack
follow the procedures outlined in the text book
EZ PZ"""
def operate(op, ops, opand):
    if op == "(":
        ops.push(op)
        return
    while precedence(op) <= precedence(ops.top()):
        topOp = ops.pop()
        if topOp == "+" or topOp ==  "-" or topOp == "*" or topOp == "/":
            a = str(opand.pop())
            b = str(opand.pop())
            c = eval(b+topOp+a)
            opand.push(c)
        if topOp == "(":
            return
    
    ops.push(op)
    return


def precedence(op):
    if op == "*" or op == "/":
        return 1
    elif op == "+" or op == "-":
        return 0
    return -1


def eval_infix(ex):
    l = ex.split()
    operators = Stack()
    operands = Stack()
    
    operators.push("(")
    
    for item in l:
        if item == "*" or item == "/" or item == "+" or item == "-" or item == "(" or item == ")":
            operate(item, operators, operands)
        try:
            operands.push(float(item))
        except ValueError:
            continue
    operate(")",operators,operands)
    return operands.pop()

def main():
    ex = input("Please enter an infix expression: ")
    
    result = eval_infix(ex)
    print("The result of", ex, "is", result)
    
if __name__ == "__main__":
    main()
#LOL I finished this thing waaaaay to fast, and I also made like 0 commits
#So here is another comment so that I have another commit