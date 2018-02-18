from Stack import Stack

def type_ch(x):
    try:
        int(x)
        return True
    except:
        return False

def infixToPostfix(infix_expr):
    postfix_str = []
    token_list = infix_expr.split() #for input string with spaces-separated-characters
#    token_list =list(infix_expr) #for input string without spaces-separated-characters **all or some chars**
    #doesn't work with numbers over 9 since 
    #they have more than one character
    #print(token_list)
    while ' ' in token_list:
        token_list.remove(' ')
    
    op_stack = Stack()
    op_prec = {'^' : 4,
            '*' : 3, '/' : 3,
            '+' : 2, '-' : 2,
            '(' : 1   }
    
    for token in token_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or \
           type_ch(token):
            postfix_str.append(token)
              
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top = op_stack.pop()
            while top != '(':
                 postfix_str.append(top) 
                 top = op_stack.pop()
        else:
            while not (op_stack.is_empty()) and \
                     (op_prec[token] <= op_prec[op_stack.peek()]):
                postfix_str.append(op_stack.pop())
            op_stack.push(token)
        
    while not(op_stack.is_empty()):
        postfix_str.append(op_stack.pop())
    return str(' '.join(postfix_str)) #return postfix with spaces
#    return str(''.join(postfix_str)) #return postfix without spaces

#print(infixToPostfix("15 * 3 ^ ( 4 - 2 )")) 
"""print(infixToPostfix("(A + B ) ^ X * ( C +  D )"))
print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))  #string without spaces
print(infixToPostfix("A * B + C * D"))  #string with spaces
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print infixToPostfix("( A + B ) * ( C + D )") 
print infixToPostfix("( A + B ) * C")
print infixToPostfix("A + B * C")
print infixToPostfix("1 + 2 * 3 / ( 3 - 5 )")
print infixToPostfix(" 1 + 3 * 5 / ( 6 - 4 )")
"""
