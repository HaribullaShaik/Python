cities = {
    'makkah': {
        'country': 'saudi arabia',
        'population': '2 million',
        'fact': 'it is the holiest city in islam'
    },
    'madinah': {
        'country': 'saudi arabia',
        'population': '1 million',
        'fact': 'it is the second holiest city in islam'
    },
    'riyadh': {
        'country': 'saudi arabia',
        'population': '7 million',
        'fact': 'it is the capital city of saudi arabia'
}
}
for city, info in cities.items():
    print(f'City: {city.title()}')
    country = info['country'].title()
    population = info['population']
    fact = info['fact'].capitalize()
    print(f'Country: {country}')
    print(f'Population: {population}')
    print(f'Fact: {fact}\n')