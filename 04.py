import time
import math

def delayed_sqrt(num, delay):
    time.sleep(delay / 1000) 
    result = math.sqrt(num)
    print(f"Square root of {num} after {delay} milliseconds is {result}")

num = 25100
delay = 2123
delayed_sqrt(num, delay)