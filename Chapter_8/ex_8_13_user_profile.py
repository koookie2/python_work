def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last-name'] = last
    return user_info

user_profile = build_profile('kavin', 'wesley',
                             grade=9,
                             age=15,
                             siblings=1)

print(user_profile)