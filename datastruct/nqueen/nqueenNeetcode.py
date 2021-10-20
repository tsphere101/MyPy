import time

class NQueen:
    def __init__(self,n):
        self.n = n
        self.board = [["."] * n for _ in range(n)]
        self.res = []
        self.count = 0
        self.posDiag = set()
        self.negDiag = set()
        self.col = set()

    def backtrack(self,r=0):
        if r == self.n:
            # base case; completed the board
            copy = ["".join(row) for row in self.board]
            self.res.append(copy)
            self.count += 1
            return

        for c in range(n):  # goes in each column
            if c in self.col or (r+c) in self.posDiag or (r-c) in self.negDiag:
                continue  # already ocupied, not safe to land.

            # found the safe place
            self.col.add(c)
            self.posDiag.add(r+c)
            self.negDiag.add(r-c)
            self.board[r][c] = "Q"

            self.backtrack(r+1)

            # clean up
            self.col.remove(c)
            self.posDiag.remove(r+c)
            self.negDiag.remove(r-c)
            self.board[r][c] = "."



problemSize = 4
print("%12s%16s" % ("Board Size", "Runtime (ns)"))

# Testing for variation of problem size.
for loopCount in range(12):
    n = loopCount
    o = NQueen(n)
    startTime = time.time_ns()

    o.backtrack()

    elapsedTime = time.time_ns() - startTime
    print("\t%d\t%d" % (problemSize, elapsedTime))
    problemSize += 1  
