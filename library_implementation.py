from matching import Player
from matching.games import StableMarriage

women = [
    Player("ella"),
    Player("lefke"),
    Player("julia"),
]

men = [
    Player("ted"),
    Player("sasha"),
    Player("jethro"),
]

ella, lefke, julia = women
ted, sasha, jethro = men

ella.set_prefs([sasha, ted, jethro])
lefke.set_prefs([sasha, jethro, ted])
julia.set_prefs([jethro, sasha, ted])

ted.set_prefs([ella, julia, lefke])
sasha.set_prefs([ella, lefke, julia])
jethro.set_prefs([lefke, julia, ella])

game = StableMarriage(women, men)
result = game.solve()
print(result)
print()
