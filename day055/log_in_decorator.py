# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapped(*args):
        function_name = function.__name__
        print(f"You called {function_name}{args}")
        result = function(*args)
        print(f"It returned: {result}")
    return wrapped
        

# Use the decorator 👇

@logging_decorator
def sum(*args):
    result = 0
    for num in args:
        result += num
    return result

@logging_decorator
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result    
    
sum(1, 2, 3, 4)