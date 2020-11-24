import random

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

    for num in range(number_of_households):
        household = input("Enter names of household seperated by commas: ")
        list_of_households.append(household.split(", "))
        recipients += " ".join(household.split(", ")) + " "
    recipients = recipients.split()
    print(recipients)
    while len(recipients) > 0 and (len(chosen_gift_giver) and len(chosen_recipient)) < len(recipients):
        for household in list_of_households:
            for name in household:
                if name not in chosen_gift_giver:
                    rand1 = name
                    rand2 = random.choice(recipients)
                    if rand1 != rand2 and rand2 not in household:
                        chosen_gift_giver.append(rand1)
                        chosen_recipient.append(rand2)
                        recipients.remove(rand2)
                        print(f"{rand1} has {rand2}")
                    else:
                        pass

else:
    print("else")
    # number_in_game = int(
    #     input("How many total individuals are playing the game? "))
