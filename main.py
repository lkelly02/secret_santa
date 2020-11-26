import random
import sys
import time
import os


def clear():
    os.system("clear")


print("Welcome to the Secret Santa name generator")
print("Let's start with a few questions:")

households_or_group = input(
    "Will this game be played with multiple households or one group?(households/group) ").lower()

chosen_gift_giver = []
chosen_recipient = []

if households_or_group == "households":
    list_of_households = []
    recipients = ""

    number_of_households = int(input("How many households are in the game? "))
    print(
        f"Enter the names of each individual in a household seperated by commas (repeat for each of the {number_of_households} households): ")
    for num in range(number_of_households):
        household = input("names: ")
        list_of_households.append(household.split(", "))
        recipients += " ".join(household.split(", ")) + " "
    recipients = recipients.split()
    print("Okay, here we go...")
    time.sleep(3)
    while len(recipients) > 0:
        for household in list_of_households:
            for name in household:
                if name not in chosen_gift_giver:
                    random_recipient = random.choice(recipients)
                while name == random_recipient or random_recipient in household:
                    random_recipient = random.choice(recipients)
                    if recipients == [name, random_recipient] or recipients == [name] or (len(recipients) == 1 and recipients[0] in household):
                        recipients.extend(chosen_recipient)
                        chosen_gift_giver = []
                        chosen_recipient = []
                        clear()
                if name != random_recipient and random_recipient not in household:
                    chosen_gift_giver.append(name)
                    chosen_recipient.append(random_recipient)
                    recipients.remove(random_recipient)
                    print(f"{name.title()} has {random_recipient.title()}")
elif households_or_group == "group":
    individuals_names = input(
        "Please enter each inividuals name, seperated by a comma and a space: ")
    list_of_individuals = individuals_names.split(", ")
    number_of_individuals = len(list_of_individuals)
    ans = input(
        f"You entered {number_of_individuals} names, is this the correct number of individuals playing? (yes/no) ").lower()
    if ans == "no":
        print("Sorry, please play again re-enter the names")
        sys.exit(0)
    recipients = individuals_names.split(", ")
    print("Okay, here we go...")
    time.sleep(3)
    while len(recipients) > 0:
        for name in list_of_individuals:
            if name not in chosen_gift_giver:
                random_recipient = random.choice(recipients)
            while name == random_recipient:
                random_recipient = random.choice(recipients)
                if recipients == [name, random_recipient] or recipients == [name]:
                    recipients.extend(chosen_recipient)
                    chosen_gift_giver = []
                    chosen_recipient = []
                    clear()
            if name != random_recipient:
                chosen_gift_giver.append(name)
                chosen_recipient.append(random_recipient)
                recipients.remove(random_recipient)
                print(f"{name.title()} has {random_recipient.title()}")
else:
    print("Invalid entry")
