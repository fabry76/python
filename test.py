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
    if value > 0:
        return f"\nThere are {value*60} minutes in {value} hours."
    else value == 0:
        return("\nYou've entered a zero.")
   
def check_int(value):
    if value.isdigit():
        var = int(value)
        min = calculate(var)
        print(min)
    else:
        print("\nYou have not entered an Integer number.")

clear_screen()
print("This program will return the number of minutes in (x) hours.\n")
hours = input("Enter the number of hours:\n")
check_int(hours)