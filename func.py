def clear_screen():
    import os
    ff = os.name
    if ff == "nt":
        os.system("cls")
        print(f"Your OS is Windows.\n")
    else:
        os.system("clear")
        print(f"Your OS is Linux.\n")