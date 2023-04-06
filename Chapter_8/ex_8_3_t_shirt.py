def make_shirt(size, text):
    """Displays the size and text of a shirt"""
    print(f"\nThe size of this T-shirt is {size.title()}.")
    print(f"The text on this T-shirt is {text.title()}.")

make_shirt('medium', 'Hello World')
make_shirt(size='medium', text='Hello World')