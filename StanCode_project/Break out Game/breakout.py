"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 1000 / 50  # 120 frames per second
NUM_LIVES = 3  # Number of attempts

# Variables
SCORE = 0


def main():
    global SCORE
    num_of_lives = NUM_LIVES
    graphics = BreakoutGraphics()
    graphics.switch = False
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    while True:
        ball_one = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)  # 左上角
        ball_two = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball.width, graphics.ball.y)  # 右上角
        ball_three = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * graphics.ball.height)  # 左下角
        ball_four = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball.width,
                                                  graphics.ball.y + 2 * graphics.ball.height)  # 右下角
        if graphics.switch is True:
            graphics.ball.move(dx, dy)
            if ball_one is not None:
                if ball_one == graphics.paddle:
                    if dy > 0:
                        dy = -dy
                else:
                    graphics.window.remove(ball_one)
                    SCORE += 1
                    if dy < 0 :
                        dy = -dy
            elif ball_two is not None:
                if ball_two == graphics.paddle:
                    if dy > 0:
                        dy = -dy
                else:
                    graphics.window.remove(ball_two)
                    SCORE += 1
                    if dy < 0:
                        dy = -dy
            elif ball_three is not None:
                if ball_three == graphics.paddle:
                    if dy > 0:
                        dy = -dy
                else:
                    graphics.window.remove(ball_three)
                    SCORE += 1
                    if dy < 0:
                        dy = -dy
            elif ball_four is not None:
                if ball_four == graphics.paddle:
                    if dy > 0:
                        dy = -dy
                else:
                    graphics.window.remove(ball_four)
                    SCORE += 1
                    if dy < 0:
                        dy = -dy
            # 球碰到paddle 或是 brick 進行反彈
            # 球碰到邊界進行反彈

            if graphics.ball.x + graphics.ball.width >= graphics.window.width:  # 左右兩邊碰撞改變X位移
                dx = -dx
            if graphics.ball.x <= 0:
                dx = -dx
            if graphics.ball.y <= 0:                                            # 上下兩邊碰撞改變X位移
                dy = -dy
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                # graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                #                     y=(graphics.window.height - graphics.ball.height) / 2)
                # graphics.switch = False
                # num_of_lives -= 1
                dy = -dy
            if num_of_lives == 0 or SCORE == 100:
                # Game Over
                break
        pause(FRAME_RATE)
    print("Game Over")
    if SCORE < 100:
        graphics.window.clear()
        graphics.game_over.font = "-40"
        graphics.window.add(graphics.game_over, x=100, y=graphics.window.height / 2)
        print(str(SCORE))
    else:
        graphics.window.clear()
        graphics.congratulation.font = "-40"
        graphics.window.add(graphics.congratulation, x=100, y=graphics.window.height / 2)






if __name__ == '__main__':
    main()
