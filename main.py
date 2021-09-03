def calculate(value):
    return f"\nThere are {value*60} minutes in {value} hours.\n"
      
def check_int(value):
    if value == "exit" or value == "Exit":
        exit()
    else:
        try:
            var = int(value)
            if var >= 0:
                calc = calculate(var)
                print(calc)
        except:
            print("\nYou have not entered an Integer number.\n")

user_input = ""

import func
func.clear_screen()
while user_input != "exit":
    print("This program will return the number of minutes in (x) hours.\n")
    user_input = input("Enter the number of hours:\n(Multiple entries comma separated)\n")
    hours = user_input.split(",")
    for i in set(hours):
        check_int(i)
        
        