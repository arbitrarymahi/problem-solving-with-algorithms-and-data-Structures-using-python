from Stack import Stack
        
def compare(top,sym):
    opens = '([{'
    closes = ')]}'
    
    return opens.index(top) == closes.index(sym)


def par_check1(symbol_str):
    s = Stack()
    Balanced = True
    pos = 0
    
    while pos<len(symbol_str) and Balanced:
         
        if symbol_str[pos] == "(":
            s.push("(")
        else:
            if s.is_empty():
                Balanced = False
            else:
                s.pop()
        pos += 1
    if Balanced and s.is_empty():
        return True
    else:
        return False
        
def par_check2(symbol_str):
    s1 = Stack()
    Balanced = True
    pos = 0
    
    while pos<len(symbol_str) and Balanced:
        sym = symbol_str[pos]
        if sym in  "{[(":
            s1.push(sym)
        else:
            if s1.is_empty():
                Balanced = False
            else:
                top = s1.pop()
                
                          
                if not compare(top,sym):
                    balanced = False
        pos += 1
    if Balanced and s1.is_empty():
        return True
    else:
        return False
         
print(par_check1('(()()()())'))
print(par_check1('(()()()()'))

print(par_check2('{()[{()}]}'))
print(par_check2('{()[{()]}'))




