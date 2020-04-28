import os
import time
import pygame
import msvcrt as m
pygame.init()
clock = pygame.time.Clock()
white=(255,255,255)
yellow=(245,207,15)
orange=(245,103,15)
black=(0,0,0)
green=(33,250,22)
size=100

draw_arr=[]
for i in range(0,600,int(600/size)):
    for j in range(0,600,int(600/size)):
        draw_arr.append((i,j))


class Node():


    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def rectangle(x,y,w,h,b_color):
    pygame.draw.line(gameDisplay,(255,255,255),(x,y),(x+w,y),1)
    pygame.draw.line(gameDisplay,(255,255,255),(x,y),(x,y+h),1)
    pygame.draw.line(gameDisplay,(255,255,255),(x+w,y),(x+w,y+h),1)
    pygame.draw.line(gameDisplay,(255,255,255),(x,y+h),(x+w,y+h),1)
    pygame.draw.rect(gameDisplay,b_color,(x,y,w,h))

def inside(cor,x,y,w,h):
    if(cor[0]>=x and cor[0]<=x+w) and (cor[1]>=y and cor[1]<=y+h):
        return True
    else:
        return False

def draw_grid():
    global draw_arr,visual_maze,size,start,end
    
    
    # while True:
    gameDisplay.fill((0,0,0))
   
        
        # rectangle(draw_arr[i][0],draw_arr[i][1],size,size,black)

    for i in range(size):
        for j in range(size):
            if abs(visual_maze[i][j])==3:
                rectangle(i*6,j*6,6,6,yellow)
   
            if abs(visual_maze[i][j])==2:
                rectangle(i*6,j*6,6,6,orange)
            if abs(visual_maze[i][j])==1:
                rectangle(i*6,j*6,6,6,white)
    master_flag=0
    # print(pygame.mouse.get_pos())
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.display.quit()
                master_flag=1
                break
            if master_flag==1:
                break
            if event.type==pygame.KEYDOWN:
                for i in range(10):
                    for j in range(10):
                        visual_maze[i][j]=(0)
    if master_flag==1:
        exit()

    pygame.draw.circle(gameDisplay,(255,0,0),(start[0]*6,start[1]*6),6)
    pygame.draw.circle(gameDisplay,(255,0,0),(end[0]*6,end[1]*6),6)
    pygame.display.update()


def astar(maze, start, end):

    global visual_maze,size
   
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    start_node2= Node(None, end)
    start_node2.g = start_node2.h = start_node2.f = 0
    end_node2 = Node(None, start)
    end_node2.g = end_node2.h = end_node2.f = 0

    open_list = []
    closed_list = []

    open_list2=[]
    closed_list2=[]

    
    open_list.append(start_node)

    open_list2.append(start_node2)
    pathfound=False
    pathfound1=False
    pathfound2=False
    while len(open_list) > 0 or len(open_list2)>0:

        
        current_node = open_list[0]
        current_node2=open_list2[0]

        current_index = 0
        current_index2=0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        for index, item in enumerate(open_list2):
            if item.f < current_node2.f:
                current_node2 = item
                current_index2 = index

       
        open_list.pop(current_index)
        closed_list.append(current_node)

        open_list2.pop(current_index2)
        closed_list2.append(current_node2)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:                
                path.append(current.position)
                current = current.parent
            p=path[::-1]
            pygame.display.update()
            for pos in p:
                rectangle(pos[0]*6,pos[1]*6,6,6,green)
            pygame.display.update()

            m.getch()
            return path[::-1] 
        if current_node2 == end_node2:
            path2 = []
            current = current_node2
            while current is not None:                
                path2.append(current.position)
                current = current.parent
            p=path2[::-1]
            pygame.display.update()
            for pos in p:
                rectangle(pos[0]*6,pos[1]*6,6,6,green)
            pygame.display.update()

            m.getch()
            return path[::-1] 
     
        if pathfound and pathfound2!=True:
            path = []
            current = current_node
            while current is not None:                
                path.append(current.position)
                current = current.parent
            p=path[::-1]
            pygame.display.update()
            for pos in p:
                rectangle(pos[0]*6,pos[1]*6,6,6,green)
            pygame.display.update()
            
            


            # m.getch()
            # return path[::-1] 

        if pathfound and pathfound1!=True:
            path2 = []
            current2 = current_node2
            while current2 is not None:                
                path2.append(current2.position)
                current2 = current2.parent
            p2=path2[::-1]
            pygame.display.update()
            for pos in p2:
                rectangle(pos[0]*6,pos[1]*6,6,6,green)
            pygame.display.update()

            m.getch()
            return path2[::-1] +path[::-1]



       
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

           
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            
            new_node = Node(current_node, node_position)

           
            children.append(new_node)

    
        for child in children:


            for closed_child in closed_list:
                if child == closed_child:
                    continue

           
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

    
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)

        children2 = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

           
            node_position2 = (current_node2.position[0] + new_position[0], current_node2.position[1] + new_position[1])

            
            if node_position2[0] > (len(maze) - 1) or node_position2[0] < 0 or node_position2[1] > (len(maze[len(maze)-1]) -1) or node_position2[1] < 0:
                continue

            
            if maze[node_position2[0]][node_position2[1]] != 0:
                continue

            
            new_node2 = Node(current_node2, node_position2)

           
            children2.append(new_node2)

    
        for child in children2:


            for closed_child in closed_list2:
                if child == closed_child:
                    continue

           
            child.g = current_node2.g + 1
            child.h = ((child.position[0] - end_node2.position[0]) ** 2) + ((child.position[1] - end_node2.position[1]) ** 2)
            child.f = child.g + child.h

    
            for open_node in open_list2:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list2.append(child)

        pathfound=False

        for way1 in closed_list:
            
            for way2 in closed_list2:
                
                if (way1.position[0]==way2.position[0]):
                    # print(way1.position,way2.position)
                    if way1.position[1]==way2.position[1]:
                        
                        pathfound=True
                        break
            if pathfound:
                break


        for way1 in open_list:

           
            if way1.position==end:
                pathfound1=True
        for way2 in open_list2:
            
            if way2.position==start:
                pathfound2=True


        for search in open_list:
            visual_maze[search.position[0]][search.position[1]]=2
        for found in closed_list:
            visual_maze[found.position[0]][found.position[1]]=3
        for search in open_list2:
            visual_maze[search.position[0]][search.position[1]]=-2
        for found in closed_list2:
            visual_maze[found.position[0]][found.position[1]]=-3

        for i in range(size):
            for j in range(size):
                if visual_maze[i][j]==2:
                    if visual_maze[i][j+1]==-3 or visual_maze[i][j-1]==-3 or visual_maze[i+1][j]==-3 or visual_maze[i-1][j]==-3 or visual_maze[i+1][j+1]==-3 or visual_maze[i+1][j-1]==-3 or visual_maze[i-1][j+1]==-3 or visual_maze[i-1][j-1]==-3:
                        pathfound=True


        draw_grid()
        
            
        # for i in range(size):
        #     print(visual_maze[i])

        # os.system("cls")

        # time.sleep(0.05)



    

if __name__ == '__main__':
    start=0
    wall=[]
    end=0
    flag=0
    l_exit=False
    gameDisplay = pygame.display.set_mode((600,600))
    while True:
        if pygame.mouse.get_pressed()==(1,0,0):
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(gameDisplay,white,pos,4)
            wall.append((pos[0]//6,pos[1]//6))
        if pygame.mouse.get_pressed()==(0,0,1):
            pos=pygame.mouse.get_pos()
            if flag==0:
                start=(pos[0]//6,pos[1]//6)
            else:
                end=(pos[0]//6,pos[1]//6)
            pygame.draw.circle(gameDisplay,(255,0,0),pos,6)
            flag=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                l_exit=True
                break
        if l_exit:
            break

        pygame.display.update()
    maze =[]
    gameDisplay = pygame.display.set_mode((600,600))
    gameExit=False
    for i in range(size):
        maze.append([])
    for i in range(size):
        for j in range(size):
            # if i==50 and j<=80:
            #     maze[i].append(1)
            # # if j==60 and i>=30 and i<=50:
            # #     maze[i].append(1)

            # else:

                maze[i].append(0)

    # for i in range(size):
    #     for j in range(size):
    #         if i==50 and j<=80:
    #             maze[i][j]=(1)
    #         if j==60 and i>=30 and i<=50:
    #             maze[i][j]=(1)

    for w in wall:
        maze[w[0]][w[1]]=1

    
   

    visual_maze=maze

    gameDisplay = pygame.display.set_mode((600,600))
    # draw_grid()

    

    path3 = astar(maze, start, end)

   


    # print(path)

