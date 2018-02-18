def list_sum(ls):
    lsum = 0
    if len(ls) == 1:
        return ls[0]
    else:
        lsum = ls[0] + list_sum(ls[1:])
    return lsum

print list_sum([1,2,3,4,5,6,7,8,9])
