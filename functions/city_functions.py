def get_city_country_formatted(city, country, population = ''):
    """Generate a formatted City, Country with Population"""
    if population:
        return f"{city}, {country}".title() + f" - population {population}"
    else:
        return f"{city}, {country}".title()


    