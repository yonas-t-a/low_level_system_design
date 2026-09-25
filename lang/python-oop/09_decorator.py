import functools
import time

def friendly_decorator(func):
    def wrapper(*args, **kwargs):
        """
            This is a wrapper function that add a friendly messages.
        """
        print("Calling the function...")
        result = func(*args, **kwargs)
        print("Thank you for using the function")
        return result
    return wrapper


def friendly_decorator_2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
            This is a wrapper function that add a friendly messages.
        """
        print("Calling the function...")
        result = func(*args, **kwargs)
        print("Thank you for using the function")
        return result
    return wrapper



def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsd_time = end_time - start_time
        
        print(f"{func.__name__} has take {elapsd_time}")
        return result
    return wrapper
    

@friendly_decorator
@time_decorator
def say_hello():
    print("Hello decorator")
    
@friendly_decorator_2
@time_decorator
def theFirstTenNUmbers():
    """
        This if the function that prints 
        the first 10 natural numbers
    """
    
    for i in range(1, 11):
        print(i)

if __name__ == "__main__":
    say_hello()
    print(say_hello.__name__)
    print(say_hello.__doc__)
    print("+++++++++")
    theFirstTenNUmbers()
    print(theFirstTenNUmbers.__name__)
    print(theFirstTenNUmbers.__doc__)