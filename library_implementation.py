from matching import Player
from matching.games import StableMarriage

women = [
    Player("betty"),
    Player("claire"),
    Player("alice"),
]

men = [
    Player("aaron"),
    Player("brad"),
    Player("charles"),
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
