def checkName(name):
    print(f"Good morning Sir, {name}")


"""
print(__name__) check current dictory 
only this dictory to n is working 
not working in other dictory
"""

if __name__ == "__main__":
    n = input("Enter a name \n")
    checkName(n)