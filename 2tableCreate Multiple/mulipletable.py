while (True):
    try:
        a = int(input("Enter  table number :"))
        b = [a*i for i in range(1,11) ]
        print (f"{a} == {b}")
    except Exception as e:
        print(e)
        break