# code runner extension to make console output cleaner
from tkinter.tix import Tree


# natural numbers for n:
def get_natural_numbers(n):
    # sum() call depends on range(n+1) sequence. this expression depends on n therefore it's not constant operation; 
    # but some operations run constant times: return num
    return sum([i for i in range(n + 1)])


assert get_natural_numbers(5) == 15
assert get_natural_numbers(3) == 6

# asymptotic analysis - measure of growth in terms of input size
# constant operations - it doesn't depend on size of it's operand (i.e iteration depends on size of sequence, so it's not constant), run only given times and doesn't depend on n
