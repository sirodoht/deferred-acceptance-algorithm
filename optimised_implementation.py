def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
    raise ValueError('Value does not exist in the dictionary')

men = ["aaron", "brad", "charles"]
women = ["alice", "betty", "claire"]

prefs = {
    "claire": ["brad", "charles", "aaron"],
    "betty": ["brad", "aaron", "charles"],
    "alice": ["charles", "brad", "aaron"],
    "aaron": ["betty", "alice", "claire"],
    "brad": ["betty", "claire", "alice"],
    "charles": ["claire", "alice", "betty"],
}

matches = {
    "betty": None,
    "claire": None,
    "alice": None,
}

free_women = women.copy()
while free_women:
    print(f"{free_women=}")
    woman = free_women.pop()
    print("now for " + woman)
    man = prefs[woman][0]
    print("she prefers " + man)
    print(f"{prefs=}")

    if man in matches.values():
        print(f"{man} has been picked already")
        print(f"{matches}")
        current_match = get_key(man, matches)
        print(f"{man}'s current match: {current_match}")
        matches[woman] = None
        print(f"reset {woman}'s match")
        free_women.append(current_match)
        print(f"{free_women=}")
    else:
        print(f"{man} has NOT been picked yet")
        print(matches)

    matches[woman] = man
    print(f"set {woman}'s man to {man}")
    print(f"{matches}")

    print(f"get index of {man}'s prefs: {prefs[man]}")
    index = prefs[man].index(woman)
    print(f"{index=}")
    successors = prefs[man][index + 1:]
    print(f"{successors=}")
    for person in successors:
        print(f"{person}'s preferences: {prefs[person]}")
        prefs[person] = [p for p in prefs[person] if p != man]
        print(f"{person}'s new preferences: {prefs[person]}")
    print(f"{prefs=}")
    print("=== iteration over ===")
    print()

print(matches)
