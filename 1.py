import random
import numpy as np

deck = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
otherdeck = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(deck)
random.shuffle(otherdeck)
print("Ur deck" + str(deck))
print("NPC'S deck" + str(otherdeck))
last_element = deck[-1]
last_element2 = deck[-2]
last_element3 = otherdeck[-1]
last_element4 = otherdeck[-2]
print("Ur last two cards " + str(last_element), end=" ")
print(last_element2)
print("NPC's last two cards " + str(last_element3) , end=" ")
print(last_element4)
