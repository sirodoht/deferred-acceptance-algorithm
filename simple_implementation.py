men = ["ted", "sasha", "jethro"]
women = ["julia", "ella", "lefke"]

prefs = {
    "lefke": ["sasha", "jethro", "ted"],
    "ella": ["sasha", "ted", "jethro"],
    "julia": ["jethro", "sasha", "ted"],
    "ted": ["ella", "julia", "lefke"],
    "sasha": ["lefke", "ella", "julia"],
    "jethro": ["lefke", "julia", "ella"],
}

matches = {
    "ella": None,
    "lefke": None,
    "julia": None,
}

exclusions = {
    "ted": [],
    "sasha": [],
    "jethro": [],
}

def get_top_preference(woman):
    for man in prefs[woman]:
        if woman in exclusions[man]:
            print(f"{woman} has already been rejected by {man}")
            continue
        else:
            print(f"{woman}'s preference is {man}")
            return man

    # if there is no man who has not been excluded and is no match
    raise ValueError(f"no more men left for {woman}")


def get_man_match(given_man):
    for woman, man in matches.items():
        if man == given_man:
            return woman

    raise ValueError(f"{man} is not matched with any woman")


print(f"{prefs=}\n")
free_women = women.copy()
while free_women:
    print(f"free_women={list(reversed(free_women))}")
    woman = free_women.pop()
    print(f"{woman}'s turn")
    man = get_top_preference(woman)

    if man in matches.values():
        current_match = get_man_match(man)
        print(f"{man} is currently matched with {current_match}")
        current_woman_index = prefs[man].index(current_match)
        print(f"{current_woman_index=}")
        new_woman_index = prefs[man].index(woman)
        print(f"{new_woman_index=}")
        if new_woman_index < current_woman_index:
            print(f"{woman} is higher in {man}'s list, switching")
            exclusions[man].append(current_match)
            print(f"adding {current_match} to {man}'s exclusion list: {exclusions[man]}")
            matches[woman] = man
        else:
            print(f"{woman} is lower in {man}'s list, ignored by {man}")
            exclusions[man].append(woman)
            print(f"add {woman} to {man}'s exclusion list: {exclusions[man]}")
            free_women.insert(0, woman)
            print(f"put {woman} back on free_women list")


    else:
        print(f"{man} is available, matching with {woman}")
        matches[woman] = man

    print()


print(matches)
