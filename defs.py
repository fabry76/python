def clear_screen():
    import os
    ff = os.name
    if ff == "nt":
        os.system("cls")
        print(f"Your OS is Windows.\n")
    else:
        os.system("clear")
        print(f"Your OS is Linux.\n")

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