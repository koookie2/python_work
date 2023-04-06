# Positional Arguments are a one to one correlation with parameters and their arguments
# Keyword Arguments are explicit ways to correlate parameters with their arguments
# Default Values for arguments are values that the function uses if no argument is for that parameter 
# Arbitrary Arguments are a tuple of dictionary parameter that can recive an unlimited amount of arguments 

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last-name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)