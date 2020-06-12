
"""Important  Notice:-
    
    Sometimes Some Unwanted Things Occur In Player Vs Player Mode.
    If You Notice Some Thing Like That Please Take A Screen Shoot And Mail Me at hrishikesh.pgh.patra@gmail.com
    Or Just Put A Comment Or Create A Issue In This Github Repository.
    
    
    Your Idle May Be Show
    ----> Undefined variable: 'g_gameEnd' at line [440,8] <----- This Warning 
    Don't Panic This Is Not An Error & This Warning Doesn't Create Any Problem.
    
    In Source Folder You Can Find This --> libmpg123.dll <--- File
    If You Want You Can Delete This File, This Is Only For Fix libmpg123.dll error In Pyinstaller.
    
    
                                                                            Thank You
                                                                        Hrishikesh Patra"""





#Import Modules

import tkinter.messagebox
from tkinter import *
import _thread
import random
import os,sys
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  #<- Hide Pygame Wellcome Prompt
from pygame import mixer
import webbrowser

#Default Music Sound And Full Mute State
Music = "Normal"
Sounds = "Normal"
all_sound = "Normal"

#Initialized  Computer Score Player Score & Draw

cowon = 0
playwon = 0
dr = 0


def getAbsoluteResourcePath(relative_path):  #<- Collect Current Patch and add to source folder path
    CurrentPath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    spriteFolderPath = os.path.join(CurrentPath, 'Source')
    path = os.path.join(spriteFolderPath, relative_path)
    newPath = path.replace(os.sep, '/')
    return newPath


#...........main window...........
x = getAbsoluteResourcePath("back1.mp3")             #<- Back ground Music (Player vs Computer)
y = getAbsoluteResourcePath("back2.mp3")              #<- Back ground Music (Player vs Player)

back_musics = [x, y]                #<- For toggle background music base on situation
mixer.init()                    #<- Initialized pygame mixer module 
p_back = False

def play_next_back_musics(which):           #<--- change Background Music When call
    if p_back == True:
        back_musics_play = (back_musics[which])
        mixer.music.load(back_musics_play)
        mixer.music.play(-1)            #<------------------ Play Bg Music In Loop

mixer.music.set_volume(0.10)        #<------------------ Set Bg Music Volume


#Load Various sounds 

human_turn = mixer.Sound(getAbsoluteResourcePath("human.wav"))
pc_turn = mixer.Sound(getAbsoluteResourcePath("pc.wav"))
X_turn = mixer.Sound(getAbsoluteResourcePath("xTone.wav"))
O_turn = mixer.Sound(getAbsoluteResourcePath("OTone.wav"))
win_in_pc_sound = mixer.Sound(getAbsoluteResourcePath("win1.wav"))
win_sound = mixer.Sound(getAbsoluteResourcePath("win.wav"))
lost_sound = mixer.Sound(getAbsoluteResourcePath("lose.wav"))
draw_sound = mixer.Sound(getAbsoluteResourcePath("draw.wav"))
draw_sound2 = mixer.Sound(getAbsoluteResourcePath("draw1.wav"))

def center_window(name,w=300, h=200):    #<---- Open Tkinter Window In Center Of Screen 
    # get screen width and height
    ws = name.winfo_screenwidth()
    hs = name.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/3) - (h/2)              #<---------- Change y = (hs/3) to y = (hs/2) for perfectly centered 
    name.geometry('%dx%d+%d+%d' % (w, h, x, y))



org = Tk()              #<------------- Main Tk Window
center_window(org,620,450)              #<------------- Main Tk Centred


mainWnd = Frame(org)    #<-- Main Game Frame 
mainWnd.place(x=0,y=0)
tictac = Frame(org)  #<--  Main Frame For PvP

org.wm_title("Tic Tac Toe")          #<--  Set Window Title
org.iconbitmap(getAbsoluteResourcePath("Game.ico"))       #<--  Set Window Icon

#Default Massage's

cowon2 = StringVar()
cowon2.set("Computer Won 0")

dr2 = StringVar()
dr2.set("Draw 0")

pname1 = StringVar()
pname1.set("X")
pname2 = StringVar()
player1_name = pname1.get()
player2_name = pname2.get()



playwon2 = StringVar()
playwon2.set("\n\n"+ player1_name+" Won 0")

#Gif Paths and size

gif1 = Label(org, height="446", width="443")
gif3 = Label(org, height="446", width="443")
gif2 = Label(org, height="446", width="443")
gif_player1  = Label(org, height="446", width="443")
gif_player2  = Label(org, height="446", width="443")

gif_win_frame = [PhotoImage(file=(getAbsoluteResourcePath("Win.gif")),format = 'gif -index %i' % (i)) for i in range(5)]
def gif_win(ind):

    frame = gif_win_frame[ind]
    ind += 1
    if ind >= 5:
        ind = 0
    gif1.configure(image=frame)
    org.after(180, gif_win, ind)


gif_win(0)


gif_player1_win_frame = [PhotoImage(file=(getAbsoluteResourcePath("p1.gif")),format = 'gif -index %i' % (i)) for i in range(5)]
def gif_p1_win(ind):

    frame = gif_player1_win_frame[ind]
    ind += 1
    if ind >= 5:
        ind = 0
    gif_player1.configure(image=frame)
    org.after(180, gif_p1_win, ind)


gif_p1_win(0)


gif_player2_win_frame = [PhotoImage(file=(getAbsoluteResourcePath("p2.gif")),format = 'gif -index %i' % (i)) for i in range(5)]
def gif_p2_win(ind):

    frame = gif_player2_win_frame[ind]
    ind += 1
    if ind >= 5:
        ind = 0
    gif_player2.configure(image=frame)
    org.after(180, gif_p2_win, ind)

gif_p2_win(0)

gif_lost_frame = [PhotoImage(file=(getAbsoluteResourcePath("Lose.gif")),format = 'gif -index %i' % (i)) for i in range(4)]
def gif_lost(ind):

    frame = gif_lost_frame[ind]
    ind += 1
    if ind >= 4:
        ind = 0
    gif2.configure(image=frame)
    org.after(160, gif_lost, ind)


gif_lost(0)


gif_draw_frame = [PhotoImage(file=(getAbsoluteResourcePath("Draw.gif")),format = 'gif -index %i' % (i)) for i in range(40)]
def gif_draw(ind):

    frame = gif_draw_frame[ind]
    ind += 1
    if ind >= 40:
        ind = 0
    gif3.configure(image=frame)
    org.after(30, gif_draw, ind)

gif_draw(0)


def setname(n):  #Ask Player Name On 1st Time Player 1 & 2 and hide main window when ask name window open 
    
    icon2 = (getAbsoluteResourcePath("Avatar.ico"))
    global player1_name
    global player2_name
    global p_back
    
    if (pname1.get() == "X" and n == 1):
        org2 =Tk()
        org2.attributes('-topmost', True)
        mixer.music.pause()
        org2.iconbitmap(icon2)
        center_window(org2,290,80)
        org2.configure(bg='old lace')
        org2.wm_title("Player1 Name")
        org2.resizable(width=False, height =False)
        org.withdraw()
        l1 = Label(org2,text="Enter Player Name",font=("mv boli","11"),bg='old lace')
        l1.pack(side=LEFT)
        e1 = Entry(org2,font=("lucida handwriting","10"))
        e1.focus()
        e1.pack(side=RIGHT)
        def ch():
            global p_back
            global player1_name
            if e1.get()!= "":
                player1_name =str(e1.get())
                playwon2.set("\n\n"+ player1_name+" Won 0")
                player_info.config(text = player1_name +" are Player 1 'X'\n\n")
                p_back = True
                play_next_back_musics(0)
                #mixer.music.unpause()
                org2.destroy()
                org.deiconify()
                
        b = Button(org2,text="Ok",bg='alice blue',font=("Harrington","10"),command=ch)
        b.place(x=138,y=53)
    if (pname2.get() =="" and player2_name == "" and n == 2 ):
        org2 =Tk()
        org2.attributes('-topmost', True)
        mixer.music.pause()
        org2.iconbitmap(icon2)
        center_window(org2,290,80)
        #org2.geometry("290x80")
        org2.wm_title("Player2 Name")
        org2.configure(bg='old lace')
        org2.resizable(width=False, height =False)
        org.withdraw()
        l2 = Label(org2,text="Enter Player2 Name",font=("mv boli","11"),bg='old lace')
        l2.pack(side=LEFT)
        e2 = Entry(org2,font=("lucida handwriting","10"))
        e2.focus()
        e2.pack(side=RIGHT)
        def ch2():
            global player2_name
            if e2.get()!= "":
                    player2_name =str(e2.get())
                    level_i2.config(text=(player1_name + " vs " + player2_name))
                    player_i1.config(text=(player1_name + " Is 'X'"))
                    player_i2.config(text=(player2_name + " Is 'O'\n\n"))
                    w1.set(player1_name +" Win's 0")
                    w2.set(player2_name +" Win's 0")
                    play_next_back_musics(1)
                    mixer.music.unpause()
                    org2.destroy()
                    org.deiconify()
                    
        b = Button(org2,text="Ok",bg='alice blue',font=("Harrington","10"),command=ch2)
        b.place(x=138,y=53)
    def _delete_window():
        ask = messagebox.askquestion("Confirmation","Do You Want To Exit ?",icon='warning')
        if ask == 'yes':
            org.destroy()
            org2.destroy()
        else:
            pass
    try:
        org2.protocol("WM_DELETE_WINDOW", _delete_window)
    except:
        org.update()

setname(1)      #Ask Player Name For 1st Time and For Player 1

 #For Exit Window Confermation
def _delete_window2():     
    ask = messagebox.askquestion("Confirmation","Do You Want To Exit ?",icon='warning')
    if ask == 'yes':
        try:
            org.destroy()
        except:
            pass

org.protocol("WM_DELETE_WINDOW", _delete_window2)

pl1 = IntVar()
def changePlayer(_var,_menu):   #Player Changer Between X and O in Game
    global g_player1
    g_player1 = pl1
    _playas = ["Player 1 'X'","Player 2 'O'"]
    _menu.entryconfigure(0,label=_playas[0])
    _menu.entryconfigure(1,label=_playas[1])

    _menu.entryconfigure(_var,label=_playas[_var]+" <--")
    player_info.config(text = player1_name+" are "+_playas[_var] +"\n\n" )
    reset_game(0)



def changeLevel(_var,_menu):        #Game Deficits and Player vs Player Selector
    
    global g_menu_level
    g_menu_level = _var
    _levels = ["Easy","Medium","Hard","Player vs Player"]

    _menu.entryconfigure(0,label=_levels[0])
    _menu.entryconfigure(1,label=_levels[1])
    _menu.entryconfigure(2,label=_levels[2])
    _menu.entryconfigure(3,label=_levels[3])


    _menu.entryconfigure(_var,label=_levels[_var]+" <--")

    level_info.config(text ="Level : "+_levels[_var] )
    reset_game(0)





def update_aimsg(var):      #For Show Random Commentary In Game

    default = ["Common I don't have whole day","It's your move. I'm waiting.....","Please use your brain and move fast. I have other places to go."]

    draw = ["Keep calm It's a Tie","It's a Tie. Rematch?"]

    lost = ["My CPU is not feeling well today. That's why you won.","It's your lucky day.","You Cheater...","Do not let this match go to your head.","Yeah.. you won. so what?"]

    won = ["Now get ready for my slave army you brainless human.","Never come to play with me again","You need practice.. Ha Ha Ha...","Do not worry, better luck next time.","Try Easy Level"]

    compliment = ["Well done..","Nice","Verry Good","You are Inteligent"]

    insult = ["Never come to play with me again"]

    trapped = ["Get ready to loose","Do whatever you can do to win this one.","You got trapped","Do not get Demotivated, but you are going to loose.","Do not worry","Bad move","just think before you make mistakes, like this one.","You can't win this one.","Now I own this game"]

    blocked=["Not so fast.","You can't win that easily."]

    if(var=="default"):
        string = default[random.randint(0,len(default)-1)]
    elif(var=="draw"):
        string = draw[random.randint(0,len(draw)-1)]
    elif(var=="lost"):
        _thread.start_new_thread( gif_show,(172,1,1))       #<- Call Gif S_how 
        string = lost[random.randint(0,len(lost)-1)]

    elif(var=="won"):
        _thread.start_new_thread( gif_show,(172,1,2))       #<- Call Gif S_how 
        string = won[random.randint(0,len(won)-1)]
        
        
    elif(var=="insult"):
        string = insult[random.randint(0,len(insult)-1)]
    elif(var=="compliment"):
        string = compliment[random.randint(0,len(compliment)-1)]
    elif(var=="trapped"):
        string = trapped[random.randint(0,len(trapped)-1)]
    elif(var=="blocked"):
        string = blocked[random.randint(0,len(blocked)-1)]

    ai_msg.config(text=string)



def guimsg_set_gamewinner(_str):  #Show Game Status
    game_stat.config(text =_str)




def showmessage():  #<---- About Section Massage
    tkinter.messagebox.showinfo('About Tic Tac Toe','Made by Hrishikesh Patra\nAny Feedback or Requirements: \nmail me->  hrishikesh.pgh.patra@gmail.com')

def motion(event):   #Get Mouse Click Position When Click On Board 
    _x, _y = event.x, event.y
    if (_x>50 and _x<390 and _y>50 and _y<390 and abs(_x-170)>10 and abs(_x-290)>10 and abs(_y-160)>10 and abs(_y-290)>10 ):

        if(_x<170 and _x>50):
            _x=0
        if(_x<290 and _x>170):
            _x=1
        if(_x<390 and _x>290):
            _x=2

        if(_y<160 and _y>50):
            _y=0
        if(_y<290 and _y>160):
            _y=1
        if(_y<390 and _y>290):
            _y=2

        user_clicked(_y,_x)


def reset_game(event):      #<---- Reset Fame Button (Main)

    play_next_back_musics(0)
    mainWnd.place(x=0,y=0)
    tictac.forget()
    gif1.place(x=500,y=500)
    gif2.place(x=500,y=500)
    gif3.place(x=500,y=500)
    gif_player1.place(x=500,y=500)
    gif_player2.place(x=500,y=500)
    global g_gameEnd
    global g_player1
    g_winner =-1
    g_gameEnd=0
    g_chance=0
    for i in range(3):
        for j in range(3):
            g_game_grid[i][j]=-1

    bgcanvas.delete("all")
    board_img = bgcanvas.create_image(b_image_pos,b_image_pos,image=object_img_board)
    guimsg_set_gamewinner("Game is Running...")
    update_aimsg("default")
    if(g_player1==1):
        user_clicked(-5,0)

def user_clicked(_r,_c):  #<-------- Get Mouse Click Position On (0,0)so on ................
    global g_gameEnd
    global dr
    global cowon
    global playwon
    _ai_is_player1 = _r
    # Computer Turn
    if(_ai_is_player1==-5):
        _r=0
    if(g_gameEnd==0 and g_game_grid[_r][_c] ==-1 ):
        if(_ai_is_player1!=-5):
            g_game_grid[_r][_c] = g_player1
            put_piece(g_player1,_r,_c,0)

        _stat = check_game_status(return_list(g_game_grid))

        if(_stat==-1):
            _move = runai(g_player1)
            g_game_grid[_move[0]][_move[1]] = int(not(g_player1))
            _thread.start_new_thread( put_piece,(int(not(g_player1)), _move[0],_move[1],0.2))
            
            
        else:  #<------ Game Over 
            g_gameEnd = 1

        _stat = check_game_status(return_list(g_game_grid))
        if(_stat==5):
            update_aimsg("draw")
            guimsg_set_gamewinner("Draw")
            dr += 1
            dr2.set("Draw "+str(dr))
            if Sounds == "Normal" and all_sound == "Normal":
                draw_sound.play()
            _thread.start_new_thread( gif_show,(172,1,3))
        
        if(_stat==int(not(g_player1))):
            update_aimsg("won")
            guimsg_set_gamewinner(player1_name+" Loose..")
            cowon += 1
            cowon2.set("Computer Won "+str(cowon))
            if Sounds == "Normal" and all_sound == "Normal":
                time.sleep(1)
                lost_sound.play()
        if(_stat==g_player1):
            update_aimsg("lost")
            guimsg_set_gamewinner(player1_name+" won..")
            if Sounds == "Normal" and all_sound == "Normal":
                win_in_pc_sound.play()
            playwon += 1
            playwon2.set("\n\n"+player1_name+" Won "+str(playwon))

            

        if(_stat!=-1):
            g_gameEnd=1

def return_list(_mainlist):  #<---------------- Get Cordinate For Game
    _tmplist = [[-1] *3 for n in range(3)]
    for i in range(3):
        for j in range(3):
            _tmplist[i][j] = _mainlist[i][j]

    return _tmplist




def put_piece(_player,_r,_c,_delay):  #<---------------- Set X,O Image On Board 
    time.sleep(0.6)
    if(_player == 0):
        if Sounds == "Normal" and all_sound == "Normal":
            human_turn.play()
        _image = bgcanvas.create_image(img_pos_x +(_c*offset),img_pos_y + (_r*offset),image=object_img_red)

    else:
        time.sleep(0.6)
        if Sounds == "Normal" and all_sound == "Normal":
            pc_turn.play()
        _image = bgcanvas.create_image(img_pos_x +4+(_c*offset),img_pos_y + (_r*offset),image=object_img_blue)


def check_game_status(_tmp_g_game_grid):  #<-------------- Game Cordinate For Turn
    for i in range(3):
        if( _tmp_g_game_grid[i][0] == _tmp_g_game_grid[i][1] and _tmp_g_game_grid[i][1] == _tmp_g_game_grid[i][2] and _tmp_g_game_grid[i][2] != -1  ):
            return _tmp_g_game_grid[i][2]

    for i in range(3):
        if( _tmp_g_game_grid[0][i] == _tmp_g_game_grid[1][i] and _tmp_g_game_grid[1][i] == _tmp_g_game_grid[2][i] and _tmp_g_game_grid[2][i] != -1  ):
            return _tmp_g_game_grid[2][i]

    if( _tmp_g_game_grid[0][0] == _tmp_g_game_grid[1][1] and _tmp_g_game_grid[1][1] == _tmp_g_game_grid[2][2] and _tmp_g_game_grid[2][2] != -1  ):
        return _tmp_g_game_grid[2][2]

    if( _tmp_g_game_grid[0][2] == _tmp_g_game_grid[1][1] and _tmp_g_game_grid[1][1] == _tmp_g_game_grid[2][0] and _tmp_g_game_grid[2][0] != -1  ):
        return _tmp_g_game_grid[2][0]
#.......................draw...............

    for i in range(3):
        for j in range(3):
            if(_tmp_g_game_grid[i][j]==-1):
                return -1

    return 5




def runai(_user):  #<--- Run AI
    global g_game_grid
    _ai = int(not _user)


#.........special case...........only for legendary..........
    if(g_menu_level>=2):
        _legendmoves = legend_ai(return_list(g_game_grid), _user,1)
        if(_legendmoves[0]!=-1):
            return _legendmoves[0],_legendmoves[1]


#..........check if I can Win in this move
    if(g_menu_level>=0):
        for i in range(3):
            for j in range(3):
                if(g_game_grid[i][(j+1)%3]==_ai and g_game_grid[i][(j+2)%3]==_ai and g_game_grid[i][(j+3)%3]!=_user ):
                    return i,(j+3)%3

        for i in range(3):
            for j in range(3):
                if(g_game_grid[(j+1)%3][i]==_ai and g_game_grid[(j+2)%3][i]==_ai and g_game_grid[(j+3)%3][i]!=_user ):
                    return (j+3)%3,i


        for i in range(3):
            if(g_game_grid[(i+1)%3][(i+1)%3]==_ai and g_game_grid[(i+2)%3][(i+2)%3]==_ai and g_game_grid[(i+3)%3][(i+3)%3]!=_user ):
                    return (i+3)%3,(i+3)%3

                    #.........diagonal 1
        for i in range(3):
            if(g_game_grid[(i+1)%3][(i+1)%3]==_ai and g_game_grid[(i+2)%3][(i+2)%3]==_ai and g_game_grid[(i+3)%3][(i+3)%3]!=_user ):
                    return (i+3)%3,(i+3)%3


                    #.........diagonal 2
        for i in range(3):
            if(g_game_grid[0][2]==_ai and g_game_grid[2][0]==_ai and g_game_grid[1][1]!=_user ):
                    return 1,1
            if(g_game_grid[1][1]==_ai and g_game_grid[2][0]==_ai and g_game_grid[0][2]!=_user ):
                    return 0,2
            if(g_game_grid[0][2]==_ai and g_game_grid[1][1]==_ai and g_game_grid[2][0]!=_user ):
                    return 2,0


    update_aimsg("blocked")

# .......check if user can win in this move..............
    if(g_menu_level>=1):
        for i in range(3):
            for j in range(3):
                if(g_game_grid[i][(j+1)%3]==_user and g_game_grid[i][(j+2)%3]==_user and g_game_grid[i][(j+3)%3]!=_ai ):
                    return i,(j+3)%3

        for i in range(3):
            for j in range(3):
                if(g_game_grid[(j+1)%3][i]==_user and g_game_grid[(j+2)%3][i]==_user and g_game_grid[(j+3)%3][i]!=_ai ):
                    return (j+3)%3,i

    #.........diagonal 1
        for i in range(3):
            if(g_game_grid[(i+1)%3][(i+1)%3]==_user and g_game_grid[(i+2)%3][(i+2)%3]==_user and g_game_grid[(i+3)%3][(i+3)%3]!=_ai ):
                    return (i+3)%3,(i+3)%3


    #.........diagonal 2
        for i in range(3):
            if(g_game_grid[0][2]==_user and g_game_grid[2][0]==_user and g_game_grid[1][1]!=_ai ):
                    return 1,1
            if(g_game_grid[1][1]==_user and g_game_grid[2][0]==_user and g_game_grid[0][2]!=_ai ):
                    return 0,2
            if(g_game_grid[0][2]==_user and g_game_grid[1][1]==_user and g_game_grid[2][0]!=_ai ):
                    return 2,0



    update_aimsg("default")

#...........choose centre if available
    if(g_menu_level>=1):
        if g_game_grid[1][1]==-1:
            return 1,1



#.....default case..ai choose  random location ............................


    if(g_menu_level>=0):
        i = random.randint(0,3)
        j = random.randint(0,3)
        for i1 in range(3):
            for j1 in range(3):
                if g_game_grid[(i+i1)%3][(j+j1)%3]==-1:
                    return (i+i1)%3,(j+j1)%3



#.......MIN MAX Algorithm .................................
def legend_ai(_local_grid, _opponent, _chance):
    if(_local_grid[1][1]==-1):
        return 1,1
    _min = 100000; _i_max =1; _j_max=1;
    for _i1 in range(3):
        for _j1 in range(3):
            if(_local_grid[_i1][_j1]==-1):
                _tmp = min_max_search( return_list(_local_grid), _i1,_j1,_opponent,_chance,0)
                _total = _tmp[0] + _tmp[1] + _tmp[2]
                if(_total!=0):
                    if( (_tmp[2]*100)/_total< _min ):
                        _min = (_tmp[2]*100)/_total
                        _i_max= _i1
                        _j_max = _j1

    return _i_max,_j_max

def min_max_search(_local_grid, i1_,j1_, _opponent, _chance,_lvl):
    #return won,draw,lost
    #if(_lvl>1):
        #return 0
    _ai = int(not _opponent)

#if ai wins return 1
    if(_chance==1):
        _local_grid[i1_][j1_] = _ai
        for i in range(3):
            for j in range(3):
                if (_local_grid[i][j]==-1):
                    tmp = return_list(_local_grid)
                    tmp[i][j] = _opponent
                    _stat = check_game_status(return_list(tmp))
                    if(_stat == _opponent):
                        return 0,0,1
    else:
        #if opponent wins return -1
        _local_grid[i1_][j1_] = _opponent
        for i in range(3):
            for j in range(3):
                if (_local_grid[i][j]==-1):
                    tmp = return_list(_local_grid)
                    tmp[i][j] = _ai
                    _stat = check_game_status(return_list(tmp))
                    if(_stat == _ai):
                        return 1,0,0

    _stat = check_game_status(return_list(_local_grid))
    if(_stat == 5):                 #if grid is full and draw return 0
        return 0,1,0

    _sum =[0,0,0]
    for i in range(3):
        for j in range(3):
            if(_local_grid[i][j]==-1):
                _tmp= min_max_search(return_list(_local_grid), i, j,_opponent,int(not _chance),_lvl+1)
                _sum[0]+=_tmp[0]
                _sum[1]+=_tmp[1]
                _sum[2]+=_tmp[2]

    return _sum






#.............toolbar.............

menu_bar = Menu(org, tearoff=False)
org.config(menu = menu_bar)


submenu_levels = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Levels",menu=submenu_levels)








submenu_player = Menu(menu_bar, tearoff=False)


sounds_option = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Volume",menu=sounds_option)


submenu_contact = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Contact",menu=submenu_contact)



menu_bar.add_command(label="About", command=showmessage)






#.............options frame left side part of main wnd.............

option_frame = Frame(mainWnd, bg="#21252b", height="450", width="170",highlightthickness=1,highlightbackground ="#1a181f", relief=RAISED )
option_frame.pack(side=LEFT, fill=None, expand=False)
option_frame.pack_propagate(0)



game_name = Label(option_frame, text="T I C  T A C  T O E\n",bg ="#21252b",fg="#e97263", font=("Arial","13","bold"))
game_name.pack()

restart_btn = Button(option_frame, text="RESET", font=("Helvetica","17","bold"),bg ="#4285fa", fg ="white",bd=0)
restart_btn.pack()
restart_btn.config(height=1, width=7)
restart_btn.bind('<Button-1>', reset_game)

lb = Label(option_frame, text="",bg ="#21252b",fg="#9da5b4", font=("Arial","1"))
lb.pack()
playas = Label(option_frame, text="Play \nAs  ",bg ="#21252b",fg="#9da5b4", font=("Arial","11"))
playas.place(x=2,y=100)


pl1.set(0)
r1 = Radiobutton(option_frame, text="Player 1 'X'",bg ="#21252b",fg="#9da5b4", font=("Arial","11"),pady=1, variable=pl1, value=0,command = lambda: changePlayer(0,submenu_player))
r1.pack()
r2 = Radiobutton(option_frame, text="Player 2 'O'",bg ="#21252b",fg="#9da5b4", font=("Arial","11"),pady=1, variable=pl1, value=1,command = lambda: changePlayer(1,submenu_player))
r2.pack()


level_info = Label(option_frame, text="Level : Easy",bg ="#21252b",fg="#9da5b4", font=("Arial","11"),pady=15)
level_info.pack()

player_info = Label(option_frame, text= (player1_name +" are Player 1 'X'\n\n"),bg ="#21252b",fg="#9da5b4", font=("Arial","11"))
player_info.pack()


ai_msg = Label(option_frame, text="It's your move. I'm waiting.......",bg ="#21252b",fg="#4285fa", font=("Arial","11"),wraplength="150")
ai_msg.pack()


game_scp = Label(option_frame, textvariable=playwon2,bg ="#21252b",fg="light slate blue", font=("castellar","12"))
game_scp.pack()
game_scc = Label(option_frame, textvariable=cowon2,bg ="#21252b",fg="light slate blue", font=("castellar","11"))
game_scc.pack()
game_scd = Label(option_frame, textvariable=dr2,bg ="#21252b",fg="light slate blue", font=("castellar","12"))
game_scd.pack()


game_stat = Label(option_frame, text="You Won\n",bg ="#21252b",fg="green", font=("Arial","11"))
game_stat.pack(side=BOTTOM)



#.............game frame right side part of main window or main gui.............

game_frame = Frame(mainWnd, bg="#282c34", height="450", width="450", relief=SUNKEN)
game_frame.pack_propagate(0)
game_frame.pack(side=LEFT)


#.................main canvas where images get drawn..............
canvas_size =450
bgcanvas = Canvas(game_frame, width=canvas_size,height=canvas_size,highlightthickness=0,bg="#282c34")
bgcanvas.pack()
bgcanvas.bind('<Button-1>', motion)

#.............background_image.............
object_img_board = PhotoImage(file=getAbsoluteResourcePath("tictactoeboard.png"))
b_image_pos = canvas_size/2
board_img = bgcanvas.create_image(b_image_pos,b_image_pos,image=object_img_board)
#.............objects on board.............

object_img_blue = PhotoImage(file=getAbsoluteResourcePath("O.png"))
object_img_red = PhotoImage(file=getAbsoluteResourcePath("X.png"))

img_pos_x =100
img_pos_y=100

offset = 126

#...................game variables....................

g_player1 =0 #red one
g_winner =-1
g_gameEnd=0
g_chance=0
g_game_grid = [[-1] *3 for n in range(3)] #initial state
g_menu_level = 0
g_menu_playas = 0
t01 = 0
ti1 = 0
w10 = 0
w20 = 0
changeLevel(0,submenu_levels)






sideframe = Frame(tictac, bg="#21252b", height="500", width="170",highlightthickness=1,highlightbackground ="#1a181f", relief=RAISED)
sideframe.pack(side=LEFT, fill=None, expand=False)
sideframe.pack_propagate(0)

#.............game frame right side part of main window or main gui.............

gamewind = Frame(tictac, bg="#282c34", height="448", width="450", relief=SUNKEN)
gamewind.pack_propagate(0)
gamewind.pack(side=LEFT)


#Set Default Values 


pa = StringVar()
playerb = StringVar()
who = StringVar()
mov = StringVar()
to = StringVar()
to.set("\nTotal Match 0")
w1 = StringVar()
w1.set(player1_name +" Win's 0")
w2 = StringVar()
w2.set(player2_name +" Win's 0")
ti = StringVar()
ti.set("Tie Match 0")

bclick = True
flag = 0

def disableButton():   #<------ Disable All Button On Game Over Button 
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)






def btnClick(buttons):     #<------------Get Button Number And Check For Win And Who Win
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        mov.set(player2_name + "'s Turn ('O')")
        if Sounds == "Normal" and all_sound == "Normal":
            O_turn.play()
        playerb = player2_name + " Wins!"
        pa = player1_name + " Wins!"
        checkForWin()
        flag += 1



    if buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        mov.set(player1_name + "'s Turn ('X')")
        if Sounds == "Normal" and all_sound == "Normal":
            X_turn.play()
        checkForWin()
        flag += 1


def checkForWin():     #<------------Check Win Based On Conditions Main Problem.........................................
    global w10
    global w20
    global ti1
    who.set("Game Running.......")
    if(button1['text'] == 'X' and button2['text'] == 'X' and button6['text'] == 'X' and button7['text'] == 'X' and button9['text'] == 'X' or flag == 8):
        who.set("It is a Tie")
        ti1 += 1
        ti.set("Tie Match "+str(ti1))
        mov.set("Game Over "+"It is a Tie")
        _thread.start_new_thread( gif_show,(172,1,3))
        if Sounds == "Normal" and all_sound == "Normal":
            draw_sound2.play()
    
    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        mov.set("Game Over "+pa)
        _thread.start_new_thread( gif_show,(172,1,4))
        who.set(pa)
        w10 += 1
        w1.set(player1_name +" Win's "+str(w10))
        #_thread.start_new_thread( gif_show,(172,1,3))
        if Sounds == "Normal" and all_sound == "Normal":
            win_sound.play()

    elif(flag == 8):
        who.set("It is a Tie")
        ti1 += 1
        ti.set("Tie Match "+str(ti1))
        _thread.start_new_thread( gif_show,(172,1,3))
        if Sounds == "Normal" and all_sound == "Normal":
            draw_sound2.play()
        mov.set("Game Over "+"It is a Tie")

        
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        who.set("Game Running.......")
        disableButton()
        mov.set("Game Over "+playerb)
        _thread.start_new_thread( gif_show,(172,1,5))
        who.set(playerb)
        w20 += 1
        w2.set(player2_name +" Win's "+str(w20))
        if Sounds == "Normal" and all_sound == "Normal":
            win_sound.play()


buttons = StringVar()


#light sky blue4


#Buttons Configuration's Main 

button1 = Button(gamewind, text=" ", font='Times 58 bold', bg='#282c34', fg='pale turquoise', height=0, width=3, command=lambda: btnClick(button1),relief=SUNKEN)
button1.grid(row=3, column=0)

button2 = Button(gamewind, text=' ', font='Times 58 bold', bg='#282c34', fg='pale turquoise', height=0, width=3, command=lambda: btnClick(button2),relief=SUNKEN)
button2.grid(row=3, column=1)

button3 = Button(gamewind, text=' ', font='Times 58 bold', bg='#282c34', fg='pale turquoise', height=0, width=3, command=lambda: btnClick(button3),relief=SUNKEN)
button3.grid(row=3, column=2)

button4 = Button(gamewind, text=' ', font='Times 58 bold', bg='#282c34', fg='pale turquoise', height=0, width=3, command=lambda: btnClick(button4),relief=SUNKEN)
button4.grid(row=4, column=0)

button5 = Button(gamewind, text=' ', font='Times 58 bold', bg='#282c34', fg='pale turquoise', height=0, width=3, command=lambda: btnClick(button5),relief=SUNKEN)
button5.grid(row=4, column=1)

button6 = Button(gamewind, text=' ', font='Times 58 bold', bg='#282c34', fg='pale turquoise', height=0, width=3, command=lambda: btnClick(button6),relief=SUNKEN)
button6.grid(row=4, column=2)

button7 = Button(gamewind, text=' ', font='Times 58 bold', bg='#282c34', fg='pale turquoise', height=0, width=3, command=lambda: btnClick(button7),relief=SUNKEN)
button7.grid(row=5, column=0)

button8 = Button(gamewind, text=' ', font='Times 58 bold', bg='#282c34', fg='pale turquoise', height=0, width=3, command=lambda: btnClick(button8),relief=SUNKEN)
button8.grid(row=5, column=1)

button9 = Button(gamewind, text=' ', font='Times 58 bold', bg='#282c34', fg='pale turquoise', height=0, width=3, command=lambda: btnClick(button9),relief=SUNKEN)
button9.grid(row=5, column=2)

def reset_game3():   #Rest Game On Change Level Only
    play_next_back_musics(1)
    setname(2)
    global flag 
    global bclick
    gif1.place(x=500,y=500)
    gif2.place(x=500,y=500)
    gif3.place(x=500,y=500)
    gif_player1.place(x=500,y=500)
    gif_player2.place(x=500,y=500)
    flag = 0
    bclick = True
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)
    mov.set(player1_name + "'s Turn ('X')")
    who.set("As Usual 1st Player is \n 'X' " )

def reset_game2():   #Rest Game On Rest Button Clicked
    global flag 
    global bclick
    global t01
    global ti1
    gif1.place(x=500,y=500)
    gif2.place(x=500,y=500)
    gif3.place(x=500,y=500)
    gif_player1.place(x=500,y=500)
    gif_player2.place(x=500,y=500)
    
    flag = 0
    bclick = True
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)
    mov.set(player1_name + "'s Turn ('X')")
    who.set("As Usual 1st Player is \n 'X' " )
    t01 += 1
    to.set("\nTotal Match "+str(t01))


#Side Frames Configartion

blan = Label(sideframe, text=" /",bg ="#21252b",fg="#21252b", font=("Arial","14","bold"))
blan.pack()

TicTitelBig = Label(sideframe, text="T I C  T A C  T O E\n",bg ="#21252b",fg="#e97263", font=("Arial","13","bold"))
TicTitelBig.pack()

restart_bt2 = Button(sideframe, text="RESET", font=("Helvetica","17","bold"),bg ="#4285fa", fg ="white",bd=0,command=reset_game2)
restart_bt2.pack()
restart_bt2.config(height=1, width=7)


level_i2 = Label(sideframe, text=(player1_name + " vs " + player2_name),bg ="#21252b",fg="#9da5b4", font=("Arial","11"),pady=15)
level_i2.pack()

player_i1 = Label(sideframe, text=(player1_name + " Is 'X'"),bg ="#21252b",fg="#9da5b4", font=("Arial","11"))
player_i1.pack()

player_i2 = Label(sideframe, text=(player2_name + " Is 'O'\n\n"),bg ="#21252b",fg="#9da5b4", font=("Arial","11"))
player_i2.pack()





if mov.get() == "":  #Set Who's Turn
    mov.set(player1_name + "'s Turn ('X')")


ai_msg2 = Label(sideframe, textvariable=mov,bg ="#21252b",fg="#4285fa", font=("Arial","11"),wraplength="150")
ai_msg2.pack()

if who.get() == "": # Set 1st Massage
    who.set("As Usual 1st Player is \n 'X' " )

#Side Frames Configurations
blacn2 = Label(sideframe, text="",bg ="#21252b",fg="#4285fa", font=("Arial","6"),wraplength="150")
blacn2.pack()

toMatch = Label(sideframe, textvariable=to,bg ="#21252b",fg="light slate blue", font=("Fixedsys","16"))
toMatch.pack()
wl1 = Label(sideframe, textvariable=w1,bg ="#21252b",fg="light slate blue", font=("Fixedsys","16"))
wl1.pack()
wl2 = Label(sideframe, textvariable=w2,bg ="#21252b",fg="light slate blue", font=("Fixedsys","16"))
wl2.pack()
timatch = Label(sideframe, textvariable=ti,bg ="#21252b",fg="light slate blue", font=("Fixedsys","16"))
timatch.pack()



game_stat2 = Label(sideframe, textvariable=who, bg ="#21252b",fg="green", font=("Arial","11"))
game_stat2.pack(side=BOTTOM)

def pvp(_var,_menu):   #Menu Bar Select Level Configurations
    global g_menu_level
    g_menu_level = _var
    _levels = ["Easy","Medium","Hard","Player vs Player"]

    _menu.entryconfigure(0,label=_levels[0])
    _menu.entryconfigure(1,label=_levels[1])
    _menu.entryconfigure(2,label=_levels[2])
    _menu.entryconfigure(3,label=_levels[3])


    _menu.entryconfigure(_var,label=_levels[_var]+" <--")
    reset_game3()
    tictac.pack()

submenu_levels.add_command(label="Easy <--", command = lambda: changeLevel(0,submenu_levels))
submenu_levels.add_command(label="Medium",command = lambda: changeLevel(1,submenu_levels))
submenu_levels.add_command(label="Hard", command = lambda: changeLevel(2,submenu_levels))
submenu_levels.add_command(label="Player vs Player", command = lambda: pvp(3,submenu_levels))

def sound_state_change(_var,_menu):  #Menu Bar Volume Changing Configuration
    global Music,Sounds,all_sound
    _levels = ["Music Un-Mute","Sounds Un-Mute","Un-Mute"]
    _levels2 = ["Music Mute","Sounds Mute","Mute"]
    if _var == 0 and Music == "Normal":
        _menu.entryconfigure(_var,label=_levels[_var])
        mixer.music.set_volume(0.00)
        Music = "Music Mute"
    elif _var == 0 and Music == "Music Mute" and all_sound == "Normal":
        _menu.entryconfigure(_var,label=_levels2[_var])
        mixer.music.set_volume(0.10)
        Music = "Normal"
    if _var == 1 and Sounds == "Normal":
        _menu.entryconfigure(_var,label=_levels[_var])
        Sounds = "Sounds Mute"
    elif _var == 1 and Sounds == "Sounds Mute" and all_sound == "Normal":
        _menu.entryconfigure(_var,label=_levels2[_var])
        Sounds = "Normal"
    if Music == "Music Mute" and Sounds == "Sounds Mute":
        _menu.entryconfigure(2,label="Un-Mute")
        all_sound = "Mute"
    if _var == 2 and all_sound == "Normal":
        
        _menu.entryconfigure(_var,label="Un-Mute")
        _menu.entryconfigure(0,label="Music Muted")
        _menu.entryconfigure(1,label="Sounds Muted")
        
        mixer.music.set_volume(0.00)
        all_sound = "Mute"
        Music = "Music Mute"
        Sounds = "Sounds Mute"
    elif _var == 2 and all_sound == "Mute":
        _menu.entryconfigure(0,label=_levels2[0])
        _menu.entryconfigure(1,label=_levels2[1])
        _menu.entryconfigure(2,label=_levels2[2])
        mixer.music.set_volume(0.10)
        all_sound = "Normal"
        Music = "Normal"
        Sounds = "Normal"

sounds_option.add_command(label="Music Mute", command = lambda: sound_state_change(0,sounds_option))
sounds_option.add_command(label="Sounds Mute",command = lambda: sound_state_change(1,sounds_option))
sounds_option.add_command(label="Mute", command = lambda: sound_state_change(2,sounds_option))

def urlfb():        #Open Fb page with default web browser
    url = "https://www.facebook.com/Isjtijlfti.patra"
    webbrowser.open(url,new=2)

def urlin():        #Open Github page with default web browser
    url = "https://github.com/Hrishikesh7665"
    webbrowser.open(url,new=2)

def urltw():        #Open HackerRank page with default web browser
    url = "https://www.hackerrank.com/Hrishikesh7665"
    webbrowser.open(url,new=2)

submenu_contact.add_command(label="Hacker Rank", command = lambda: urltw())
submenu_contact.add_command(label="Facebook",command = lambda: urlfb())
submenu_contact.add_command(label="GitHub", command = lambda: urlin())


def gif_show(x1,y1,w): #<------ Change Gif Label Position When Called 
    time.sleep(1.2)
    if(w == 1):
        gif1.place(x=x1,y=y1)
    elif(w == 2):
        time.sleep(1.2)
        gif2.place(x=x1,y=y1)
    elif(w == 3):
        gif3.place(x=x1,y=y1)
    elif(w == 4):
        gif_player1.place(x=x1,y=y1)
    elif(w == 5):
        gif_player2.place(x=x1,y=y1)


#.....................................
org.resizable(width=False, height =False)  #Main Window Un-resizable  
org.mainloop()      #Main Window Main loop