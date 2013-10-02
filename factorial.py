import doctest


def factorial(n):
    '''Given a number returns it's factorial e.g. factorial of 5 is 5*4*3*2*1
    
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    '''
    if not type(n) == int:
        raise Exception("Input to factorial() function must be an integer")
    if n < 0:
        raise Exception("Factorial for negative numbers is not defined")
    
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total
    

def fibonacci(n):
    '''Returns the Nth value in the Fibonacci
    sequence
    
    F(N) = F(N-1) + F(N-2)
    F(0) = 0, F(1) = 1
    
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    '''
    assert n >= 0
    assert isinstance(n, int)
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a
    
if __name__ == "__main__":
    doctest.testmod()
