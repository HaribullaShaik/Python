from pathlib import Path
def read_files(filenames):
    """Read the contents of a list of files."""
    for filename in filenames:
        path = Path(filename)
        try:
            contents = path.read_text(encoding = 'utf-8')
        except FileNotFoundError:
            pass
        else:
            print(contents)
filenames = ['cats.txt', 'dogs.txt', 'birds.txt']
read_files(filenames)