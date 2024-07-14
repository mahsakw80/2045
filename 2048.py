import random
import pygame
import sys
from pygame.locals import *

class Game2048:
    def __init__(self):
        self.board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.gameOver=False
        self.move=True
        self.correct_move=0
        self.wingame=False
        self.record=2
# A Function for add number 2 or 4 (80% and 20%)
    def AddNumber_2_4(self,once=True): #how_many is (True or False) a number of numbers that you want add
        if(once==True):                # if it was False we need numbers for first boart(start Game)
            if(random.randint(1,10)<3): # choice 4 --> 20%
                addnumber=4
            else:                       # choice 2 --> 80%
                addnumber=2
            #choice a place for a random number,we shuld check there was 0.
            not_zero=True
            while (not_zero):    
                row=random.randint(0,3)
                col=random.randint(0, 3)
                if(self.board[row][col]==0):
                    self.board[row][col]=addnumber
                    not_zero=False   
        elif(once==False):
            #this part is for start the game
            #First Number:
            if (random.randint(1, 10) < 3):  # choice 4 --> 20%
                first_addnumber = 4
            else:                            # choice 2 --> 80%
                first_addnumber = 2
            #Second Number:
            if (random.randint(1, 10) < 3):  # choice 4 --> 20%
                second_addnumber = 4
            else:                            # choice 2 --> 80%
                second_addnumber = 2    
            #choice a place for first random number
            first_row = random.randint(0, 3)
            first_col = random.randint(0, 3)
            self.board[first_row][first_col] = first_addnumber
            #after choice a first place,we shouhd check that the places was't equal
            equal=True
            while(equal):
                #choice a place for second random number
                second_row = random.randint(0, 3)
                second_col = random.randint(0, 3)
                if(second_row==first_row and second_col==first_col):
                    pass
                else:
                    self.board[second_row][second_col] = second_addnumber
                    equal=False
        else:
            pass            
        return self.board    
#A Function for move on the row(left or right)
    def move_on_row(self,command):
        move_numbers=[]
        row1=[]
        row2=[]
        row3=[]
        row4=[]
        for row in range(4):
            for col in range(4):
                if(self.board[row][col]!=0):
                    if(row==0):
                        #List of zero opposite numbers in the first row
                        row1.append(self.board[row][col])
                    elif(row==1):
                        #List of zero opposite numbers in the second row    
                        row2.append(self.board[row][col])
                    elif(row==2):
                        #List of zero opposite numbers in the third row    
                        row3.append(self.board[row][col])
                    elif(row==3):
                        #List of zero opposite numbers in the fourth row    
                        row4.append(self.board[row][col])
        if(command=='l'):
            row1+=[0]*(4-len(row1))
            row2+=[0]*(4-len(row2))
            row3+=[0]*(4-len(row3))
            row4+=[0]*(4-len(row4))
            move_numbers=[row1]+[row2]+[row3]+[row4]


        elif(command=='r'):
            row_1=[0]*(4-len(row1))+row1
            row_2=[0]*(4-len(row2))+row2
            row_3=[0]*(4-len(row3))+row3
            row_4=[0]*(4-len(row4))+row4
            move_numbers=[row_1]+[row_2]+[row_3]+[row_4]
        else:
            pass
        
        self.board=move_numbers    
        return self.board
#A Function for move on the column(up or down)
    def move_on_col(self,command):
        change=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        move_numbers=[]
        col1=[]
        col2=[]
        col3=[]
        col4=[]
        for row in range(4):
            for col in range(4):
                if(self.board[row][col]!=0):
                    if(col==0):
                        #List of zero opposite numbers in the first column
                        col1.append(self.board[row][col])
                    elif(col==1):
                        #List of zero opposite numbers in the second column    
                        col2.append(self.board[row][col])
                    elif(col==2):
                        #List of zero opposite numbers in the third column    
                        col3.append(self.board[row][col])
                    elif(col==3):
                        #List of zero opposite numbers in the fourth column    
                        col4.append(self.board[row][col])
        if(command=='u'):
            col1+=[0]*(4-len(col1))
            col2+=[0]*(4-len(col2))
            col3+=[0]*(4-len(col3))
            col4+=[0]*(4-len(col4))
            move_numbers=[col1]+[col2]+[col3]+[col4]
        elif(command=='d'):
            col_1=[0]*(4-len(col1))+col1
            col_2=[0]*(4-len(col2))+col2
            col_3=[0]*(4-len(col3))+col3
            col_4=[0]*(4-len(col4))+col4
            move_numbers=[col_1]+[col_2]+[col_3]+[col_4]
        else:
            pass
        
        for i in range(4):
            for j in range(4):
                change[i][j]=move_numbers[j][i]
        self.board=change    
        return self.board   
#َA Function for add numbers side by side
    def add_together(self,whitch):
        check_move=self.board.copy()
        if whitch=='row l':
            for i in range(4):
                for j in range(3):
                        if self.board[i][j]!=0 and self.board[i][j]==self.board[i][j+1]:
                            self.board[i][j]*=2
                            self.board[i][j+1]=0
        if whitch=='row r':
            for i in range(4):
                for j in range(3):
                        if self.board[i][3-j]!=0 and self.board[i][3-j]==self.board[i][2-j]:
                            self.board[i][3-j]*=2
                            self.board[i][2-j]=0                    
                             
        if whitch=='col u':
            for i in range(3):
                for j in range(4):
                        if self.board[i][j]!=0 and self.board[i][j]==self.board[i+1][j]:
                            self.board[i][j]*=2
                            self.board[i+1][j]=0
        if whitch=='col d':
            for i in range(3):
                for j in range(4):
                        I=3-i
                        if self.board[3-i][j]!=0 and self.board[3-i][j]==self.board[2-i][j]:
                            self.board[3-i][j]*=2
                            self.board[2-i][j]=0                    
        if self.board!=check_move:
            self.move=False                               
        return self.board,self.move
#A Function for check move    
    def checkMove(self,check):
        if self.board!=check:
            self.move=True
            self.correct_move+=1
        elif self.board==check:
            self.move=False
        return self.move,self.correct_move
#Record section
    def max(self):
        for i in range(4):
            for j in range(4):                               
                if self.board[i][j]>self.record:
                    self.record=self.board[i][j]
        return self.record                
#A Function for check "game over"    
    def game_over(self):
        checkplay=0
        zero=0
        for i in range(4):
            for j in range(4):                               
                if self.board[i][j]==2048:
                    checkplay=-1
        if  checkplay==-1:
            self.gameOver=True
            self.wingame=True                      
        elif checkplay!=-1:
            for i in range(4):
                for j in range(4):                               
                    if self.board[i][j]==0:
                        zero+=1
            if zero==0:            
                for i in range(4):
                    for j in range(3):
                        if self.board[i][j]!=0 and self.board[i][j]==self.board[i][j+1]:
                            checkplay+=1
                for i in range(3):
                        for j in range(4):
                            if self.board[i][j]!=0 and self.board[i][j]==self.board[i+1][j]:
                                checkplay+=1
                if checkplay==0:
                    self.gameOver=True
                    self.wingame=False

                               
        return self.gameOver,self.wingame                                           
#main function of the game    
    def play_2048(self,keyboard):
        check_move=self.board.copy()
        if keyboard=='w':
            self.move_on_col('u')
            self.add_together('col u')
            self.move_on_col('u')
            self.checkMove(check_move)
            if self.move==True:
                self.AddNumber_2_4()
        if keyboard=='s':
            self.move_on_col('d')
            self.add_together('col d')
            self.move_on_col('d')
            self.checkMove(check_move)
            if self.move==True:
                self.AddNumber_2_4()
        if keyboard=='d':
            self.move_on_row('r')
            self.add_together('row r')
            self.move_on_row('r')
            self.checkMove(check_move)
            if self.move==True:
                self.AddNumber_2_4()
        if keyboard=='a':
            self.move_on_row('l')
            self.add_together('row l')
            self.move_on_row('l')
            self.checkMove(check_move)
            if self.move==True:
                self.AddNumber_2_4()
        self.game_over()        
        return self.board
               
        
#Build game graphics            
pygame.init()           
#set a caption
pygame.display.set_caption('2048')
#set an icon 
icon=pygame.image.load('icon (1).png')
pygame.display.set_icon(icon)
#build a window
win=pygame.display.set_mode((500,500))
#set a background
bg=pygame.image.load("bg.jpg")
backG=pygame.transform.scale(bg,(500,500))
win.blit(backG,(0,0))
#set a toll for game(that's image)
tool=pygame.image.load("Capture.png")
Tool=pygame.transform.scale(tool,(300,300))
win.blit(Tool,(100,100))
#The fonts 
fonT=pygame.font.Font(None,30)
font1=pygame.font.Font(None,25)
#A Function for show the board on tool
def show(window,brd):
    win.blit(Tool,(100,100))
    color={0:(225,225,225),2:(153,102,255),4:(153,153,225),8:(147,112,219),16:(123,104,238),
           32:(106,90,205),64:(72,61,139),128:(138,43,226),256:(102,51,153),
           512:(127,0,225),1024:(93,63,211),2048:(128,0,128)}
    loc_x_y={0:130,1:205,2:280,3:355}

    for i in range(4):
        for j in range(4):
            if brd[i][j]!=0:
                text=str(brd[i][j])
            else:
                text=' '
            clr=brd[i][j]                
            txt=fonT.render(text,True,color[clr])
            x=((len(text)-1)*5)
            win.blit(txt,(loc_x_y[j]-x,loc_x_y[i]))
#creat a game
game=Game2048()
game.AddNumber_2_4(False)
show(win,game.board)
exit=False
reset=False
play=True
lock=False
lc=False
#main loop   
while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if game.gameOver==False:
                if play:
                    if event.key==K_w:
                        game.play_2048('w')
                        show(win,game.board)
                    if event.key==K_s:
                        game.play_2048('s')
                        show(win,game.board)
                    if event.key==K_a:
                        game.play_2048('a')
                        show(win,game.board)
                    if event.key==K_d:
                        game.play_2048('d')
                        show(win,game.board)      
            if lock==False:                                           
                if event.key==K_r and exit==False:
                    lock=True
                    play=False
                    reset=True
                    ask_rs=pygame.image.load("reset.jpg")
                    askreset=pygame.transform.scale(ask_rs,(400,200))
                    win.blit(askreset,(50,150)) 
                    crctmv=font1.render(f'{game.correct_move}',True,(225,225,225))
                    win.blit(crctmv,(205,220))
                    game.max()
                    rcrd=font1.render(f'{game.record}',True,(225,225,225))
                    win.blit(rcrd,(370,220))
                if event.key==K_q and reset==False:
                    lock=True
                    play=False         
                    ask_ex=pygame.image.load("exit.jpg")
                    askexit=pygame.transform.scale(ask_ex,(400,200))
                    win.blit(askexit,(50,150))
                    crctmv=font1.render(f'{game.correct_move}',True,(225,225,225))
                    win.blit(crctmv,(205,220))
                    game.max()
                    rcrd=font1.render(f'{game.record}',True,(225,225,225))
                    win.blit(rcrd,(370,220))
                    exit=True    
            if reset==True and event.key==K_y:
                    lock=False
                    play=True
                    game=Game2048()
                    game.AddNumber_2_4(False)
                    win.blit(backG,(0,0))          
                    win.blit(Tool,(100,100))
                    show(win,game.board)
                    reset=False
                    lc=False
            if reset==True and event.key==K_n:
                    lock=False
                    play=True
                    win.blit(backG,(0,0))          
                    win.blit(Tool,(100,100))
                    show(win,game.board)
                    reset=False
                    lc=False
                
            if exit==True and event.key==K_y:
                    pygame.quit()
                    sys.exit()
            if exit==True and event.key==K_n:
                    lock=False
                    play=True
                    win.blit(backG,(0,0))          
                    win.blit(Tool,(100,100))
                    show(win,game.board)
                    exit=False 
                    lc=False         
        if game.gameOver==True and lc==False:
                if game.wingame==True:
                    wn=fonT.render('Game over. You win!',True,(51,0,102))
                    win.blit(wn,(150,50))
                    lc=True
                elif game.wingame==False:
                    fonT=pygame.font.Font(None,30)
                    ls=fonT.render('Game over. You lose!',True,(51,0,102))
                    win.blit(ls,(150,50))
                    lc=True            
            
    pygame.display.update()      
        