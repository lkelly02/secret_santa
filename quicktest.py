# This file is a quick way to test some of the code in a shorter version than the main file. Run in the terminal.


import random
import sys
import os

# Clear function is used to clear out the terminal when the the code cannot be completed due to the remaining recipient(s) is either
# the same as gift giver, or in the same household as the gift giver.


def clear():
    os.system("clear")

# The user will be entering each name in a single household.
household1 = ["Lucas", "Andrea"]
household2 = ["Ted", "Sheila"]
household3 = ["Jake", "Katlyn"]
household4 = ["Brandan", "Kayla"]

list_of_households = [household1, household2, household3, household4]
# The entries that the user enters, will also be entered into the recipients list.
recipients = ["Lucas", "Andrea", "Ted", "Sheila",
              "Jake", "Katlyn", "Brandan", "Kayla"]


chosen_gift_giver = []
chosen_recipient = []


while len(recipients) > 0:
    for household in list_of_households:
        for name in household:
            if name not in chosen_gift_giver:
                random_recipient = random.choice(recipients)
                while name == random_recipient or random_recipient in household:
                    if recipients == [name, random_recipient] or recipients == [name] or (len(recipients) == 1 and recipients[0] in household):
                        recipients.extend(chosen_recipient)
                        chosen_gift_giver = []
                        chosen_recipient = []
                        clear()
                    random_recipient = random.choice(recipients)
                if name != random_recipient and random_recipient not in household:
                    chosen_gift_giver.append(name)
                    chosen_recipient.append(random_recipient)
                    recipients.remove(random_recipient)
                    print(f"{name} has {random_recipient}")
