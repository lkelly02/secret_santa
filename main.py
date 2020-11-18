import random

# gift_giver = ["Lucas", "Andrea", "Ted", "Sheila", "Jake", "Katlyn", "Brandan", "Kayla"]
# recipient = [family1, family2, family3, family4]

family1 = ["Lucas", "Andrea"]
family2 = ["Ted", "Sheila"]
family3 = ["Jake", "Katlyn"]
family4 = ["Brandan", "Kayla"]

families = [family1, family2, family3, family4]
recipient = ["Lucas", "Andrea", "Ted", "Sheila", "Jake", "Katlyn", "Brandan", "Kayla"]


chosen_gift_giver = []
chosen_recipient = []

while len(recipient) > 0 and (len(chosen_gift_giver) and len(chosen_recipient)) < 8:
    for family in families:
        fam1 = family
        for name in fam1:
            if name not in chosen_gift_giver:
                rand1 = name
                rand2 = random.choice(recipient)
                if rand1 != rand2 and rand2 not in fam1:
                    chosen_gift_giver.append(rand1)
                    chosen_recipient.append(rand2)
                    recipient.remove(rand2)
                    print(f"{rand1} has {rand2}")
                else:
                    pass


