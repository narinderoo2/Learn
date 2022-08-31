while (True):
    try:
        a = int(input("Enter  table number :"))
        b = [a*i for i in range(1, 11)]
        print(f"{a} == {b}")

        """
        Store mutilple table in text file """

        with open("table.txt","a") as f:
            f.write(str(f"{a} table = {b}"))
            f.write('\n')


    except Exception as e:
        print(e)
        break
