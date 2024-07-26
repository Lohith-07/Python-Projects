def game(in1,in2):
    if in1==in2:
        print("It's A Tie")
        return None
    elif (in1==1 and in2==2) or (in1==2 and in2==3) or (in1==3 and in2==1):
        return in2
    else:
        return in1
print("This Is Rock Paper Scissor Game\nThe Game Rules Are as Follows\nIf The Clash Is\tRock vs Paper->Paper Wins\n\t\tPaper vs Scissor->Scissor Wins\n\t\tScissor vs Rock->Rock Wins")
print("Enter  1 For Rock\n\t2 for paper\n\t3 for scissor")
ch=input("Are You Ready To Play(If Not Enter 'n'or'N\n")
while ch!='n' and ch!='N':
    pal1=int(input("Clash Your Friend:Select 1/2/3\t"))
    pal2=int(input("Clash Your Friend:Select 1/2/3\t"))
    if pal1 in [1,2,3] and pal2 in [1,2,3]:
        r=game(pal1,pal2)
        if r==1:    
             print("Rock Wins")
        elif r==2:  
            print("Paper Wins")
        elif r==3:
            print("scisssor Wins")
    else:
        print("Invalid Choice Try Again")
    ch=input("Do You Want To Continue y or n\n")
print("Thanks For Playing We Hope You Enjoyed Our Game")

