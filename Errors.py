def ask():
    while True:
        try:
            x = int(input("Type in a number: "))
        except ValueError:
            print("something went wrong")
            continue
        else:
            print("It is ok now")
            break
        finally:
            print("All cool")
    print(x**2)
ask()