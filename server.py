import math
import copy
import random
import json
import socket
import threading
from minimaxAgent import MiniMaxAgent

X = "X"
O = "O"
EMPTY = None

BOARD_MAXIMUM_SCORE = 1
BOARD_MINIMUM_SCORE = -1



class Problem:
    STATE_MINIMUM_SCORE = BOARD_MINIMUM_SCORE 
    STATE_MAXIMUM_SCORE = BOARD_MAXIMUM_SCORE 
    MAX = X 
    MIN = O

    def __init__(self) -> None:
        self.minimax_agent = MiniMaxAgent(self)
        self.first_time = True

    def actions(self, state):
        all_possible_actions = set()
        board = state
        for i, row in enumerate(board):
            for j, col_element in enumerate(row):
                if col_element is EMPTY:
                    all_possible_actions.add((i, j))

        return all_possible_actions


    def result(self, state, action):
        assert action is not None, "None type action is illegal."
        i, j = action
        assert 0 <= i <= 2 and 0 <= j <= 2, "Illegal Action!"
        board = state
        if board[i][j] is not EMPTY:
            raise AssertionError("This action is not valid, the spot is already occupied!")
        board_copy = copy.deepcopy(board)
        board_copy[i][j] = self.player(board)
        return board_copy



    def agent(self, state):
        number_of_Xs = 0
        number_of_Os = 0
        board = state
        for row in board:
            for col_element in row:
                if col_element == X:
                    number_of_Xs += 1
                elif col_element == O:
                    number_of_Os += 1

        if number_of_Xs > number_of_Os:
            return O
        return X



    def utility(self, state):
        winner_ = self.winner(state)
        if winner_ is X:
            return 1
        elif winner_ is O:
            return -1
        return 0


    def terminal(self, state):
        board = state
        if not self.winner(board):
            for row in board:
                for col_element in row:
                    if col_element is EMPTY:
                        return False
        return True


    def successors(self, state):
        all_possible_actions = self.actions(state)
        for action in all_possible_actions:
            result_state = self.result(state, action)
            yield (result_state, action)


    def initial_state(self):
        self.first_time = True
        return [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]

    def player(self, state):
        return self.agent(state)

    def winner(self, board):
        def checkDiagonally():
            two_diagonal_locations = (
                                        ( (0, 0), (1, 1), (2, 2) ),
                                        ( (2, 0), (1, 1), (0, 2) )
                                    )
            for diag in two_diagonal_locations:
                number_of_Xs = 0
                number_of_Os = 0
                try:
                    for xy in diag:
                        if board[xy[0]][xy[1]] is EMPTY:
                            raise Exception("Continue next diagonal.")
                        elif board[xy[0]][xy[1]] is X:
                            number_of_Xs += 1
                        else:
                            number_of_Os += 1
                except Exception:
                    continue

                if number_of_Xs == 3:
                    return X
                elif number_of_Os == 3:
                    return O

        def checkHorizontallyAndVertically():
            for row in board:
                number_of_Xs = 0
                number_of_Os = 0
                try:
                    for col_element in row:
                        if col_element is EMPTY:
                            raise Exception("Continue to next row.")
                        elif col_element is X:
                            number_of_Xs += 1
                        else:
                            number_of_Os += 1
                except Exception:
                    continue

                if number_of_Xs == 3:
                    return X
                elif number_of_Os == 3:
                    return O
            for col in range(3):
                number_of_Xs = 0
                number_of_Os = 0
                try:
                    for row in range(3):
                        if board[row][col] is EMPTY:
                            raise Exception("Continue to next col.")
                        elif board[row][col] is X:
                            number_of_Xs += 1
                        else:
                            number_of_Os += 1
                except Exception:
                    continue

                
                if number_of_Xs == 3:
                    return X
                elif number_of_Os == 3:
                    return O
        have_a_winner = checkHorizontallyAndVertically()
        if have_a_winner:
            return have_a_winner
        else:
            return checkDiagonally()


    def minimax(self, state):
        if self.first_time: 
            self.first_time = False
            if self.player(state) is O:
                return self.minimax_agent.solve(state)
            return random.choice(list(self.actions(state)))
        else:
            return self.minimax_agent.solve(state)


            





def handle_new_player(conn, addr):
    with conn:
        problem = Problem()

        while True:
            data = conn.recv(1024)
            if not data: break
            data = json.loads(data.decode('utf-8'))
            
            if data['args']:
                data = eval('problem.'+data['func_name'])(*data['args'])
            else:
                data = eval('problem.'+data['func_name'])()
            conn.sendall(json.dumps(data).encode('utf-8'))



HOST = ''                 
PORT = 50007             
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print('Waiting to serve new players ...')
    while True:
        conn, addr = s.accept()
        print(f'handling new player with ip {addr[0]} and port {addr[1]}')
        th = threading.Thread(target=handle_new_player, args=[conn, addr])
        th.start()
