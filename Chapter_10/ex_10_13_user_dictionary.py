from pathlib import Path
import json

path = Path('chapter_10/data_user_dictionary.json')

def get_stored_info():
    """Retrieves and prints the stored information."""
    if path.exists():
        return json.loads(path.read_text())
    else:
        return None

def get_new_info(info):
    """Prompts the user for information about themselves."""
    user_info = {}
    for key in info:
        user_info[key] = input(f"What is your {key}? ")
    
    path.write_text(json.dumps(user_info))
    return user_info

def user_information():
    """
    If information has been inputted, it prints a summary of the user.
    If no information has been inputted, it asks the user for their information.
    """
    user_info = get_stored_info()

    if user_info:
        print(f"Here is everything we know about {user_info['name']}:")
        for key, info in user_info.items():
            print(f" - {key.title()}: {info}")
    else:
        user_info = get_new_info(['name', 'age', 'favorite color'])
        print(f"\nI'll make sure to remember you {user_info['name']}!")


user_information()