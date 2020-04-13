def checkio(game_result):
    game = list(zip(*game_result))
    x = 0
    if game[0][0] == game[1][1] == game[2][2] != '.':
        if game[0][0] == 'X':
            return 'X'
        else:
            return 'O'
        x += 1
    elif game[2][0] == game[1][1] == game[0][2] != '.':
        if game[2][0] == 'X':
            return 'X'
        else:
            return 'O'
        x += 1
    elif True:
        for k in game_result:
            k.split()
            if k[0] == k[1] == k[2] != '.':
                if k[0] == 'X':
                    return 'X'
                else:
                    return 'O'
                x += 1
        for i in game:
            if i[0] == i[1] == i[2] != '.':
                if i[0] == 'X':
                    return 'X'
                else:
                    return 'O'
                x += 1
    if x == 0:
        return 'D'
