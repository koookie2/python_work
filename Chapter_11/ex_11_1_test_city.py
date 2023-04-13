from ex_11_1_city_functions import city_country

def test_city_country():
    """Do cities like 'Santiago Chile' work?"""
    assert city_country('santiago', 'chile') == 'Santiago Chile'

def test_city_country_population():
    """Do cities like 'Santiago Chile' work?"""
    assert city_country('santiago', 'chile', population=5000000) == 'Santiago Chile - population 5000000'

test_city_country()
test_city_country_population()