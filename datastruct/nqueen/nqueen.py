BOARD_SIZE = 16


def under_attack(col, queens):
    return col in queens or \
        any(abs(col - x) == len(queens)-i for i, x in enumerate(queens))


def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = (solution+[i+1]
                     # first for clause is evaluated immediately,
                     for solution in solutions
                     # so "solutions" is correctly captured
                     for i in range(BOARD_SIZE)
                     if not under_attack(i+1, solution))
    return solutions


answers = solve(BOARD_SIZE)
first_answer = next(answers)
print(list(enumerate(first_answer, start=1)))
