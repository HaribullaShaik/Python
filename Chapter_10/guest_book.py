from pathlib import Path
path = Path('Chapter_10/guest_book.txt')
guest_list = []
while True:
    name = input("Please enter your name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    print(f"Hello, {name}! Welcome to the guest book.")
    guest_list.append(name)

file_string = ''
for guest in guest_list:
    file_string += guest + '\n'
path.write_text(file_string)