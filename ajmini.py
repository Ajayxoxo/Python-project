import os
import time 
import random

def display():
    
        print("***********__CANDY CRUSH ²__************")
        print("A knock off (BETA) for testers only")
        print("""
        
        
        """)
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                print(board[i][j],end=" ")
                    
            print() 
            for j in range(len(board[0])):
                 print(pointer[i][j],end=" ")
                 
            print()   
            
        """for i in range(len(board)):   
            print('✓',end=" ")"""
        print("Moves left : ",moves)
        print("Score : ",score)
        
            
def upseniche(i,j):
    while(i != 0):
        #print("in recursive",i)
        if(i>0):
            board[i][j],board[i][j+1],board[i][j+2]=board[i-1][j],board[i-1][j+1],board[i-1][j+2]
            upseniche(i-1,j)
            return
        else:
            return
     
def  pattern_finder():
    #for row 
    for i in range(len(pointer[0])):
        for j in range(len(pointer[0])-2):
            if(board[i][j]==board[i][j+1]==board[i][j+2]):
                #print(i,j,i+1,j,i+2,j)
                #print("pattern found at ")
                #time.sleep(7)
                upseniche(i,j)
                board[0][j]=random.choice("$%#*")
                board[0][j+1]=random.choice("$%#*")
                board[0][j+2]=random.choice("$%#*")
                #display()
                
            """  else:
                print("in else")
                print(board[i][j],board[i][j+1],board[i][j+2])"""
                

def swap_with():
    """print("here")
    here=[0,0]
    for i in range(len(pointer[0])):
        for j in range(len(pointer[0])):
            if(pointer[i][j]=='∆'):
                here=i,j
                print(here)"""
    
    nxt=input("Enter a character : ")
    
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if(pointer[i][j]=='^' ):
                #print(i,j)
                #print(i+1,j)
                if (nxt=='d' and j<len(board[0])-1):
                    board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
                    
                elif (nxt=='w' and i>0):   
                    board[i][j],board[i-1][j]=board[i-1][j],board[i][j]
                    
                elif (nxt=='s' and i<len(board[0])-1):   
                 #   print(pointer[i][j],pointer[i+1][j])
                    board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
                    
                elif (nxt=='a' and j>0):   
                    board[i][j],board[i][j-1]=board[i][j-1],board[i][j]
                else:
                    print("no change")       
                       
    pattern_finder()
                
    
def move():
    global moves
    nxt=input("Enter a character : ")
    moves=moves-1
    
    if(nxt=="p"):
        swap_with()
    else:    
      for i in range(len(pointer[0])):
        for j in range(len(pointer[0])):
            if(pointer[i][j]=='^'):
                #print(i,j)
                #print(i+1,j)
                if (nxt=='d' and j<len(pointer[0])-1):
                    pointer[i][j],pointer[i][j+1]=pointer[i][j+1],pointer[i][j]
                    
                elif (nxt=='w' and i>0):   
                    pointer[i][j],pointer[i-1][j]=pointer[i-1][j],pointer[i][j]
                    
                elif (nxt=='s' and i<len(pointer[0])-1):   
                 #   print(pointer[i][j],pointer[i+1][j])
                    pointer[i][j],pointer[i+1][j]=pointer[i+1][j],pointer[i][j]
                    moves-=1
                    
                elif (nxt=='a' and j>0):   
                    pointer[i][j],pointer[i][j-1]=pointer[i][j-1],pointer[i][j]
                else:
                    print("MOVE WASTED!!!!!!")   
                    time.sleep(0.5)
                    
                break

def recurse(i,j):
    while(i != 0):
        #print("in recursive",i)
            if(i>0):
                board[i][j]=board[i-1][j]
                recurse(i-1,j)
                return

def points():
    global score,moves
    
    i=len(board)-1
    for j in range(len(board)):
        if(board[i][j]=='*'):  
            score+=100     
            moves+=5
            recurse(i,j)
            board[0][j]=random.choice("$#%*")
            
            
a=1
opt="f"
moves =30
score=0
rows = 10
cols = 10 
values="$#%"
#print("mai sTart me kaise poch Gaya ")
#board = [[random.randint(1,3) for _ in range(cols)] for _ in range(rows)]
#letters='$#%'
board = [[random.choice(values) for _ in range(cols)] for _ in range(rows)]
    
pointer=[[ ' ' for _ in range(cols)]for _ in range(rows)]
pointer[0][0]='^'

"""for eachrow in pointer :
    print(eachrow)"""
    
def howtoplay() :
    os.system('clear')
    print("***********__CANDY CRUSH ²__************")
    print("A knock off (BETA) for testers only")
    print("""
        
        
        """)
        
    print("""
    Hello fellow gamer !!!
    wanna play the knock off version of candy crush 
    
    ABOUT: 
    The goal is to get scores as high as possible by 
    bringing down as much stars as possible 
    
    You have been given limited amount of moves 
    so play carefully.
    
    HOW TO PLAY :
    Use w,a,s,d to move your pointer 
        w - move up
        a - move left
        s - move down 
        d - move right 
    
        Use p to pick and enter w,a,s,d to swap the
        positions
    
   THINGS YPU NEED TO KNOW :
       *There is a higher penalty for using down key
       *You'll get extra moves if you bring down stars
    """)
    opt=input("Enter any key to go back ")
#menu

while(1):
    os.system('clear')
    
    print("***********__CANDY CRUSH ²__************")
    print("A knock off (BETA) for testers only")
    print("""
    1.START
    2.HOW TO PLAY
    3.EXIT
    """)
    option=(int(input("Enter a value ")))
    if(option==1):
        
        pattern_finder()
        pattern_finder()   
        while(moves>0):
            
            os.system('clear')
            points()
            display()
            move()
            time.sleep(0.2)
            
    
        display()    
        print("game finished")
        opt=input("Do you want to play again (y/n)")
        
                
    elif(option==2):
        howtoplay()
     
    elif(option==3):     
        option=input("are you sure ? :( (y/n)")
        if(option=='y'):
            print("Exiting the game")   
            break
          
        else  :
            continue
         
    else:
        print("Enter a valid input")     
    