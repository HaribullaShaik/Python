favorite_places = {
    'syed': ['makkah', 'madinah', 'riyadh'],
    'sara': ['paris', 'london', 'new york'],
    'ahmed': ['cairo', 'alexandria', 'giza'],
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")