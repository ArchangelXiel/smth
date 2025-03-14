import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
        return math.sqrt(number)

        num = 25100
        delay_ms = 2123
        result = delayed_sqrt(num, delay_ms)
        print(f"Square root of {num} after {delay_ms} milliseconds is {result}")