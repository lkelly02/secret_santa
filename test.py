import random
import sys

print("Welcome to the Secret Santa name generator")
print("Let's start with a few questions:")

households_or_group = input(
    "Will this game be played with multiple households or one group? ").lower()

chosen_gift_giver = []
chosen_recipient = []

if households_or_group == "households":
    list_of_households = []
    recipients = ""

    number_of_households = int(input("How many households are in the game? "))
    # number_in_game = int(
    #     input("How many total individuals are playing the game? "))
    print(
        f"Enter the names of each individual in a household seperated by commas (repeat for each of the {number_of_households} households): ")
    for num in range(number_of_households):
        household = input("names: ")
        list_of_households.append(household.split(", "))
        recipients += " ".join(household.split(", ")) + " "
    recipients = recipients.split()
    while len(recipients) > 0:
        for household in list_of_households:
            for name in household:
                if name not in chosen_gift_giver:
                    random_recipient = random.choice(recipients)
                while name == random_recipient or random_recipient in household:
                    random_recipient = random.choice(recipients)
                    if len(recipients) == 1 and recipients == [name]:
                        print("The code cannot be completed, please try again.")
                        sys.exit(0)
                if name != random_recipient and random_recipient not in household:
                    chosen_gift_giver.append(name)
                    chosen_recipient.append(random_recipient)
                    recipients.remove(random_recipient)
                    print(f"{name} has {random_recipient}")
                    print(" ")
else:
    print("else")
    # number_in_game = int(
    #     input("How many total individuals are playing the game? "))
