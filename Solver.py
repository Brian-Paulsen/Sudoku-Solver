#put in the puzzle and the coordinates of the newly added number
def valid(puzzle, row, col):

    #check rows
    used = [False]*10
    for i in range(9):
        if puzzle[row][i] != 0:
            if used[puzzle[row][i]] is True:
                return False
            used[puzzle[row][i]] = True

    #check columns
    used = [False]*10
    for i in range(9):
        if puzzle[i][col] != 0:
            if used[puzzle[i][col]] is True:
                return False
            used[puzzle[i][col]] = True

    #check boxes
    top_corner_row = (row // 3) * 3
    top_corner_col = (col // 3) * 3
    used = [False]*10
    for i in range(3):
        for j in range(3):
            curr = puzzle[top_corner_row + i][top_corner_col + j]
            if curr != 0:
                if used[curr] is True:
                    return False
                used[curr] = True

    return True


def solver(puzzle, start_row = 0, start_col = 0):

    if start_row == 9:
        return True

    if puzzle[start_row][start_col] == 0:
        for i in range(1, 10):
            puzzle[start_row][start_col] = i
            if valid(puzzle, start_row, start_col):
                if solver(puzzle, start_row+1 if start_col == 8 else start_row, 0 if start_col == 8 else start_col+1):
                    return True
        return False

    else:
        return solver(puzzle, start_row + 1 if start_col == 8 else start_row, 0 if start_col == 8 else start_col + 1)


def main():
    puzzle = []
    for i in range(9):
        puzzle.append([None] * 9)

    print("Enter puzzle (enter 0 for blanks)")
    print("   1 2 3 4 5 6 7 8 9")
    for i in range(1, 10):
        print(str(i) + ": ", end="")
        puzzle[i-1] = list(map(int, input().split()))

    print(solver(puzzle))
    for row in puzzle:
        for col in row:
            print(col, end=" ")
        print()

main()