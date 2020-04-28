num=int(input("enter the number to reverse  : "))
count=0
while num>0:
    num=num//10
    count+=1



temp=0
newnum=0
print(count)


while num:

    count=count-1

    temp=num%10
    print (temp)
    num=num//10

    newnum=newnum+(10**count)*temp

print("the reversed number : ",newnum)
