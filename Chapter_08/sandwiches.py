def sandwich(*items):
    """Print the list of items that have been requested."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
sandwich('ham', 'cheese', 'lettuce', 'tomato')