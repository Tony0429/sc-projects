"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=self.window.height - paddle_offset - self.paddle.height)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        # Default initial velocity for the ball
        self._dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx = - self._dx
        self._dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.starto)
        # Setting the window for the End
        self.game_over = GLabel("Game Over")
        self.congratulation = GLabel("Congratulation!")

        # Draw bricks
        # 設定顏色
        self.bricks = GRect(brick_width, brick_height)
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                if j > 7:
                    self.bricks.fill_color = "blue"
                if 7 >= j > 5:
                    self.bricks.fill_color = "green"
                if 5 >= j > 3:
                    self.bricks.fill_color = "yellow"
                if 3 >= j > 1:
                    self.bricks.fill_color = "orange"
                if j <= 1:
                    self.bricks.fill_color = "red"
                self.window.add(self.bricks, x=(brick_width + brick_spacing) * i, y=(brick_height + brick_spacing) * j)

    def move_paddle(self, m):
        self.paddle.x = m.x + self.paddle.width / 2
        if m.x <= self.paddle.width / 2:
            self.paddle.x = self.paddle.width
        if m.x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = m.x
            self.paddle.y = self.window.height - PADDLE_OFFSET

    def starto(self, n):
        # 設定開關，確保不會重複mouseclick
        self.switch = True

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

