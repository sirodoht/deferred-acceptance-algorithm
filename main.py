from matching import Player
from matching.games import StableMarriage

suitors = [
    Player("Bingley"),
    Player("Collins"),
    Player("Darcy"),
    Player("Wickham"),
]

reviewers = [
    Player("Charlotte"),
    Player("Elizabeth"),
    Player("Jane"),
    Player("Lydia"),
]

bingley, collins, darcy, wickham = suitors
charlotte, elizabeth, jane, lydia = reviewers

bingley.set_prefs([jane, elizabeth, lydia, charlotte])
collins.set_prefs([elizabeth, jane, lydia, charlotte])
darcy.set_prefs([elizabeth, jane, charlotte, lydia])
wickham.set_prefs([lydia, jane, elizabeth, charlotte])

charlotte.set_prefs([collins, darcy, bingley, wickham])
elizabeth.set_prefs([wickham, darcy, bingley, collins])
jane.set_prefs([bingley, wickham, darcy, collins])
lydia.set_prefs([wickham, bingley, darcy, collins])

game = StableMarriage(suitors, reviewers)
result = game.solve()
print(result)
