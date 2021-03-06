def score(game):
    result = 0
    frame = 1
    in_first_half = True
    strike = ['X', 'x']
    spare = ['/']
    for i in range(len(game)):
        if game[i] in spare:
            result += 10 - last + get_value(game[i + 1])
        else:
            result += get_value(game[i])
        if frame < 10 and game[i] in strike:
            result += get_value(game[i + 1])
            if game[i + 2] in spare:
                result += 10 - get_value(game[i + 1])
            else:
                result += get_value(game[i + 2])
            in_first_half = True
            frame += 1
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
        last = get_value(game[i])
    return result


def get_value(char):
    try:
        return int(char)
    except:
        if char in ['X', 'x', '/']:
            return 10
        elif char == '-':
            return 0
        else:
            raise ValueError()
            