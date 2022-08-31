"""
function created using an expression using lambda keyword
it is using with lambda keyword 
lambda funtion can be used as a normal function 
"""

# def fun(a):
#     return a + 5

fun = lambda a:a+5
multiplication = lambda a:a*a
sumData = lambda a,b,c:a+b+c

x = 55
print(fun(x))
print(multiplication(x))
print(sumData(x,2,2))