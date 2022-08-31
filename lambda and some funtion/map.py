"""
 In advance python, we are use map,filter and reduce with code 
"""

""" ****************** MAP *********************"""
def square(num):
    return num * num 

l = [1,2,4]

# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print (l2)

# Method 2 

print(list(map(square,l)))


""" ****************** FILTER *********************"""

def greater_then_5(num):
    if num > 5 :
        return True
    else:
        return False

l = [1,2,3,4,5,6,7,9,33,22,12]
print(list(filter(greater_then_5,l)))

l2 = lambda num:num > 10
print(list(filter(l2,l)))


""" ****************** REDUCE *********************"""

from functools import reduce



