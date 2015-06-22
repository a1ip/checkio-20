def checkio(game_result):
    for row in game_result:
        if row[0] == row[1] == row[2] != '.':
            return row[0]
    # To check the verticals you can rotate a matrix with this trick:
    for row in zip(*game_result):
        if row[0] == row[1] == row[2] != '.':
            return row[0]

    if game_result[0][0] == game_result[1][1] == game_result [2][2] != ".":
        return game_result[1][1]
    elif game_result[0][2] == game_result[1][1] == game_result [2][0] != ".":
        return game_result[1][1]

    return 'D'

if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
