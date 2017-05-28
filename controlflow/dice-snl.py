import random
final_square = 25
board = range(0, final_square)
board[3] += 8
board[6] += 11
board[9] += 9
board[10] += 2
board[14] -= 10
board[19] -= 11
board[22] -= 2
board[24] -= 8
square = 0
dice_roll = 0
print("Game Starting at square {}".format(square))
while square < final_square:

    dice_roll = random.randint(0, 7)

    square += dice_roll

    if square < len(board):
        old_square = square
        square += board[square]
        print("dice roll = {}, landing = {}, instruction = {}, destination = {}".format(
            dice_roll, old_square, board[old_square], square))
print("Game over !")
