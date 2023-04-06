# Positional Arguments are a one to one correlation with parameters and their arguments
# Keyword Arguments are explicit ways to correlate parameters with their arguments
# Default Values for arguments are values that the function uses if no argument is for that parameter 
# Arbitrary Arguments are a tuple of dictionary parameter that can recive an unlimited amount of arguments 

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('mercedes', 'C 300 4MATIC Sedan', color='black', cost=46850)

print(car)