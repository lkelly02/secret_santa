

print("Welcome to the Secret Santa name generator")
print("Let's start with a few questions:")

households_or_group = input(
    "Will this game be played with multiple households or one group? ").lower()

if households_or_group == "households":
    list_of_families = []
    recipients = ""

    number_of_households = int(input("How many households are in the game? "))
    number_in_game = int(
        input("How many total individuals are playing the game? "))

    for num in range(number_of_households):
        household = input("Enter names of household seperated by commas: ") + " "
        list_of_families.append(household.split(","))
        recipients += "".join(household.split(","))
    recipients = recipients.split()  
    print(recipients)
else:
    print("else")
    # number_in_game = int(
    #     input("How many total individuals are playing the game? "))
