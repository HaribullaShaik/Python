current_users = ["admin", "alice", "bob", "charlie", "dave", "eve"]
new_users = ["frank", "grace", "heidi", "bob", "charlie"]
for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry {new_user}, that username is already taken. Please choose a different username.")
    else:
        print(f"Congratulations {new_user}, that username is available!")