board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def isWinner(b, lp):
    return (b[1] == lp and b[2] == lp and b[3] == lp) or\
        (b[4] == lp and b[5] == lp and b[6] == lp) or\
        (b[7] == lp and b[8] == lp and b[9] == lp) or\
        (b[1] == lp and b[4] == lp and b[7] == lp) or\
        (b[2] == lp and b[5] == lp and b[8] == lp) or\
        (b[3] == lp and b[6] == lp and b[9] == lp) or\
        (b[1] == lp and b[5] == lp and b[9] == lp) or\
        (b[1] == lp and b[5] == lp and b[7] == lp)


def playerMove():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')
        except Exception:
            print('Please type a number')
