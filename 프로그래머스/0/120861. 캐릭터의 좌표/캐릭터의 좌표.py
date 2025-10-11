def solution(keyinput, board):
    rows, cols = board
    x, y = 0, 0 
    limit_x = rows // 2
    limit_y = cols // 2
    move = {
        "up": (0, 1),
        "down": (0, -1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    for key in keyinput:
        dx, dy = move[key]
        nx, ny = x + dx, y + dy

        if -limit_x <= nx <= limit_x and -limit_y <= ny <= limit_y:
            x, y = nx, ny


    return [x, y]