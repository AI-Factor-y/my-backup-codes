import random
total=0
h=0
one=0
two=0
three=0
four=0
five=0
six=0
seven=0
eight=0
nine=0
ten=0
run=True
val=0
large=0
win=0
loss=0
prob_one=0
prob_two=0
prob_three=0
prob_four=0
prob_five=0
prob_six=0
prob_seven=0
prob_eight=0
prob_nine=0
prob_ten=0
number=0
while(number<=1000):

    h=random.randint(1,10)

    comp_guess=[]
    

    large=max(prob_one,prob_two,prob_three,prob_four,prob_five,prob_six,prob_seven,prob_eight,prob_nine,prob_ten)
    print("\n")
    if (large==0):
        print("first trial... jsut starting to learn ")
    else:
        if (large==prob_one):
            print("the number with more chance is : 1    with probability of :",prob_one)
            comp_guess.append(1)
        if large==prob_two:
            print("the number with more chance is : 2    with probability of :",prob_two)
            comp_guess.append(2)
        if large==prob_three:
            print("the number with more chance is : 3    with probability of :",prob_three)
            comp_guess.append(3)
        if large==prob_four:
            print("the number with more chance is : 4    with probability of :",prob_four)
            comp_guess.append(4)
        if large==prob_five:
            print("the number with more chance is : 5    with probability of :",prob_five)
            comp_guess.append(5)
        if large==prob_six:
            print("the number with more chance is : 6    with probability of :",prob_six)
            comp_guess.append(6)
            
        if large==prob_seven:
            print("the number with more chance is : 7    with probability of :",prob_seven)
            comp_guess.append(7)
        if large==prob_eight:
            print("the number with more chance is : 8    with probability of :",prob_eight)
            comp_guess.append(8)
        if large==prob_nine:
            print("the number with more chance is : 9    with probability of :",prob_nine)
            comp_guess.append(9)
        if large==prob_ten:
            print("the number with more chance is : 10    with probability of :",prob_ten)
            comp_guess.append(10)

    if h==1:
        one=one+1
    if h==2:
        two=two+1
    if h==3:
        three=three+1
    if h==4:
        four=four+1
    if h==5:
        five=five+1
    if h==6:
        six=six+1
    if h==7:
        seven=seven+1
    if h==8:
        eight=eight+1
    if h==9:
        nine=nine+1
    if h==10:
        ten=ten+1

    total=total+1
    
    prob_one=one/total
    prob_two=two/total
    prob_three=three/total
    prob_four=four/total
    prob_five=five/total
    prob_six=six/total
    prob_seven=seven/total
    prob_eight=eight/total
    prob_nine=nine/total
    prob_ten=ten/total




#end case

    
    if large!=0:
        val=random.choice(comp_guess)
        if number==val:
            print("\n hurray its correct")
            win=win+1
            print("computer chose : ",val)
            
        else:
            print("\n ohh mann incorrect")
            print("computer chose : ",val)

            print("\n the correct is : ",h)
            loss=loss+1

    print("\n\n win : ",win)
    print("loss  :",loss)

    number=number+1
    



print("\n\n\n",one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)
print(ten)


        
        
        
    
        
    



    
        

    
