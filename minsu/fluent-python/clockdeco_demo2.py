# clockdeco_demo2.py
import time
from clockdeco2 import clock

@clock
def snooze(seconds):
    time.sleep(seconds)
    
@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
