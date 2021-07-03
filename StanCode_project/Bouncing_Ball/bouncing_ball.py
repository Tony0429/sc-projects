"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
switch = False  # 開關

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global VX, switch
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    ball.fill_color = "black"
    window.add(ball)
    vy = 0
    onmouseclicked(starto)
    while True:
        if switch is True:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y+SIZE > window.height:
                if vy > 0:
                    vy *= REDUCE
                    vy = - vy
            if ball.x > window.width:
                switch = False
                window.add(ball, x=START_X, y=START_Y)
        pause(DELAY)



def starto(m):
    global switch
    switch = True




if __name__ == "__main__":
    main()

if ball_one is not None:
    if ball_one == graphics.paddle.line_width:
        dx = -dx
        dy = -dy
    else:
        # graphics.window.remove(ball_one)
        dx = -dx
        dy = -dy
        SCORE += 1
if ball_two is not None:
    if ball_two == graphics.paddle.line_width:
        dx = -dx
        dy = -dy
    else:
        # graphics.window.remove(ball_two)
        dx = -dx
        dy = -dy
        SCORE += 1
if ball_three is not None:
    if ball_three == graphics.paddle.line_width:
        dx = -dx
        dy = -dy
    else:
        # graphics.window.remove(ball_three)
        dx = -dx
        dy = -dy
        SCORE += 1
if ball_four is not None:
    if ball_four == graphics.paddle.line_width:
        dx = -dx
        dy = -dy
    else:
        # graphics.window.remove(ball_four)
        dx = -dx
        dy = -dy
        SCORE += 1