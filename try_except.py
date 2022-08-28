from re import I


while (True):
    print("press q to quit")
    a = input("Enter your number:-")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6:
            print("Please enter more then 6 ")
    except Exception as e:
        print(f"Error is not handle {e}")

print("thanks for game")



'''
try and except, we are creating new exception handle 
we are create new funtion like error handle

    def (value):
        try:
            a = value
            return int(a) + 1
        except:
            raise ValueError("THis is not good ")

'''
# while (True):
#     try:
#         a = int(input("Enter your number "))
#         if a=='q':
#             break
#         c = 1/a
#     except ValueError as e:
#         print("Make sure a valid value")
#     except ZeroDivisionError as e:
#         print(f"Make sure you are not divided by 0 {e}")


# print ("thankes ")


'''
We are useing try excep with else 
else is only work with try 
else is not working for except
'''

try:
    i = int(input("Enter number ( While loop is not working)"))
    c = 1/i
except Exception as e :
    print(f"Without loop {e}")
else:
    print("we are succesfully")



"""
try and except use with finally 
finally is wroking after the exit() programe
"""

try:
    i = int(input("Enter number ( While loop is not working)"))
    c = 1/i
except Exception as e :
    print(f"Without loop {e}")
    exit()
finally:
    print("Finally is working after exit() programe")

print("Program is exit()")

