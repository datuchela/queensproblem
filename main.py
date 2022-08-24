import time
import os

def solveNQueens(n: int, visual: bool):
    
    # constants
    delay = 0.5 #seconds
    #

    col = []
    posDiag = []
    negDiag = []

    res = []
    board = [["[_]"] * n for i in range(n)]
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in  negDiag:
                continue

            col.append(c)
            posDiag.append(r+c)
            negDiag.append(r-c)
            board[r][c] = "[Q]"

            if visual == True:
                time.sleep(delay)
                copy = ["".join(row) for row in board]
                os.system('clear')
                print('\033[?25l', end="")
                for i in copy:
                    print(i)
            
            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "[_]"
            

    timeWALLStart = time.time()
    timeCPUStart = time.process_time()

    backtrack(0)
    
    timeCPUEnd = time.process_time()
    timeWALLEnd = time.time()

    os.system('clear')

    elapsedCPUTime = round((timeCPUEnd - timeCPUStart)*1000, 2)
    elapsedWALLTime = round((timeWALLEnd - timeWALLStart)*1000, 2)
    print("CPU time: " + str(elapsedCPUTime) + " ms | " + "Wall time: " + str(elapsedWALLTime) + " ms")

    print('\033[?25h', end="")

    print("Number of solutions: ",len(res))
    showBoards = input("Wanna see solutions? y/(n): ")
    if(showBoards == "y"):
        print("_____\n")
        for i in res:
            for j in i:
                print(j)
            print("_____\n")
        print("CPU time: " + str(elapsedCPUTime) + " ms | " + "Wall time: " + str(elapsedWALLTime) + " ms")
    return res

def mainLoop():
    while True:
        print('Type "exit" or use "Ctrl ^ C" to exit the program')
        userInput = input("Provide integer N for [N x N] chess board (default: 8x8): ")
        visual = False
        visualInput = input("Want visuals? Note: visual version is significantly slow. y/(n): ")
        if visualInput == "y":
            visual = True
        try:
            if(userInput == "exit"):
                print("Bye!")
                return
            if userInput == "":
                value = 8
                break
            value = int(userInput)
            break
        except ValueError:
            print("N must be an integer!")
        
        
    solveNQueens(value, visual)



mainLoop()
