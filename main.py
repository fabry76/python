#imports
from defs import clear_screen
from defs import check_int
import vars as v


user_input = ""

clear_screen()
while user_input != "exit":
    print(v.initial_statement)
    user_input = input(v.input_by_user)
    hours = user_input.split(",")
    for i in set(hours):
        check_int(i)
