## GUESS WORK MAIN PROGRAM

## MAIN IMPORTS
from tkinter import *
from PIL import (Image , ImageTk)



## STARTING PAGE
class Start_Page():
    def __init__(self):
        start = Frame(window , background='royalblue')
        start.grid( row =0,column=0 ,sticky='nsew')

        
        #methods
        def NameData(event):
            name = Name_input.get()
            
            #Appending the names
            ScoreFile = open("Score of Players.txt",'a')
            Dataname = '{:<20}'.format(name)
            ScoreFile.write(Dataname)
            ScoreFile.close()

            #Play Button
            Play = Button(start,text="Play",bg='seagreen',width=10,font="Ariel 12", relief ='raised',command= lambda: swap(Game_Page))
            Play.grid(row =6 , column =0 ,ipadx=5 ,ipady=5)

            

        def start_Pic():
            canvas = Canvas(start , width = 500 , height = 370 , bg= 'royalblue',bd=0,highlightthickness=0 )
            canvas.grid(column = 2 , row = 5, sticky = 'se')
            img = Image.open("gamer.png")
            tkpic = ImageTk.PhotoImage(img)
            canvas.create_image(200,200,anchor= 'center' ,image=tkpic )
            canvas.image = tkpic


            
        #Label for start
        label = Label(start,text="Welcome to Guess Work \n\nLet's have some fun!!" , bg = 'royalblue',font="Ariel 20 bold" ,width=20, height=4)
        label.grid(row=0 , column=0,padx=5,sticky='nw')

        # Label for name input
        Name_label = Label(start,text="Enter your name" , bg = 'royalblue' ,font="Ariel 14 " ,width=15, height = 2)
        Name_label.grid(row =2 ,column=0,sticky="w")

        # Input for name
        Name_input = Entry(start,width=30, bg="white")
        Name_input.bind('<Return>',NameData)
        Name_input.grid(row=3 ,padx=20 , sticky="w")
      
        #Picture for start page
        start_Pic()


        #Score_Board Button
        Score = Button(start,text="Score Board",bg='lightblue',width=10,font="Ariel 12", relief ='raised',command= lambda: swap(Score_Board))
        Score.grid(row=6 , column=1 ,ipadx=5 ,ipady=5)

        #Quit Button
        Quit = Button(start,text="Quit",bg='red',width=10,font="Ariel 12", relief ='raised', command= window.destroy)
        Quit.grid(row=6 ,column= 2,ipadx=5 ,ipady=5 )

        #Help Button
        Help = Button(start,text="Help",bg='salmon',width=10,font="Ariel 12", relief ='raised', command= lambda: swap(Help_Page))
        Help.grid(row=0 ,column= 2,ipadx=5 ,ipady=5 )
        
        start.tkraise()



class Game_Page():
    def __init__(self):
        import threading
        import time
        
        
        Game = Frame(window , background='violetred1')
        Game.grid(row=0,column=0,sticky='nsew')
        
        # methods
        def chara_Pic():
            canvas = Canvas(Game , width = 300 , height = 300 , bg= 'violetred1',highlightthickness=0 )
            canvas.grid(column = 4,columnspan=2, row = 3,rowspan=2, sticky = 'se')
            img = Image.open("catgame.png")
            tkpic = ImageTk.PhotoImage(img)
            canvas.create_image(150,150,anchor= 'center' ,image=tkpic )
            canvas.image = tkpic
            
        # threading lets you do multitasking
        def run_in_background(func, *args):
            global endTime
            if not endTime:
                self.thread = threading.Thread(target=func, args=args)
                self.thread.start()
            else:
                self.thread.join()
                

        # Players answer
        def Player_Ans(event):
            self.P_Ans = Ans_input.get()
            Ans_input.delete(0,'end')

        # Actual Answer
        def Answers(number):
            filename = "level_"+str(number)+"Answers.txt"
            FileAns = open(filename,'r')
            Ans = FileAns.read()
            FileAns.close()
            return Ans

        #Game clock
        def clock(sec_left):
            # declare variable
            self.P_Ans =''
            
            Time = Frame(Game)
            Time.grid(row=1,column=4)

            Tlabell = Label(Time,background='yellow',font='Arial 12',width=10 ,height=2 )
            Tlabell.grid(row = 0 , column = 0,sticky='ne')

            seconds =''
            while sec_left > -1 and self.P_Ans == '':
                seconds = str(sec_left)
                timeformat = (seconds).zfill(2)
                Tlabell['text']= 'Time left :' + timeformat
                time.sleep(1)
                sec_left -= 1
            else:
                return seconds

        # Game Over message
        def Game_Over():
            Game_over = Frame(Game, background='red4',relief ='raised',height =2)
            Game_over.grid(row=3,column=3,sticky='n')

            Game_label1=Label(Game_over ,bg='firebrick1', text ='Game Over!!',font = "Arial 16 bold")
            Game_label2=Label(Game_over ,bg='firebrick1', text ='Do you want to see your score?',font = "Arial 12 bold")
            Game_label1.grid(row=0 ,column=0 ,columnspan=2 ,pady =2)
            Game_label2.grid(row=1 ,column=0 ,columnspan=2 ,pady =2)

            Game_Button1 = Button(Game_over,text ='Yes',bg="firebrick1",font="Arial 10",width=5 ,height=2, command =lambda : swap(Score_Board))
            Game_Button1.grid(row =2 ,column=0,pady=10)
            Game_Button2 = Button(Game_over , text ='No',bg="firebrick1",font="Arial 10",width=5 ,height=2, command =lambda : swap(Start_Page))
            Game_Button2.grid(row =2 ,column=1, pady=10)

        # Game Won message
        def Game_Won():
            Game_Won = Frame(Game, background='gold',relief ='raised',height =2)
            Game_Won.grid(row=3,column=3,sticky='n')

            Game_label1=Label(Game_Won ,bg='gold', text ='WINNER!! ',font = "Arial 16 bold")
            Game_label2=Label(Game_Won ,bg='gold', text ='Do you want to see your score?',font = "Arial 12 bold")
            Game_label1.grid(row=0 ,column=0 ,columnspan=2 ,pady =2)
            Game_label2.grid(row=1 ,column=0 ,columnspan=2 ,pady =2)

            Game_Button1 = Button(Game_Won,text ='Yes',bg="lightgoldenrod",font="Arial 10",width=5 ,height=2, command =lambda : swap(Score_Board))
            Game_Button1.grid(row =2 ,column=0,pady=10)
            Game_Button2 = Button(Game_Won , text ='No',bg="lightgoldenrod",font="Arial 10",width=5 ,height=2, command =lambda : swap(Start_Page))
            Game_Button2.grid(row =2 ,column=1, pady=10)

            
        # LEVELS for the Game

        def level_1():
            import Level_1
            Level_1.random_function(self.turtle_screen)
                
        def level_2():
            import Level_2
            Level_2.random_function(self.turtle_screen)



        #Label for Game 
        label = Label(Game,text='Guess!!',font='Ariel 12 bold',bg='violetred1' ,width=5,justify='left')
        label.grid(row=0 ,column=0)

        #Character picture
        chara_Pic()
        
        # turtle
        self.turtle_screen = Canvas(Game, width=550,height=500 ,highlightthickness=10 , relief='sunken')
        self.turtle_screen.grid(column =0, row=1 ,columnspan=4,rowspan=4 )
        

        # Label for ANSWER input
        Ans_label = Label(Game,text="Enter your answer" , bg = 'violetred1' ,font="Ariel 14 " ,width=15)
        Ans_label.grid(row =5 ,column=0,sticky="sw")


        # Input for ANSWER
        Ans_input = Entry(Game,width=30, bg="white" )
        Ans_input.grid(row=6 ,column=0,padx=20 , sticky="w")
        Ans_input.bind('<Return>',Player_Ans)

        #Start_Page Button
        Main = Button(Game,text="Back",bg='red',width=10,font="Ariel 12",command= lambda: swap(Start_Page))
        Main.grid(row =6 , column =4 ,ipadx=3 ,ipady=3)

        # Loop for levels

        score = 0               #variable to store score of player
        cond = True
        game = 'lost'
        while cond == True :
            for Lvl in range(1,10+1):
                global endTime
                endTime = False
                
                if Lvl== 1:
                    countdown = run_in_background(clock ,13)
                    level_1()
                    Ans =  Answers(Lvl)
                    
                    
                    if self.P_Ans == Ans and countdown != '0':
                        score += 10
                        
                        
                    elif self.P_Ans != Ans :
                        break

                elif Lvl== 2:
                    countdown = run_in_background(clock,10)
                    level_2()
                    Ans = Answers(Lvl)
                    
                    if self.P_Ans == Ans and countdown != '0':
                        score += 10
                        game = 'won'
                    else :
                        break
                    
                endTime = True
                    
            cond = False

        else:
            # appending score into Score of Players file
            ScoreFile = open("Score of Players.txt",'a')
            Data = '{:>8}'.format(score)
            
            ScoreFile.write(Data+'\n')
            ScoreFile.close()

            if game == 'won':
                Game_Won()

            else:
                Game_Over()

            
        Game.tkraise()



## Score Board of the Game
class Score_Board():
    def __init__(self):
        Score = Frame(window , background='deepskyblue')
        Score.grid(row=0,column=0,sticky='nsew')

        # methods
        def Score_Pic():
            canvas = Canvas(Score , width = 300 , height = 300 , bg= 'deepskyblue',highlightthickness=0 )
            canvas.grid(column = 5,columnspan=2, row = 2,rowspan=2, sticky = 'se')
            img = Image.open("snows.png")
            tkpic = ImageTk.PhotoImage(img)
            canvas.create_image(150,170,anchor= 'center' ,image=tkpic )
            canvas.image = tkpic

        # THE SCORE BOARD FOR GAME
        def Score_Table():
            # Reading Score of players file
            with open("Score of Players.txt",'r') as Data:
                ScoreFile = Data.read()
                
            with open("Score of Players.txt",'r') as Data:
                lines = sum (1 for line in Data)

            
            maximum = 0
            with open("Score of Players.txt",'r') as topScorer:
                for i in range(lines):
                    string = topScorer.readline()
                    numbers=''
                    name=''
                    for k in string:
                        if k.isalpha():
                            name +=k
                      
                        if k.isdigit():
                            numbers += k
                            nums = int(numbers)
                            maximum = max(maximum ,nums)

                    if nums>=maximum:
                        topper = name
                        score = str(maximum)
                       
                

            # Table Frame
            Table = Frame(Score ,height = 500 , width = 400,bd=5, background='lightblue' )
            Table.grid(row = 1 , column = 1,rowspan=2,columnspan=2,sticky='nw')
            Table.grid_propagate(0)

            # Text widget
            ScoreData = Text(Table ,bg='deepskyblue3')
            ScoreData.grid(row =1 ,column =0,columnspan = 5)
            ScoreData.insert(END,"Name\t\t\tScore\n\n")
            ScoreData.insert(END, ScoreFile)

            TopScorer = StringVar()
            topScorer = Label(Table , text='Top Player : ')
            topScorer.grid(row =2 , column = 0)
            topName = Label(Table ,textvariable = TopScorer)
            TopScorer.set(topper)
            topName.grid(row=2 , column = 1)
            
    
            Table.tkraise()

            

        #Label for Score
        label_score = Label(Score,text='Score Board',font='Ariel 16 bold',bg='deepskyblue' ,width=10,justify='left')
        label_score.grid(row=0 ,column=0)

        #Table for recording score
        Score_Table()

        # picture
        Score_Pic()

        #Quit Button
        Quit = Button(Score,text="Quit",bg='red',width=10,font="Ariel 12", command= window.destroy)
        Quit.grid(row=5 ,column= 2,padx=5 ,pady=10 ,ipadx=5 ,ipady=5 )

        #Back Button
        Back = Button(Score,text="Back",bg='green',width=10,font="Ariel 12",command= lambda: swap(Start_Page))
        Back.grid(row =5 , column =0 ,padx=5 ,pady=10 ,ipadx=5 ,ipady=5)

        Score.tkraise()


class Help_Page():
    def __init__(self):
        Help = Frame(window , background='AntiqueWhite2')
        Help.grid(row=0,column=0,sticky='nsew')

        def Help_Pic():
            canvas = Canvas(Help , width = 300 , height = 300 , bg= 'AntiqueWhite2',highlightthickness=0 )
            canvas.grid(column = 0,columnspan=2, row = 4,rowspan=3)
            img = Image.open("help.png")
            tkpic = ImageTk.PhotoImage(img)
            canvas.create_image(100,110,anchor= 'center' ,image=tkpic )
            canvas.image = tkpic

        with open("Help.txt",'r') as DATA:
             Guide = DATA.read()

        #Label for Help
        label_help = Label(Help,text='GUIDE',font='Ariel 16 bold',bg='AntiqueWhite2')
        label_help.grid(row=0 ,column=0)


        # Table Frame
        Table = Frame(Help ,height = 400 , width = 660,bd=5, background='AntiqueWhite3' )
        Table.grid(row = 1 , column = 1,rowspan=3,columnspan=4,sticky='nw')
        Table.grid_propagate(0)

        # Text widget
        GuideBook = Text(Table ,bg='PeachPuff3')
        GuideBook.grid(row =0 ,column =0)
        GuideBook.insert(END,Guide)

        #Back Button
        Back = Button(Help,text="Back",bg='MistyRose2',width=10,font="Ariel 12",command= lambda: swap(Start_Page))
        Back.grid(row =5 , column =4 ,padx=5 ,pady=10 ,ipadx=5 ,ipady=5)

        Help_Pic()

        Help.tkraise()
        

## change pages
def swap(Func):
    Func()


## starting window

window = Tk()
window.title("Guess Work")
window.iconbitmap("icon.ico")
window.geometry('800x630+200+0')
window.config(bg='white')

Start_Page()

window.mainloop()


