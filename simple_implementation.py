men = [
    "aaron",
    "brad",
    "charles",
    "david",
    "edward",
    "frank",
    "greg",
    "harry",
    "irving",
    "jack",
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
    "isabella",
    "jane",
]

prefs = {
    # women
    "alice": ['frank', 'greg', 'aaron', 'brad', 'charles', 'edward', 'irving', 'david', 'jack', 'harry'],
    "betty": ['charles', 'aaron', 'brad', 'greg', 'edward', 'frank', 'jack', 'david', 'harry', 'irving'],
    "claire": ['edward', 'charles', 'frank', 'aaron', 'david', 'brad', 'irving', 'jack', 'greg', 'harry'],
    "donna": ['brad', 'greg', 'jack', 'frank', 'aaron', 'irving', 'edward', 'david', 'harry', 'charles'],
    "esther": ['brad', 'aaron', 'charles', 'irving', 'frank', 'greg', 'david', 'jack', 'harry', 'edward'],
    "fay": ['jack', 'edward', 'greg', 'david', 'irving', 'brad', 'harry', 'frank', 'charles', 'aaron'],
    "grace": ['david', 'frank', 'brad', 'harry', 'greg', 'edward', 'aaron', 'irving', 'charles', 'jack'],
    "holly": ['greg', 'edward', 'charles', 'jack', 'frank', 'harry', 'irving', 'aaron', 'brad', 'david'],
    "isabella": ['greg', 'david', 'aaron', 'edward', 'brad', 'harry', 'frank', 'jack', 'charles', 'irving'],
    "jane": ['greg', 'charles', 'irving', 'harry', 'aaron', 'david', 'brad', 'edward', 'frank', 'jack'],
    # men
    "aaron": ['jane', 'holly', 'fay', 'donna', 'grace', 'betty', 'esther', 'isabella', 'claire', 'alice'],
    "brad": ['claire', 'betty', 'jane', 'esther', 'alice', 'grace', 'holly', 'isabella', 'donna', 'fay'],
    "charles": ['betty', 'holly', 'alice', 'donna', 'fay', 'jane', 'grace', 'claire', 'isabella', 'esther'],
    "david": ['grace', 'holly', 'isabella', 'jane', 'esther', 'betty', 'claire', 'alice', 'fay', 'donna'],
    "edward": ['claire', 'betty', 'fay', 'esther', 'grace', 'donna', 'isabella', 'jane', 'holly', 'alice'],
    "frank": ['betty', 'jane', 'claire', 'esther', 'grace', 'fay', 'alice', 'isabella', 'holly', 'donna'],
    "greg": ['claire', 'fay', 'alice', 'jane', 'isabella', 'holly', 'esther', 'betty', 'grace', 'donna'],
    "harry": ['jane', 'isabella', 'betty', 'alice', 'claire', 'donna', 'holly', 'fay', 'esther', 'grace'],
    "irving": ['fay', 'donna', 'claire', 'alice', 'holly', 'jane', 'esther', 'isabella', 'grace', 'betty'],
    "jack": ['claire', 'holly', 'fay', 'betty', 'jane', 'esther', 'grace', 'isabella', 'alice', 'donna'],
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
    "isabella": None,
    "jane": None,
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
    "irving": [],
    "jack": [],
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
