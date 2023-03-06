guest_list = ["Albert Einstein", "Jesus", "Donald Trump"]
print(f"I would like to invite you, {guest_list[0]}, to dinner!")
print(f"I would like to invite you, {guest_list[1]}, to dinner!")
print(f"I would like to invite you, {guest_list[2]}, to dinner!")

print("\nI have found a bigger table for the dinner!\n")

guest_list.insert(0, "Max Planck")
guest_list.insert(3, "Saint Peter")
guest_list.append("Barack Obama")
print(f"I would like to invite you, {guest_list[0]}, to dinner!")
print(f"I would like to invite you, {guest_list[1]}, to dinner!")
print(f"I would like to invite you, {guest_list[2]}, to dinner!")
print(f"I would like to invite you, {guest_list[3]}, to dinner!")
print(f"I would like to invite you, {guest_list[4]}, to dinner!")
print(f"I would like to invite you, {guest_list[5]}, to dinner!")

print(f"\nOh no, the larger table won't arrive in time for the dinner, and I can only invite 2 people to the dinner!\n")

print(f"Sorry {guest_list.pop()}, you are uninvited to the dinner!")
print(f"Sorry {guest_list.pop()}, you are uninvited to the dinner!")
print(f"Sorry {guest_list.pop()}, you are uninvited to the dinner!")
print(f"Sorry {guest_list.pop()}, you are uninvited to the dinner!")
print(f"\n{guest_list[0]} and {guest_list[0]}, you are still invited to the dinner!")
del guest_list[0], guest_list[0]
print(guest_list)