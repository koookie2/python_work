def make_shirt(size='large', text='I love Python'):
    """Displays the size and text of a shirt"""
    print(f"\nThe size of this T-shirt is {size.title()}.")
    print(f"The text on this T-shirt is {text.title()}.")

make_shirt('large')
make_shirt('medium')
make_shirt(text='Hello World')