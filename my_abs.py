import math
import numbers

def my_abs(x):
    try:
        
        if x < 0:
            return -x
        else:
            return x
    elif isinstance(x, numbers.Complex):
        return math.sqrt(x.real ** 2 + x.imag ** 2)
    else:
        return math.nan
    
def my_almost_eq(x, y):
    if my_abs(x -y ) < 1e-16:
        return True
    else:
        return False
