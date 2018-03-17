def main():
    puzzle = []
    for i in range(9):
        puzzle.append([None] * 9)

    print("Enter puzzle (enter 0 for blanks)")
    print("   1 2 3 4 5 6 7 8 9")
    for i in range(1, 10):
        print(str(i) + ": ", end="")
        puzzle[i-1] = map(int, input().split())

main()