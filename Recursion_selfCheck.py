def str_rev(s):
    if len(s) == 1:
        return s
    else:
        return str_rev(s[1:]) + s[0]
#string reverse    
print str_rev('avs')

# palindrome check      
x = str(raw_input("enter to check palindrome "))
print x == str_rev(x)
x = raw_input("enter to check palindrome ")
print x == str_rev(x)
