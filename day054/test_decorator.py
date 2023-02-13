# Given the above information, complete the code exercise by 
# printing out the speed it takes to run the fast_function() 
# vs the slow_function(). You will need to complete the 
# speed_calc_decorator() function.


import time

def speed_calc_decorator(function):
    def speed():
        start_time = time.time()
        function()
        end_time = time.time()
        duration = end_time - start_time
        function_name = function.__name__ 
        print(f"Operation time for {function_name} is: {duration:.3f} s")
    return speed
        
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i
        
fast_function()
slow_function()