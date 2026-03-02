from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)
lines = contents.splitlines()
contents_lines = ''
for line in lines:
    contents_lines += line + '\n'
print(contents_lines)