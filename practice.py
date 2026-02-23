favourite_languages = {
    "Alice": "Python",
    "Bob": "JavaScript",
    "Charlie": "C++",
}
print("The following languages have been mentioned:")
for language in sorted(set(favourite_languages.values())):
    print(language.title())
