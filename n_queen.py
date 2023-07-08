import math
import sys
import random
import numpy as np
import matplotlib.pyplot as plt

maxq=100
max_iter=1000

def in_conflict(column,row,other_column,other_row):
    if column==other_column:
        return True
    elif row==other_row:
        return True
    elif abs(column-other_column)==abs(row-other_row):
        return True
    return False

def in_conflict_with_another_queen(row,column,board):
    for other_column,other_row in enumerate(board):
        if in_conflict(column,row,other_column,other_row):
            if (row!=other_row or column!=other_column):
                return True
    return False

def init_board(nqueens):
    board=[]
    for column in range(nqueens):
        board.append(random.randint(0,nqueens-1))
    return board

def count_conflicts(board):
    count=0
    for queen in range(0,len(board)):
        for other_queen in range(queen+1,len(board)):
            if in_conflict(queen,board[queen],other_queen,board[other_queen]):
                count+=1
    return count

def evaluate_state(board):
    return(len(board)-1)*len(board)/2-count_conflicts(board)

def print_board(board):
    for row in range(len(board)):
        line=''
        for column in range(len(board)):
            if board[column]==row:
                line+='Q' if in_conflict_with_another_queen(row,column,board) else 'q'

            else:
                line+='.'
        print(line)
    print("")

def plot(i,evaluation,board,optimum):
    #for results which break the loop in algorithm
    if i==max_iter:
        evaluation.append(evaluate_state(board))
    plt.plot(range(i+1),evaluation,'teal')
    plt.plot(i,optimum,'ro')
    plt.xlabel("Iterations")
    plt.ylabel("Evaluation Score")
    plt.show()

def hill_climbing(board):
    i=0
    optimum=(len(board)-1)*len(board)/2
    evaluation=[evaluate_state(board)]
    while(evaluate_state(board))!=optimum:
        i+=1
        print(f"Iteration {i}: Evaluation = {evaluate_state(board)}")
        if i==max_iter: #Give up after max_iter tries
            break

        max_score_of_each_column=[]
        row_resulting_in_max_score=[]

        for col in range(len(board)):
            col_scores=[]

            for row in range(len(board)):
                new_board=board.copy()
                new_board[col]=row
                col_scores.append(evaluate_state(new_board))

            if max(col_scores)>evaluate_state(board):
                max_score_of_each_column.append(max(col_scores))
                row_resulting_in_max_score.append(np.argmax(col_scores))

            else:
                max_score_of_each_column(False)
                row_resulting_in_max_score(False) 

        if max(max_score_of_each_column):
            maximizing_col=np.argmax(max_score_of_each_column)
            maximizing_row=row_resulting_in_max_score[maximizing_col]
            board[maximizing_col]=maximizing_row

        evaluation.append(evaluate_state(board))
        if evaluate_state(board)==optimum:
            print('\nSolved Puzzle!')

        print('\nFinal State :') 
        print_board(board)
        plot(i,evaluation,board,optimum)
     
def main():
    n_queens=int(input('enter n :'))
    if n_queens<1 or n_queens<maxq:
        board=init_board(n_queens)
        print('\nInitial Board :')
        print(board)
        hill_climbing(board)

#This is the starting point of the program
if __name__=="__main__":
    main()