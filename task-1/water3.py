def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    actions = []
    x, y, z = s

    if x > 0 and y < 5:
        amount = min(x, 5 - y)
        actions.append(((x - amount, y + amount, z), amount))

    if x > 0 and z < 3:
        amount = min(x, 3 - z)
        actions.append(((x - amount, y, z + amount), amount))

    if y > 0 and x < 8:
        amount = min(y, 8 - x)
        actions.append(((x + amount, y - amount, z), amount))

    if y > 0 and z < 3:
        amount = min(y, 3 - z)
        actions.append(((x, y - amount, z + amount), amount))

    if z > 0 and x < 8:
        amount = min(z, 8 - x)
        actions.append(((x + amount, y, z - amount), amount))

    if z > 0 and y < 5:
        amount = min(z, 5 - y)
        actions.append(((x, y + amount, z - amount), amount))

    return actions  

