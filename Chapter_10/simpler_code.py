from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
contents_lines = ''
for line in contents.splitlines():
    contents_lines += line + '\n'
print(contents_lines.replace('Python', 'C'))