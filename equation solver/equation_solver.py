
while(True):

    try:
    
        print("\n\n")
        varno=int(input("enter the number of variables ( 0 to exit ): "))
        if(varno==0):
            break

        mat=[]

        for i in range(varno+1):
                  mat.append([])
        print("EQUATION SOLVER")

        print("enter the variables (enter 0 to exit) ")

        for i in range(varno):


                  print("enter the variables of equation ( including constant term) : "+str(i+1))

                  for j in range(varno+1):
                  
                      print("enter value of ",end=" ")
                      print((chr(ord('A')+j)))
                      val=int(input())
                      mat[i].append(val)


        def interchanger(a):
            for b in range(varno+1):
                swap=mat[a][b]
                mat[a][b]=mat[varno-1][b]
                mat[varno-1][b]=swap


        def matprint():
            for i in range(varno):
                print(mat[i])
        print("Augumented matrix : ")
        print("---------------------")

        matprint()

        temp=0
        for k in range(varno-1):
            
            if(mat[k][k]==0):
                interchanger(k)
                
            for i in range(1+k,varno):
                
                temp=mat[i][k]/mat[k][k]
                for j in range(0,varno+1):

                   
                    mat[i][j]=mat[i][j]-temp*mat[k][j]
                    
                    
        print("gausiian matrix used for solution matrix :")
        print("--------------------")



        matprint()

        flag=0
        sol=[]
        sumer=0
        sol.append(mat[varno-1][varno]/mat[varno-1][varno-1])
        level=varno-1
        while(level>0):
              sumer=0
              
              flag=flag+1
              level=level-1
              n=1
              while(n<=flag):
                  sumer=sumer+mat[level][varno-n]*sol[n-1]
                  n=n+1
             
              sol.append(((mat[level][varno])+(-1*(sumer)))/mat[level][level])
            
        sol.reverse()
        print("\n\n")
        for i in range(len(sol)):
            print((chr(ord('A')+i)),end=" ")
            print(" : ",end=" ")
            print(sol[i])

    except ZeroDivisionError:
        print("\n\n")
        print("______________________________________________________________")
        print("the system of equations is inconsistent and no solution exists")
        print("--------------------------------------------------------------")
