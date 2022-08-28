a = 21 # Global variable

def fun1():
    global a
    print(f"Global variable: {a}")
    a1= 8  # Local variable
    print(f"Local variable: {a1}")



"""
local scope only print local variable 
if variable name is same and your use global variable then use keyword is global
"""

fun1()
print(f"chack scope value :{a}")