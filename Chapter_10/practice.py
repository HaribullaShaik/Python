from pathlib import Path

contents = "I Love Programming!\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path = Path('Chapter_10/programming.txt')
path.write_text(contents)