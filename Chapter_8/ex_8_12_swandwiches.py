def make_sandwich(*ingredients):
    """Show the ingredients on the swandwich we are about to make."""
    print("\nThe following are ingredients in this sandwich")
    for ingredient in ingredients:
        print(f" - {ingredient}")

make_sandwich('cheese')
make_sandwich('cheese', 'chicken')
make_sandwich('cheese', 'chicken', 'turkey')