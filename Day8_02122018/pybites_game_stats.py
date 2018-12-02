games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won=games_won):
    """Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""
    for people in games_won:
        if games_won[people] == 1:
            print(f"{people} has won {games_won[people]} game")
        else:
            print(f"{people} has won {games_won[people]} games")
    pass

print_game_stats()
