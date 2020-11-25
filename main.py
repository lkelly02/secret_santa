import random
import sys

# # The idea for the family variables, are that they can be created by the user for as many families and family memebers as they want.
# # Not sure how to do this yet.

household1 = ["Lucas", "Andrea"]
household2 = ["Ted", "Sheila"]
household3 = ["Jake", "Katlyn"]
household4 = ["Brandan", "Kayla"]

list_of_households = [household1, household2, household3, household4]
recipients = ["Lucas", "Andrea", "Ted", "Sheila",
              "Jake", "Katlyn", "Brandan", "Kayla"]


chosen_gift_giver = []
chosen_recipient = []


while len(recipients) > 0:
    for household in list_of_households:
        for name in household:
            if name not in chosen_gift_giver:
                rand2 = random.choice(recipients)
                while name == rand2 or rand2 in household:
                    rand2 = random.choice(recipients)
                    if len(recipients) == 1 and recipients == [name]:
                        print("The code cannot be completed, please try again.")
                        sys.exit(0)
                if name != rand2 and rand2 not in household:
                    chosen_gift_giver.append(name)
                    chosen_recipient.append(rand2)
                    recipients.remove(rand2)
                    print(f"{name} has {rand2}")
