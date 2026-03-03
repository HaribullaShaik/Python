from pathlib import Path
path = Path('alice.txt')
contents = path.read_text()
print(contents.lower().count('the'))
print(contents.lower().count('the '))  # Count 'the' followed by a space