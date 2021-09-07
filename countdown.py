import datetime
user_input = input("Please enter your goal with a deadline separated by a colon\n")
input_list= user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

dat = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.datetime.today()
time_until = dat - today

print(f"The time left to your {goal} goal is: {time_until.days} days")
