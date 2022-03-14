"""
Tic Tac Toe Player
"""

import math
import socket
import json

X = "X"
O = "O"
EMPTY = None


HOST = 'localhost'    
PORT = 50007         
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))



def initial_state():
    data = {
        'func_name': 'initial_state',
        'args': None
    }
    s.sendall(json.dumps(data).encode('utf-8'))
    data = json.loads(s.recv(1024).decode('utf-8'))

    return data


def player(board):
    data = {
        'func_name': 'agent',
        'args': [board]
    }
    s.sendall(json.dumps(data).encode('utf-8'))
    data = json.loads(s.recv(1024).decode('utf-8'))

    return data


def actions(board):
    data = {
        'func_name': 'actions',
        'args': [board]
    }
    s.sendall(json.dumps(data).encode('utf-8'))
    data = json.loads(s.recv(1024).decode('utf-8'))

    return data


def result(board, action):
    data = {
        'func_name': 'result',
        'args': [board, action]
    }
    s.sendall(json.dumps(data).encode('utf-8'))
    data = json.loads(s.recv(1024).decode('utf-8'))

    return data



def winner(board):
    data = {
        'func_name': 'winner',
        'args': [board]
    }
    s.sendall(json.dumps(data).encode('utf-8'))
    data = json.loads(s.recv(1024).decode('utf-8'))

    return data


def terminal(board):
    data = {
        'func_name': 'terminal',
        'args': [board]
    }
    s.sendall(json.dumps(data).encode('utf-8'))
    data = json.loads(s.recv(1024).decode('utf-8'))

    return data


def utility(board):
    data = {
        'func_name': 'utility',
        'args': [board]
    }
    s.sendall(json.dumps(data).encode('utf-8'))
    data = json.loads(s.recv(1024).decode('utf-8'))

    return data

def minimax(board):
    data = {
        'func_name': 'minimax',
        'args': [board]
    }
    s.sendall(json.dumps(data).encode('utf-8'))
    data = json.loads(s.recv(1024).decode('utf-8'))

    return data
