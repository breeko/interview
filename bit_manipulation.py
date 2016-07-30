def get_bit(num, i):
    """ returns ith bit in num """
    return num & (1 << i) != 0
    
def set_bit(num, i):
    """ sets the ith bit in num to 1 """
    return num | (1 << i)
