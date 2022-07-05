import numba
from functools import wraps
from time import time

def timing(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        ts = time()
        result = func(*args, **kwargs)
        te = time()
        print(f"fun: {func.__name__}, args: [{args}, {kwargs}] took: {te-ts} sec")
        return result
    return wrap

@timing
@numba.jit(nopython=True)
def expmean_jut(rea):
    """
    Calculate average value
    """
    val = rea.mean()**2
    return val

