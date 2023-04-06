current_users = ['Sashi', 'Swarnim', 'Anvitha', 'Mahi', 'Ananya']
for x in range(len(current_users)):
     current_users[x] = current_users[x].lower()

new_users = ['Sashi', 'Swarnim', 'Eric', 'Henry', 'Sahil']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("That user name has already been taken! Please enter a different username.")
    else:
        print("That user name is available!")