from city_functions import get_formatted_city_name

def test_test_city_country():
    """Do city names like 'Santiago, Chile' work?"""
    formatted_city_name = get_formatted_city_name('santiago', 'chile')
    assert formatted_city_name == 'Santiago, Chile'

def test_city_country_population():
    """Do city names like 'Santiago, Chile' and population work?"""
    formatted_city_name = get_formatted_city_name(
        'santiago', 'chile', '5,000,000')
    assert formatted_city_name == 'Santiago, Chile - population 5,000,000'