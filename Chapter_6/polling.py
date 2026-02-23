favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
peoples = ["jen", "sarah", "edward", "phil", "michael"]
for people in peoples:
    if people in favorite_languages.keys():
        print(f"Thank you for taking the poll, {people.title()}.")
    else:
        print(f"{people.title()}, please take our poll!")