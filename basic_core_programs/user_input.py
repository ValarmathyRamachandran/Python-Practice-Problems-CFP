def user_function():
    user_input = input("Please enter your Name: ")

    if len(user_input) > 2:
        print("Hello " + user_input + ", How are you? ")
    else:
        print("please enter atleast 3 characters")


user_function()
