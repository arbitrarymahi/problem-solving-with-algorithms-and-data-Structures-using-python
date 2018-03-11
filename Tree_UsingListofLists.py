def binary_tree(n):
    return [n,[],[]]

def insert_left(root,new_value):    
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[new_value,t,[]])
    else:   
        root.insert(1,[new_value,[],[]])
    return root
        
def insert_right(root,new_value):    
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[new_value,[],t])
    else:   
        root.insert(2,[new_value,[],[]])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val
    
def get_left_child(root):
    return root[1]
    
def get_right_child(root):
    return root[2]
    
def build_tree():
    x = binary_tree('a')
    insert_left(x,'b')
    insert_right(x,'c')
    insert_right(get_left_child(x),'d')
    insert_left(get_right_child(x),'e')
    insert_right(get_right_child(x),'f')
    return x

print(build_tree())
"""
x = binary_tree('a')
insert_left(x,'b')
insert_right(x,'c')
print x
insert_right(get_right_child(x), 'd')
print x
insert_left(get_right_child(get_right_child(x)), 'e')    
print x

# another tree  
r = binary_tree(3)
print(r)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
print(r)
l = get_left_child(r)
print(l)
set_root_val(l, 9)
print(r)
insert_left(l, 11)
print(r)
print(get_right_child(get_right_child(r)))"""
