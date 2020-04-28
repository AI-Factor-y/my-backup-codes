import socket
from _thread import *
# from player import Player
import pickle
import os

server = "192.168.43.21"
port = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind((socket.gethostname(), 7777))


s.listen(2)
print("Waiting for a connection, Server Started")


# datas=[[[-2, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, -1, -1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]],[[-2, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, -1, -1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]]]
datas=[[(-5,-5),(-5,-5)],[(-5,-5),(-5,-5)]]
def threaded_client(conn, player):
    global datas
    conn.send(pickle.dumps(datas[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            datas[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    # reply = players[0]
                    reply=datas[0]
                    # pass
                else:
                    # reply = players[1]
                    reply=datas[1]

                print("Received: ", datas[player])
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1