"""


"""
def checkFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read(),'file is show')
    except FileNotFoundError:
        print(f"File {filename} is not found")

checkFile("one.txt")
checkFile("two.txt")
checkFile("three.txt")