def get_formatted_city_name(city, country, population=''):
    if population:
        return f'{city.title()}, {country.title()} - population {population}'
    else:
        return f'{city.title()}, {country.title()}'