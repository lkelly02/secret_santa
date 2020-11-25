import random
import sys

# # The idea for the family variables, are that they can be created by the user for as many families and family memebers as they want.
# # Not sure how to do this yet.

family1 = ["Lucas", "Andrea"]
family2 = ["Ted", "Sheila"]
family3 = ["Jake", "Katlyn"]
family4 = ["Brandan", "Kayla"]

families = [family1, family2, family3, family4]
recipients = ["Lucas", "Andrea", "Ted", "Sheila",
              "Jake", "Katlyn", "Brandan", "Kayla"]


chosen_gift_giver = []
chosen_recipient = []

   
while len(recipients) > 0:
    for family in families:
        fam1 = family
        for name in fam1:
            if name not in chosen_gift_giver:
                rand2 = random.choice(recipients)
                while name == rand2 or rand2 in fam1:
                    rand2 = random.choice(recipients)
                    if len(recipients) == 1 and recipients == [name]:
                        print("The code cannot be completed, please try again.")
                        sys.exit(0)
                if name != rand2 and rand2 not in fam1:
                    chosen_gift_giver.append(name)
                    chosen_recipient.append(rand2)
                    recipients.remove(rand2)
                    print(f"{name} has {rand2}")

