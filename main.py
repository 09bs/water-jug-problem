from collections import deque


def path_finder(path: list):
    """This Function finds the path to solve the problem."""
    final = [path[-1][0:3]]
    k = path[-1][-1]
    while k != -1:
        final.append(path[k][0:3])
        k = path[k][-1]

    return final[::-1]


def water_jug(x: int, y: int, z: int):
    """this function finds whether it is possible to solve the problem or not."""
    que = deque([(0, 0, 'start', -1)])
    visited = {}
    path = []
    prev = -1  # path is empty so previous is set to -1

    while que:
        jug = que.popleft()
        if jug[0:2] not in visited:
            visited[jug[0:2]] = 1
            path.append(jug)
            prev += 1  # prev is pointed to the index of recently added element in path

            if jug[0] == z or jug[1] == z:
                print(*path_finder(path), sep='\n')
                return True

            if jug[0] < x:
                que.append((x, jug[1], f'fill {x} liter jug', prev))

            if jug[1] < y:
                que.append((jug[1], y, f'fill {y} liter jug', prev))

            if jug[0] > 0:
                que.append((0, jug[1], f'empty {x} liter jug', prev))

            if jug[1] > 0:
                que.append((jug[0], 0, f'empty {y} liter jug', prev))

            if jug[0] + jug[1] >= x:
                que.append((x, jug[1] - (x - jug[0]), f'pour water from {y} liter jug to {x} liter jug', prev))
            else:
                que.append((jug[0] + jug[1], 0, f'pour water from {y} liter jug to {x} liter jug', prev))

            if jug[0] + jug[1] >= y:
                que.append((jug[0] - (y - jug[1]), y, f'pour water from {x} liter jug to {y} liter jug', prev))
            else:
                que.append((0, jug[0] + jug[1], f'pour water from {x} liter jug to {y} liter jug', prev))

    print('Not Possible')
    return False


x = int(input('Enter JUG 1 capacity: '))
y = int(input('Enter JUG 2 capacity: '))
z = int(input('Enter required quantity: '))

water_jug(x, y, z)
