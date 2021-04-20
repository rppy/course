while True:
    try:
        n = eval(input("Input an integer: "))
    except:
        print("An error occurred! Please try again!")
    else:
        break
print("Thank you, you number squared is: ", n ** 2)

