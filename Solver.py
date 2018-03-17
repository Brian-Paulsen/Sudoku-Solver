def valid(puzzle):


def solver(puzzle, start_row = 0, start_col = 0):

    if start_row == 9:
        return True

    if puzzle[start_row][start_col] == 0:
        for i in range(1, 10):
            print(i)
            puzzle[start_row][start_col] = i
            if valid(puzzle):
                if solver(puzzle, start_row+1 if start_col == 8 else start_row, 0 if start_col == 8 else start_col+1):
                    return True
        return False

    else:
        solver(puzzle, start_row + 1 if start_col == 8 else start_row, 0 if start_col == 8 else start_col + 1)
        return True



def main():
    puzzle = []
    for i in range(9):
        puzzle.append([None] * 9)

    print("Enter puzzle (enter 0 for blanks)")
    print("   1 2 3 4 5 6 7 8 9")
    for i in range(1, 10):
        print(str(i) + ": ", end="")
        puzzle[i-1] = list(map(int, input().split()))

    solver(puzzle)
    for row in puzzle:
        for col in row:
            print(col, end=" ")
        print()

main()