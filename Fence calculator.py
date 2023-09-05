print()
print("**** Welcome to the fence cost calculator ****")
print()

error = "Please enter a number more than zero"
error_int = "Please enter a number"

again = ""
while again == "":

    loop_1 = False
    while not loop_1:
        try:
            width = float(input("Please input width of fence (must be number): "))
            if width > 0:
                loop_1 = True
            else:
                print()
                print(error)
                print()
        except ValueError:
            print()
            print(error_int)
            print()

    loop_2 = False
    while not loop_2:
        try:
            length = float(input("Please input length of fence (must be number): "))
            if length > 0:
                loop_2 = True
            else:
                print()
                print(error)
                print()
        except ValueError:
            print()
            print(error_int)
            print()

    loop_3 = False
    while not loop_3:
        try:
            cost_per_metre = float(input("please enter how much a fence costs per metre: $"))
            loop_3 = True
        except ValueError:
            print()
            print(error_int)
            print()

    perimeter = (2 * width) + (2 * length)
    cost = (2 * width) + (2 * length) * cost
    print()
    print("The Perimeter of your fence is {}m".format(perimeter))
    print("The cost for your fence is ${}".format(cost))
    print()

    again = input("press <enter> to rerun, any other key to end: ")

print()
print("Thank you for using the fence cost calculator")
