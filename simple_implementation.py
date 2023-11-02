men = [
    "aaron",
    "brad",
    "charles",
    "david",
    "edward",
    "frank",
    "greg",
    "harry",
]

women = [
    "alice",
    "betty",
    "claire",
    "donna",
    "esther",
    "fay",
    "grace",
    "holly",
]

prefs = {
    # women
    "alice": ['frank', 'greg', 'aaron', 'brad', 'charles', 'edward', 'david', 'harry'],
    "betty": ['charles', 'aaron', 'brad', 'greg', 'edward', 'frank', 'david', 'harry'],
    "claire": ['edward', 'charles', 'frank', 'aaron', 'david', 'brad', 'greg', 'harry'],
    "donna": ['brad', 'greg', 'frank', 'aaron', 'edward', 'david', 'harry', 'charles'],
    "esther": ['brad', 'aaron', 'charles', 'frank', 'greg', 'david', 'harry', 'edward'],
    "fay": ['edward', 'greg', 'david', 'brad', 'harry', 'frank', 'charles', 'aaron'],
    "grace": ['david', 'frank', 'brad', 'harry', 'greg', 'edward', 'aaron', 'charles'],
    "holly": ['greg', 'edward', 'charles', 'frank', 'harry', 'aaron', 'brad', 'david'],
    # men
    "aaron": ['holly', 'fay', 'donna', 'grace', 'betty', 'esther', 'claire', 'alice'],
    "brad": ['claire', 'betty', 'esther', 'alice', 'grace', 'holly', 'donna', 'fay'],
    "charles": ['betty', 'holly', 'alice', 'donna', 'fay', 'grace', 'claire', 'esther'],
    "david": ['grace', 'holly', 'esther', 'betty', 'claire', 'alice', 'fay', 'donna'],
    "edward": ['claire', 'betty', 'fay', 'esther', 'grace', 'donna', 'holly', 'alice'],
    "frank": ['betty', 'claire', 'esther', 'grace', 'fay', 'alice', 'holly', 'donna'],
    "greg": ['claire', 'fay', 'alice', 'holly', 'esther', 'betty', 'grace', 'donna'],
    "harry": ['betty', 'alice', 'claire', 'donna', 'holly', 'fay', 'esther', 'grace'],
}

matches = {
    "alice": None,
    "betty": None,
    "claire": None,
    "donna": None,
    "esther": None,
    "fay": None,
    "grace": None,
    "holly": None,
}

exclusions = {
    "aaron": [],
    "brad": [],
    "charles": [],
    "david": [],
    "edward": [],
    "frank": [],
    "greg": [],
    "harry": [],
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
