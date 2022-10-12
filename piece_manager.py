from tetronimo import Tetronimo
from operator import add, sub

WIDTH = 10
HEIGHT = 20

QUEUE_ORIGINS = [(215, 285), (215, 195), (215, 105)]
ORIGIN_COORDINATES = (15, 285)
ORIGIN_INDEX = (5, 19)

HOLD_COORDINATES = (-215, 285)


class PieceManager:
    def __init__(self, square_size):
        self.square_size = square_size

        # 10 x 20 array of None to begin
        self.board = None
        self.initialize_board()

        self.active_piece = None
        self.queue = []
        self.hold_piece = None

        self.left_wall = -WIDTH / 2 * self.square_size
        self.right_wall = WIDTH / 2 * self.square_size
        self.top_wall = HEIGHT / 2 * self.square_size
        self.bottom_wall = -HEIGHT / 2 * self.square_size

        for index in range(0, 3):
            self.queue_new()

        self.next_piece()

        self.draw_queue()

        self.active_piece.draw_piece(ORIGIN_COORDINATES, ORIGIN_INDEX)

    # initialize 20x10 array of None
    def initialize_board(self):
        self.board = []
        for row_index in range(0, 20):
            row = []
            for col_index in range(0, 10):
                row.append(None)
            self.board.append(row)

    def swap_hold_piece(self, event=None):
        if self.hold_piece is None:
            self.hold_piece = self.active_piece
            self.hold_piece.draw_piece(HOLD_COORDINATES)

            self.next_piece()
        else:
            temp = self.active_piece
            self.active_piece = self.hold_piece
            self.hold_piece = temp

            self.hold_piece.draw_piece(HOLD_COORDINATES)
            self.active_piece.draw_piece(ORIGIN_COORDINATES, ORIGIN_INDEX)

    def queue_new(self):
        # pick random new piece
        # add to end of queue
        new_piece = Tetronimo()
        self.queue.append(new_piece)

        self.draw_queue()

    def draw_queue(self):
        for index, piece in enumerate(self.queue):
            piece.draw_piece(QUEUE_ORIGINS[index])

    def next_piece(self):
        self.active_piece = self.queue[0]
        self.queue.remove(self.active_piece)
        self.queue_new()

        self.active_piece.draw_piece(ORIGIN_COORDINATES, ORIGIN_INDEX)

    #
    def move_left(self, event):
        # Check if piece can move left
        for turt in self.active_piece.turtles:
            if turt.x_index == 0 or self.board[turt.y_index][turt.x_index - 1] is not None:
                return
            # elif square is occupied by piece already on board

        # Move piece left
        for turt in self.active_piece.turtles:
            turt.goto(turt.xcor() - self.square_size, turt.ycor())
            turt.x_index -= 1

    def move_right(self, event):
        # Check if piece can move right
        for turt in self.active_piece.turtles:
            if turt.x_index == 9 or self.board[turt.y_index][turt.x_index + 1] is not None:
                return
            # elif square is occupied by piece already on board

        # Move piece right
        for turt in self.active_piece.turtles:
            turt.goto(turt.xcor() + self.square_size, turt.ycor())
            turt.x_index += 1

    def move_down(self, event=None):
        for turt in self.active_piece.turtles:
            if turt.y_index == 0 or self.board[turt.y_index - 1][turt.x_index] is not None:
                return False
            # elif square is occupied by piece already on board
        for turt in self.active_piece.turtles:
            turt.goto(turt.xcor(), turt.ycor() - self.square_size)
            turt.y_index -= 1
        return True

    def check_lines(self):
        return 0

    def is_full(self):
        for space in self.board[19]:
            if space is not None:
                return True

        return False

    # rotate around square[1]
    def finish_active(self):
        for turt in self.active_piece.turtles:
            self.board[turt.y_index][turt.x_index] = turt

    def rotate_right(self, event=None):
        if self.active_piece.rotation == 1:
            if self.active_piece.shape_name == "I":
                self.rotation(add, add, sub, sub, sub, sub, 2, 2)
            elif self.active_piece.shape_name == "S":
                self.rotation(sub, sub, sub, add, add, add, 0, 2)

        elif self.active_piece.rotation == 2:
            if self.active_piece.shape_name == "I":
                self.rotation(add, sub, sub, add, sub, add, 2, 2)
            elif self.active_piece.shape_name == "S":
                self.rotation(sub, add, add, add, add, add, 2, 0)

        elif self.active_piece.rotation == 3:
            if self.active_piece.shape_name == "I":
                self.rotation(sub, sub, add, add, add, add, 2, 2)
            elif self.active_piece.shape_name == "S":
                self.rotation(add, add, add, sub, sub, sub, 0, 2)

        elif self.active_piece.rotation == 4:
            if self.active_piece.shape_name == "I":
                self.rotation(sub, add, add, sub, add, sub, 2, 2)
            elif self.active_piece.shape_name == "S":
                self.rotation(add, sub, sub, sub, sub, sub, 2, 0)

        self.active_piece.rotate_right()

    def rotate_left(self):
        if self.active_piece.rotation == 1:
            if self.active_piece.shape_name == "I":
                self.rotation(add, sub, sub, add, sub, add, 2, 2)
            elif self.active_piece.shape_name == "S":
                self.rotation(sub, add, add, add, add, add, 2, 0)
            elif self.active_piece.shape_name == "Z":
                pass
            elif self.active_piece.shape_name == "L":
                pass
            elif self.active_piece.shape_name == "J":
                pass
            elif self.active_piece.shape_name == "T":
                pass

        if self.active_piece.rotation == 2:
            if self.active_piece.shape_name == "I":
                self.rotation(add, add, sub, sub, sub, sub, 2, 2)
            elif self.active_piece.shape_name == "S":
                self.rotation(add, add, add, sub, sub, sub, 0, 2)
            elif self.active_piece.shape_name == "Z":
                pass
            elif self.active_piece.shape_name == "L":
                pass
            elif self.active_piece.shape_name == "J":
                pass
            elif self.active_piece.shape_name == "T":
                pass

        elif self.active_piece.rotation == 3:
            if self.active_piece.shape_name == "I":
                self.rotation(sub, add, add, sub, add, sub, 2, 2)
            elif self.active_piece.shape_name == "S":
                self.rotation(add, sub, sub, sub, sub, sub, 2, 0)
            elif self.active_piece.shape_name == "Z":
                pass
            elif self.active_piece.shape_name == "L":
                pass
            elif self.active_piece.shape_name == "J":
                pass
            elif self.active_piece.shape_name == "T":
                pass

        elif self.active_piece.rotation == 4:
            if self.active_piece.shape_name == "I":
                self.rotation(sub, sub, add, add, add, add, 2, 2)
            elif self.active_piece.shape_name == "S":
                self.rotation(sub, sub, sub, add, add, add, 0, 2)
            elif self.active_piece.shape_name == "Z":
                pass
            elif self.active_piece.shape_name == "L":
                pass
            elif self.active_piece.shape_name == "J":
                pass
            elif self.active_piece.shape_name == "T":
                pass

        self.active_piece.rotate_left()

    def rotation(self, x_0_op, y_0_op, x_2_op, y_2_op, x_3_op, y_3_op, x_3_mod,
                 y_3_mod):
        turt_0 = self.active_piece.turtles[0]
        # turtles[1] is rotation center and doesnt move
        turt_2 = self.active_piece.turtles[2]
        turt_3 = self.active_piece.turtles[3]

        turt_0_x = turt_0.x_index
        turt_0_y = turt_0.y_index

        # turtles[1] is rotation center and doesnt move

        turt_2_x = turt_2.x_index
        turt_2_y = turt_2.y_index

        turt_3_x = turt_3.x_index
        turt_3_y = turt_3.y_index

        turt_0_new_x = x_0_op(turt_0_x, 1)
        turt_0_new_y = y_0_op(turt_0_y, 1)
        if not self.is_valid_rotation(turt_0_new_x, turt_0_new_y):
            return

        turt_2_new_x = x_2_op(turt_2_x, 1)
        turt_2_new_y = y_2_op(turt_2_y, 1)
        if not self.is_valid_rotation(turt_2_new_x, turt_2_new_y):
            return

        turt_3_new_x = x_3_op(turt_3_x, x_3_mod)
        turt_3_new_y = y_3_op(turt_3_y, y_3_mod)
        if not self.is_valid_rotation(turt_3_new_x, turt_3_new_y):
            return

        turt_0.x_index = turt_0_new_x
        turt_0.y_index = turt_0_new_y
        turt_0.goto(x_0_op(turt_0.xcor(), self.square_size), y_0_op(turt_0.ycor(), self.square_size))

        turt_2.x_index = turt_2_new_x
        turt_2.y_index = turt_2_new_y
        turt_2.goto(x_2_op(turt_2.xcor(), self.square_size), y_2_op(turt_2.ycor(), self.square_size))

        turt_3.x_index = turt_3_new_x
        turt_3.y_index = turt_3_new_y
        turt_3.goto(x_3_op(turt_3.xcor(), x_3_mod * self.square_size), y_3_op(turt_3.ycor(), y_3_mod * self.square_size))

    def is_valid_rotation(self, x, y):
        return not out_of_bounds(x, y) and self.board[y][x] is None


def out_of_bounds(x, y):
    return x < 0 or x > 9 or y < 0 or y > 19


