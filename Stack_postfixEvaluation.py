from Stack import Stack
from Stack_infixToPostfix import infixToPostfix



def evaluateFunc(op,op1,op2):
    res = 0
    if op == '+':
        res = op1 + op2
    elif op == '-':
        res = op1 - op2
    elif op == '/':
        res = op1 / op2
    elif op == '*':
        res = op1 * op2
    elif op == '^':
        res = op1**op2
    return res

def postfixEval(postfix_str):
    postfix_list = postfix_str.split()  #postfix string including spaces
#    postfix_list = list(postfix_str)  #postfix string without spaces
    op_stack = Stack()
    op1,op2 = 0,0
    
    for token in postfix_list:
        
        if type_ch(token):
            op_stack.push(token)
                      
        else:
           op2 = int(op_stack.pop())
           op1 = int(op_stack.pop())
           op_stack.push(evaluateFunc(token,op1,op2))
   
    return op_stack.pop()

def type_ch(x):
    try:
        int(x)
        return True
    except:
        return False
  
#x = infixToPostfix("10 + 10 * 5 / ( 26 - 1 )")
x = infixToPostfix("5 * 3^(4 - 2)")

print(postfixEval(x))


