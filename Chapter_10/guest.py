from pathlib import Path
path = Path('Chapter_10/guest.txt')

name = input("What is your name? ")
path.write_text(name)