from network import Network
import msvcrt as m



run = True
n = Network()
# startPos = read_pos(n.getPos())
# p = Player(startPos[0],startPos[1],100,100,(0,255,0))
# p2 = Player(0,0,100,100,(255,0,0))


while run:
    message=""
    if m.getch():
        message=str(input("Type your message :>"))
    message_recieved = n.send(message)


    print("\t\t\t\t\t:>",message_recieved)
