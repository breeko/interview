class Memoize:
    def __init__(self,f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

# Reverse a string
def reverse(s):
    return ''.join(list(reversed(s)))

def reverse2(s):
    s[::-1]
    
def revese(s):
    return ''.join([s[idx] for idx in range(len(s)-1,-1,-1)])
    
# Fibonacci
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

fib = Memoize(fib)

# Print out table
def print_table(num_rows, num_cols):
    max_i_size = len(str(num_rows*num_cols))
    i = 0
    for row in range(num_rows):
        for col in range(num_cols):
            print ('%d ' % i).rjust(max_i_size+1, ' '),
            i+=1
        print '\n',

def print_mult_table(max_num):
    table = [[i * j for i in range(1,10)] for j in range(1,10)]
    max_i_size = len(str(max_num**2))
    for row in table:
        for val in row:
            print ('%d' % val).rjust(max_i_size+1, ' '),
        print '\n',
        
from operator import mul

def n_choose_c(n,c):
    #  computes combination 
    # n! / ((n-r)! * r!)
    if c == 0:
        return 1
    elif c > n:
        return 0
    return reduce(mul, range(n, n-c, -1)) / reduce(mul, range(c, 0, -1))

# You have a staircase with N steps, and you can take any mixture of single and double steps
# to reach the top. How many different ways can you climb the staircase?
def count_steps(n):
    if n <= 2:
        return n
    return count_steps(n-1) + count_steps(n-2)

count_steps = Memoize(count_steps)

def count_steps2(n):
    max_twos = n // 2
    count = 0
    for num_twos in range(max_twos + 1):
        count += n_choose_c(n-num_twos, num_twos)
    return count

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None
        

def linked_list(l):
    prev = None
    head = None
    for item in l:
        node = Node(item)
        if head is None:
            head = node
        if prev:
            prev.nextNode = node
        node.prevNode = prev    
        prev = node
    return head

from random import random

def shuffle(l):
    n = len(l)
    for i in range(n):
        r = rand_between(0,n)
        l[i], l[r] = l[r], l[i]

def rand_between(lo, hi):
    """ returns random value between [lo, hi) """
    return int(random() * (hi - lo) + lo )
    
import sys

def max_sublist(l):
    best_so_far = -sys.maxint - 1
    stop_right_here = 0
    for val in l:
        stop_right_here = max(0, stop_right_here) + val
        best_so_far = max(best_so_far, stop_right_here)
    return best_so_far
    
def max_profit(l):
    sorted_l = sorted(l)
    max_prices = []
    for val in l:
        if val == sorted_l[-1]:
            sorted_l.pop()
        max_prices.append(sorted_l[-1])
        
    return max_prices

def max_profit2(l):
    n = len(l)
    daily_profit = [l[i+1] - l[i] for i in range(n=1)]
    return daily_profit

l = [3, 5, 2, 1, 9, 5, 3, 6]
# print max_profit(l)
pr

    

