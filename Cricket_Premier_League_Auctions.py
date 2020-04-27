#Cricket Premier League Auctions
import winsound
import time
import threading
time.sleep(1)
from threading import Timer
print("Cricket Premier League Auctions...\n Let's Start")
time.sleep(1)
print('Welcome to The Most Exciting Auction of CPL')
winsound.PlaySound(r'C:\Users\Sreekanth\Desktop\Pumping Sound.wav', winsound.SND_ASYNC)
import random

def mode():
    try:
        global game
        game=input('Enter Singleplayer or Multiplayer mode=>')
        global n_users
        if game=='Multiplayer' or game=='multiplayer' or game=='M' or game=='m':
            game='Multiplayer'
            n_users=int(input("Enter the Number of players="))
        elif game=='Singleplayer' or game=='singleplayer' or game=='S' or game=='s':
            game='Singleplayer'
            n_users=1
        else:
            print("\nPlease Enter valid input..")
            mode()
        if n_users not in range(1,8):
            raise ValueError 
    except ValueError:
        print("\nThe maximum number of players can be played in this game is 7.So Please...")
        mode()
mode()
time.sleep(1)

print("\n>>Teams of CPL\n\n>Super Cricketers\n>Rocking Rangers\n>Shinning Stars\n>Mysterious Masters\n>Hopping Helicopters\n>Gigantic Giants\n>Victory of Victors")
Teams=['Super Cricketers','Rocking Rangers','Shinning Stars','Mysterious Masters','Hopping Helicopters','Gigantic Giants','Victory of Victors']

comp_players=list(range(n_users+1,8))
users=list(range(1,n_users+1))
string_users=['1','2','3','4','5','6','7']

for x in range(1,n_users+1):
     if x==1: 
        player_1=input('Choose Team of Player_1==>')
        if player_1 not in Teams:
             player_1=input("Please Choose Team from given list of teams with correct spelling==>")
             print("Player_1==>",player_1)
        a=[]
        Teams.remove(player_1)
     elif x==2:
        player_2=input('Choose Team of Player_2==>')
        if player_2 not in Teams:
             player_2=input("Please Choose Team from given list of teams with correct spelling==>")
             print("Player_2==>",player_2)
        b=[]
        Teams.remove(player_2)
     elif x==3:
        player_3=input('Choose Team of Player_3==>')
        if player_3 not in Teams:
             player_3=input("Please Choose Team from given list of teams with correct spelling==>")
             print("Player_3==>",player_3)
        c=[]
        Teams.remove(player_3)
     elif x==4:
        player_4=input('Choose Team of Player_4==>')
        if player_4 not in Teams:
             player_4=input("Please Choose Team from given list of teams with correct spelling==>")
             print("Player_4==>",player_4)
        d=[]
        Teams.remove(player_4)
     elif x==5:
        player_5=input('Choose Team of Player_5==>')
        if player_5 not in Teams:
             player_5=input("Please Choose Team from given list of teams with correct spelling==>")
             print("Player_5==>",player_5)
        e=[]
        Teams.remove(player_5)
     elif x==6:
        player_6=input('Choose Team of Player_6==>')
        if player_6 not in Teams:
             player_6=input("Please Choose Team from given list of teams with correct spelling==>")
             print("Player_6==>",player_6)
        f=[]
        Teams.remove(player_6)
     elif x==7:
        player_7=input('Choose Team of Player_7==>')
        if player_7 not in Teams:
             player_7=input("Please Choose Team from given list of teams with correct spelling==>")
             print("Player_2==>",player_7)
        g=[]
        Teams.remove(player_1)
     else:
      print('There are only Seven Teams in CPL_Auctions')      

for x in range(n_users+1,8):
     if x==2:
      player_2=random.choice(Teams)
      b=[]
      Teams.remove(player_2)
     elif x==3:
      player_3=random.choice(Teams)
      c=[]
      Teams.remove(player_3)
     elif x==4:
      player_4=random.choice(Teams)
      d=[]
      Teams.remove(player_4)
     elif x==5:
      player_5=random.choice(Teams)
      e=[]
      Teams.remove(player_5)
     elif x==6:
      player_6=random.choice(Teams)
      f=[]
      Teams.remove(player_6)
     elif x==7:
      player_7=random.choice(Teams)
      g=[]
      Teams.remove(player_7)
time.sleep(2)
print('\nTeam of player_1=>',player_1,'\nTeam of player_2=>',player_2,'\nTeam of player_3=>',player_3,'\nTeam of player_4=>',player_4,'\nTeam of player_5=>',player_5,'\nTeam of player_6=>',player_6,'\nTeam of player_7=>',player_7)      
print("Let's play...")
def func_team(chosen):
    if chosen==1:
        return player_1
    if chosen==2:
        return player_2
    if chosen==3:
        return player_3
    if chosen==4:
        return player_4
    if chosen==5:
        return player_5
    if chosen==6:
        return player_6
    if chosen==7:
        return player_7  

amount_1=100
amount_2=100
amount_3=100
amount_4=100
amount_5=100
amount_6=100
amount_7=100

time.sleep(3)            
print("\n\nCricket Premier League Auctions begins now..")
print("\n==>Game Description\n    CPL Auctions has four rounds which are Batsman Auctions,Bowler Auctions,Allrounder Auctions,Wicket Keeper Auction. In these four rounds You can buy as many cricketers but limited to amount given to you. You will be placed in 'Place of standings' according to your cricketers in your team at Half Time and Full Time. Team should contain atleast ONE Wicketkeeper in your team. Otherwise you will be disqualified from the auction.Choose Most Rated Cricketer as Captain which helps you in 'Place of Standings'...")
time.sleep(5)
move=input("\nPress Enter to start CPL Auctions...")
time.sleep(2)
inp='jack'
def store_player(inp):
    global a,b,c,d,e,f,g,comp_players,amount_1,amount_2,amount_3,amount_4,amount_5,amount_6,amount_7
    if inp==1:
        a.append(rand_player)
        amount_1-=round(base_price,1)
    if inp==2:
        b.append(rand_player)
        amount_2-=round(base_price,1)
        if inp in comp_players:
            if show=='Batsman Auction':
                if len(b)==4:
                    comp_players.remove(2)
            if show=='Bowler Auction':
                if len(b)==8:
                    comp_players.remove(2)
            if show=='Allrounder Auction':
                if len(b)==12:
                    comp_players.remove(2)
            if show=='Wicket keeper Auction':
                if len(b)==13:
                    comp_players.remove(2)
    if inp==3:
        c.append(rand_player)
        amount_3-=round(base_price,1)
        if inp in comp_players:
            if show=='Batsman Auction':
                if len(c)==4:
                    comp_players.remove(3)
            if show=='Bowler Auction':
                if len(c)==8:
                    comp_players.remove(3)
            if show=='Allrounder Auction':
                if len(c)==12:
                    comp_players.remove(3)
            if show=='Wicket keeper Auction':
                if len(c)==13:
                    comp_players.remove(3)
    if inp==4:
        d.append(rand_player)
        amount_4-=round(base_price,1)
        if inp in comp_players:
            if show=='Batsman Auction':
                if len(d)==4:
                    comp_players.remove(4)
            if show=='Bowler Auction':
                if len(d)==8:
                    comp_players.remove(4)
            if show=='Allrounder Auction':
                if len(d)==12:
                    comp_players.remove(4)
            if show=='Wicket keeper Auction':
                if len(d)==13:
                    comp_players.remove(4)
    if inp==5:
        e.append(rand_player)
        amount_5-=round(base_price,1)
        if inp in comp_players:
            if show=='Batsman Auction':
                if len(e)==4:
                    comp_players.remove(5)
            if show=='Bowler Auction':
                if len(e)==8:
                    comp_players.remove(5)
            if show=='Allrounder Auction':
                if len(e)==12:
                    comp_players.remove(5)
            if show=='Wicket keeper Auction':
                if len(e)==13:
                    comp_players.remove(5)
    if inp==6:
        f.append(rand_player)
        amount_6-=round(base_price,1)
        if inp in comp_players:
            if show=='Batsman Auction':
                if len(f)==4:
                    comp_players.remove(6)
            if show=='Bowler Auction':
                if len(f)==8:
                    comp_players.remove(6)
            if show=='Allrounder Auction':
                if len(f)==12:
                    comp_players.remove(6)
            if show=='Wicket keeper Auction':
                if len(f)==13:
                    comp_players.remove(6)
    if inp==7:
        g.append(rand_player)
        amount_7-=round(base_price,1)
        if inp in comp_players:
            if show=='Batsman Auction':
                if len(g)==4:
                    comp_players.remove(7)
            if show=='Bowler Auction':
                if len(g)==8:
                    comp_players.remove(7)
            if show=='Allrounder Auction':
                if len(g)==12:
                    comp_players.remove(7)
            if show=='Wicket keeper Auction':
                if len(g)==13:
                    comp_players.remove(7)

def rem_amount(num):
    global amount_1,amount_2,amount_3,amount_4,amount_5,amount_6,amount_7
    if num==1:
        amount_1-=rand_maxprice
    if num==2:
        amount_2-=rand_maxprice
    if num==3:
        amount_3-=rand_maxprice
    if num==4:
        amount_4-=rand_maxprice
    if num==5:
        amount_5-=rand_maxprice
    if num==6:
        amount_6-=rand_maxprice
    if num==7:
        amount_7-=rand_maxprice

def play_fix(link,num):
        global rand_player,b,c,d,e,f,g
        if show=='Batsman Auction':
            while len(link)<4:
                rand_player=random.choice(list_bat)
                link.append(rand_player)
                set_max_price(batsman)
                rem_amount(num)
                list_bat.remove(rand_player)
        if show=='Bowler Auction':
            while len(link)<8:
                rand_player=random.choice(list_bowl)
                link.append(rand_player)
                set_max_price(bowler)
                rem_amount(num)
                list_bowl.remove(rand_player)
        if show=='Allrounder Auction':
            while len(link)<12:
                rand_player=random.choice(list_allrounder)
                link.append(rand_player)
                set_max_price(allrounder)
                rem_amount(num)
                list_allrounder.remove(rand_player)
        if show=='Wicket keeper Auction':
            while len(link)<13:
                rand_player=random.choice(list_wicketkeeper)
                link.append(rand_player)
                set_max_price(wicket_keeper)
                rem_amount(num)
                list_wicketkeeper.remove(rand_player)
        rand_player=0

def assign():
    for i in range(1,8): 
        if i in comp_players:
            if i==1:
                play_fix(a,1)
            if i==2:
                play_fix(b,2)
            if i==3:
                play_fix(c,3)
            if i==4:
                play_fix(d,4)
            if i==5:
                play_fix(e,5)
            if i==6:
                play_fix(f,6)
            if i==7:
                play_fix(g,7)
        elif i not in comp_players and want=='auto':
            if i==1:
                play_fix(a,1)
            if i==2:
                play_fix(b,2)
            if i==3:
                play_fix(c,3)
            if i==4:
                play_fix(d,4)
            if i==5:
                play_fix(e,5)
            if i==6:
                play_fix(f,6)
            if i==7:
                play_fix(g,7)

def first_bearer():
    global inp
    for i in range(1):
        if inp in string_users:
            break
        elif rand_maxprice>1.6:
                inp=random.choice(comp_players)
                print("\nThe First Bearer to buy = Player_",random.choice(comp_players))
        if rand_maxprice<1.6:
            global result
            result='unsold'
            print("\n\n",rand_player,"is unsold due to no interest from bearers")
            print("\nPlease Enter 0 to continue the auction...")
            time.sleep(3)

def random_play():
    global inp
    global base_price
    if inp not in comp_players:
        time.sleep(2)
    for i in range(1):
            if base_price>rand_maxprice:
                break
    while inp in comp_players:
            if result=='unsold':
                break
            if inp=='Exit':
                break
            if base_price>rand_maxprice:
                break
            inp=random.choice(comp_players)           
            print("\nPlayer_",inp)
            base_price+=0.1
            print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if base_price>1.0:
                global count
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
                if count==3:
                    last=Timer(2,declare)
                    last.start()
            time.sleep(3)    

def set_max_price(typer):
    global rand_maxprice    
    if typer[rand_player]==5:
        rand_maxprice=random.choice(star_rate)
    elif typer[rand_player]==4.5:
        rand_maxprice=random.choice(marque_rate)
    elif typer[rand_player]==4:
        rand_maxprice=random.choice(average_rate)
    elif typer[rand_player]==3.5:
        rand_maxprice=random.choice(below_rate)
    elif typer[rand_player]==3:
        rand_maxprice=random.choice(bad_rate)

def set_base_price(typer):
    global fixed_base_price
    if typer[rand_player]==5:
        fixed_base_price=random.choice(stars)
    elif typer[rand_player]==4.5:
        fixed_base_price=random.choice(marques)
    elif typer[rand_player]==4:
        fixed_base_price=random.choice(averages)
    elif typer[rand_player]==3.5:
        fixed_base_price=random.choice(below)
    elif typer[rand_player]==3:
        fixed_base_price=random.choice(bad)

def multi():
    global inp,base_price
    while inp not in comp_players:
            if base_price>rand_maxprice:
                break
            inp=random.choice(comp_players)           
            print("\nPlayer_",inp)
            base_price+=0.1
            print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if base_price>1.0:
                global count
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
                if count==3:
                    last=Timer(2,declare)
                    last.start()
            time.sleep(3)
            break               
def countdown():
    global count
    if count==1:
        print('\n3')
    elif count==2:
        print('\n2')
    elif count==3:
        print('\n1')
    count+=1 
    
def declare():
    global result
    for i in range(1):
        if base_price<rand_maxprice and inp not in comp_players:
            break
        if int(inp) in comp_players:
            if base_price<rand_maxprice:
                break
        if base_price>rand_maxprice:
            if inp=='Exit':
                break
            time.sleep(1)
            for i in range(1):
                print('\n')
                print("",rand_player,"is sold for",round(base_price,1),"crores to",func_team(int(inp)))
                store_player(int(inp))
                result='over'
                print("\nPlease Enter 0 to continue the auction...")
                time.sleep(2)
            
star_rate=[10.2,11.0,12.0,13.5]
marque_rate=[6.5,7.0,7.5,8.0,9.5]
average_rate=[4.5,5.0,5.5,6.5]
below_rate=[2.5,3.0,3.5,4.0]
bad_rate=[1.2,1.4,1.7,2.5]
stars=[3.5,4.5,5.0]
marques=[2.5,3.0]
averages=[1.5,2.0]
below=[0.6,0.8,1.0]
bad=[0.4,0.6,0.8]
result='not yet done'
want='unauto'
list_decide=['Yes','No','yes','no','Y','N','y','n','YES','NO']

print("\n\n==>Batsman Auction")
print("The CPL auction starts with batsmans...Hope all the teams ready to buy their batsmans for their respective teams...\n Let's start\n")
batsman={'A B De Villers':5, 'Virat Kohli':5, 'Suresh Raina':5, 'Steve Smith':5, 'Chris Gayle':4.5, 'David Warner':4.5, 'Brendon Mcculum':4.5, 'Kane Williamson':4.5, 'Chris Lynn':4.5, 'Shikar Dhawan':4, 'Rohit Sharma':4, 'Martin Guptill':4, 'Ambati Rayudu':4, 'Shaun Marsh':4, 'Faf du Plessis':3.5, 'Lendl Simmons':3.5, 'Shreyas Iyer':3.5, 'Gautam Gambhir':3.5, 'Aaron Finch':3.5, 'Peter Handscomb':3.5, 'Karun Nair':3.5, 'Prithvi Shaw':3.5, 'Manish Pandey':3.5, 'Tamim Iqbal':3.5, 'Jason Roy':3.5, 'Dwanye Smith':3.5, 'Ajinkya Rahane':3.5, 'Murali Vijay':3, 'David Miller':3, 'David Miller':3, 'Suryakumar Yadav':3}
list_bat=list(batsman.keys())
def bat_auc():
        global show
        show='Batsman Auction'
        time.sleep(2)
        print("==>Cricket Premier League Auctions of Batsmans...")
        time.sleep(2)
        print(" C\n")
        time.sleep(1)
        print("   P\n")
        time.sleep(1)
        print("     L\n")
        time.sleep(1)
        print("       Auctions...")
        global list_bat
        global rand_player
        rand_player=random.choice(list_bat)
        list_bat.remove(rand_player)
        time.sleep(3)
        print("\nHere the Batsman for auction on your tables...\n==>",rand_player)
        time.sleep(1)
        print("\nThe bearers have to type their number and Press Enter...")
        time.sleep(1)
        global base_price
        set_base_price(batsman)
        base_price=fixed_base_price
        print("The Base Price for batsman=>",base_price)
        global inp
        set_max_price(batsman)
        while 1:
            t=Timer(5,random_play)
            t.start()
            if (base_price>1.0 and base_price%0.4==0) or base_price>rand_maxprice:
                global count
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
                if count==3:
                    time.sleep(2)
                    last=Timer(2,declare)
                    last.start()
            def auto_player():
               for i in range(1): 
                   global inp
                   if inp=='Exit':
                       break
                   global base_price
                   if base_price>rand_maxprice:
                       break
                   if base_price<rand_maxprice:
                       if inp not in comp_players:
                           time.sleep(3)
                           inp=random.choice(comp_players)
                           print("\nPlayer_",inp)
                           base_price+=0.1
                           print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if base_price==fixed_base_price:
                first=Timer(2,first_bearer)
                first.start()
            if result=='over':
               break 
            inp=input("Player_")
            global status
            status=0
            if inp=='Exit':
                time.sleep(3)
                break
            if inp=='0':
                break
            if inp not in string_users:
                time.sleep(3)                
                print("Due to invalid input you will not able to buy this player... ")
                status='invalid'
                break
            if int(inp) in comp_players:
                time.sleep(3)
                print("You can't access players which are not under user's control...So you will not able to buy this player... ")
                status='invalid'
                break
            base_price+=0.1
            print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if  base_price<rand_maxprice and base_price>0.9:
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
                if count==3:
                    time.sleep(2)
                    last=Timer(2,declare)
                    last.start()
            if game=='Multiplayer':
                    t=Timer(3,multi)
                    t.start()
                    inp=input("Player_")
                    if inp=='Exit':
                        time.sleep(3)
                        break
                    if inp=='0':
                        break
                    if inp not in string_users:                
                        time.sleep(3)
                        print("Due to invalid input you will not able to buy this player... ")
                        status='invalid'
                        break
                    if int(inp) in comp_players:
                        time.sleep(3)
                        print("You can't access players which are not under user's control...So you will not able to buy this player... ")
                        status='invalid'
                        break
                    base_price+=0.1
                    print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
                    if base_price<rand_maxprice and base_price>0.9:
                        count=1
                        print("\nLet's Countdown Begins...")
                        for i in range(3):    
                            s=Timer(1,countdown)
                            s.start()
                            time.sleep(1)
                            if count==3:
                                time.sleep(2)
                                last=Timer(2,declare)
                                last.start()
            if game=='Singleplayer':
                if base_price>=rand_maxprice:
                    break
            if base_price<=rand_maxprice and result!='unsold':
                    auto_player()

num_bat=len(list_bat)
for i in range(len(list_bat)): 
    if comp_players==[] and n_user!=7:
        bat='over'
        break               
    bat_auc()
    if inp=='Exit' or status=='invalid':
        print("\nPlease Wait...Processing")
        time.sleep(2)
        inp=random.choice(comp_players)
        print('\n')
        print("",rand_player,"is sold for",rand_maxprice,"crores to",func_team(int(inp)))
        base_price=rand_maxprice
        store_player(int(inp))
    time.sleep(4)
    print('\n\n>>Player_1=>'+player_1,'has',round(amount_1,1),'crores left','\n\n>>Player_2=>'+player_2,'has',round(amount_2,1),'crores left','\n\n>>Player_3=>'+player_3,'has',round(amount_3,1),'crores left','\n\n>>Player_4=>'+player_4,'has',round(amount_4,1),'crores left','\n\n>>Player_5=>'+player_5,'has',round(amount_5,1),'crores left','\n\n>>Player_6=>'+player_6,'has',round(amount_6,1),'crores left','\n\n>>Player_7=>'+player_7,'has',round(amount_7,1),'crores left')
    result='not yet done'
    time.sleep(3)
    def dec():
        global decide
        try:
            decide=input("Do you want to continue the CPL Auctions of Batsmans?\nYes=>to continue..and..No=>to exit...\n\n Enter Yes or No...\n")
            if decide not in list_decide:
                raise ValueError
        except ValueError:
            print("\nPlease Enter Yes or No..Invalid input can't be considered")
            dec()
    dec()
    if decide in ['Yes','Y','yes','y','YES']:
            num_bat-=1
            print("\nThere are only",num_bat,"batsmans left in CPL Auctions...\nRemember CPL Auctions of Batsmans will be quit if All other players don't want to continue auctions...")
            time.sleep(2)
            print("\n")
            continue
    def auto_dec():
        global auto
        try:
            auto=input("If you want to autoplay by the computer,Please Enter Yes or No..")
            if auto not in list_decide:
                raise ValueError
        except ValueError:
            print("Please Enter Yes or No..Invalid input can't be considered")
            auto_dec()
    if decide in ['No','no','n','N','NO']:
        auto_dec()
        if auto=='Yes':
            want='auto'
        assign()
        want='unauto'
        bat='over'
        break   

bowler={'Bhuvaneshwar Kumar':5, 'Chris Woakes':5, 'Rashid Khan':5, 'Tim Southee':5, 'Jasprith Bumrah':5, 'Ravichandran Ashwin':5, 'Yuzvendra Chahal':4.5, 'Imran Tahir':4.5, 'Lasith Malinga':4.5, 'Kuldeep Yadav':4.5, 'Shreyas Gopal':4.5, 'Mitchell Starc':4.5, 'Samuel Badree':4.5, 'Pat Cummins':4.5, 'Rangana Herath':4.5, 'Lungi Ngidi':4, 'Washington Sundar':4, 'Sandeep Sharma':4, 'Chris Jordan':4, 'Harbhajan Singh':4, 'Mohit Sharma':4, 'Khaleel Ahmed':4, 'Mustafiqur Rahaman':4, 'Umesh Yadav':4, 'Tyam Mills':4, 'Kagiso Rabada':4, 'Amit Mishra':3.5,  'Mohammed Shami':3.5}
list_bowl=list(bowler.keys())            

comp_players=list(range(n_users+1,8))

print("\n\n==>Bowler Auctions")
print("\nThe CPL auction proceeds with bowlers...Hope all the teams ready to buy their bowlers for their respective teams...\n Let's start")
def bowl_auc():
        global show
        show='Bowler Auction'
        time.sleep(2)
        print("==>Cricket Premier League Auctions of Bowlers...")
        time.sleep(2)
        print(" C\n")
        time.sleep(1)
        print("   P\n")
        time.sleep(1)
        print("     L\n")
        time.sleep(1)
        print("       Auctions...")
        global list_bowl
        global rand_player
        rand_player=random.choice(list_bowl)
        list_bowl.remove(rand_player)
        time.sleep(3)
        print("Here the Bowler for auction on your tables...\n==>",rand_player)
        time.sleep(1)
        print("\nThe bearers have to type their number..and Press Enter")
        time.sleep(1)
        global base_price
        set_base_price(bowler)
        base_price=fixed_base_price
        print("The Base Price for batsman=>",base_price)
        global inp
        set_max_price(bowler)
        while 1:
            t=Timer(5,random_play)
            t.start()
            if (base_price>1.0 and base_price%0.4==0) or base_price>rand_maxprice:
                global count
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
                if count==3:
                    time.sleep(2)
                    last=Timer(2,declare)
                    last.start()
            def auto_player():
               for i in range(1): 
                   global inp
                   if inp=='Exit':
                       break
                   global base_price
                   if base_price>rand_maxprice:
                       break
                   if base_price<rand_maxprice:
                       if inp not in comp_players:
                           time.sleep(3)
                           inp=random.choice(comp_players)
                           print("\nPlayer_",inp)
                           base_price+=0.1
                           print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if base_price==fixed_base_price:
                first=Timer(2,first_bearer)
                first.start()
            inp=input("Player_")
            global status
            status=0
            if inp=='Exit':
                time.sleep(3)
                break
            if inp not in string_users:                
                time.sleep(3)
                print("Due to invalid input you will not able to buy this player... ")
                status='invalid'
                break
            if int(inp) in comp_players:
                time.sleep(3)
                print("You can't access players which are not under user's control...So you will not able to buy this player... ")
                status='invalid'
                break
            if result=='over':
               break 
            if inp=='0':
                break
            base_price+=0.1
            print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if base_price<rand_maxprice and base_price>0.9:
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
            if game=='Multiplayer':
                    t=Timer(3,multi)
                    t.start()
                    inp=input("Player_")
                    if inp=='Exit':
                        time.sleep(3)
                        break
                    if inp=='0':
                        break
                    if inp not in string_users:                
                        time.sleep(3)
                        print("Due to invalid input you will not able to buy this player... ")
                        status='invalid'
                        break
                    if int(inp) in comp_players:
                        time.sleep(3)
                        print("You can't access players which are not under user's control...So you will not able to buy this player... ")
                        status='invalid'
                        break
                    base_price+=0.1
                    print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
                    if base_price<rand_maxprice and base_price>0.9:
                        count=1
                        print("\nLet's Countdown Begins...")
                        for i in range(3):    
                            s=Timer(1,countdown)
                            s.start()
                            time.sleep(1)
                            if count==3:
                                time.sleep(2)
                                last=Timer(2,declare)
                                last.start()
            if game=='Singleplayer':
                if base_price>=rand_maxprice:
                    break
            if base_price<=rand_maxprice and result!='unsold':
                auto_player()
                
num_bowl=len(list_bowl)                
for i in range(len(list_bowl)):
    if comp_players==[] and n_user!=7:
        bat='over'
        break                    
    bowl_auc()
    if inp=='Exit' or status=='invalid':
        print("\nPlease Wait...Processing")
        time.sleep(2)
        inp=random.choice(comp_players)
        print('\n')
        print("",rand_player,"is sold for",rand_maxprice,"crores to",func_team(int(inp)))
        base_price=rand_maxprice
        store_player(int(inp))
    time.sleep(4)
    print('\n\n>>Player_1=>'+player_1,'has',round(amount_1,1),'crores left','\n\n>>Player_2=>'+player_2,'has',round(amount_2,1),'crores left','\n\n>>Player_3=>'+player_3,'has',round(amount_3,1),'crores left','\n\n>>Player_4=>'+player_4,'has',round(amount_4,1),'crores left','\n\n>>Player_5=>'+player_5,'has',round(amount_5,1),'crores left','\n\n>>Player_6=>'+player_6,'has',round(amount_6,1),'crores left','\n\n>>Player_7=>'+player_7,'has',round(amount_7,1),'crores left')
    result='not yet done'
    time.sleep(3)
    def dec():
        global decide
        try:
            decide=input("Do you want to continue the CPL Auctions of Bowlers?\nYes=>to continue..and..No=>to exit...\n\n Enter Yes or No...\n")
            if decide not in list_decide:
                raise ValueError
        except ValueError:
            print("\nPlease Enter Yes or No..Invalid input can't be considered")
            dec()
    dec()
    if decide in ['Y','yes','y','Yes','YES']:
        num_bowl-=1
        print("\nThere are only",num_bowl,"bowlers left in CPL Auctions...\nRemember CPL Auctions of Bowlers will be quit if All other players don't want to continue auctions...")
        print("\n")
        continue
    def auto_dec():
        global auto
        try:
            auto=input("If you want to autoplay by the computer,Please Enter Yes or No..")
            if auto not in list_decide:
                raise ValueError
        except ValueError:
            print("Please Enter Yes or No..Invalid input can't be considered")
            auto_dec()
    if decide in ['no','n','No','N','NO']:
        auto_dec()
        if auto=='Yes':
            want='auto'
        assign()
        want='unauto'
        bat='over'
        break

print("\n\nAs CPL Auctions for Batsmans and Bowlers are over...")
print("\nLet's look into places of each team now...")
print("\nLoading...")

point_1=point_2=point_3=point_4=point_5=point_6=point_7=0
total_points=[]

list_point=['point_1','point_2','point_3','point_4','point_5','point_6','point_7']
def anouncer(num):
   global point_1,point_2,point_3,point_4,point_5,point_6,point_7
   for i in range(1):
        if num==point_1:
           if 'point_1' in list_point:
               list_point.remove('point_1')
               return 1
               break
        if num==point_2:
            if 'point_2' in list_point:
                list_point.remove('point_2')
                return 2
                break
        if num==point_3:
            if 'point_3' in list_point:
                list_point.remove('point_3')
                return 3
                break
        if num==point_4:
            if 'point_4' in list_point:
                list_point.remove('point_4')
                return 4
                break
        if num==point_5:
            if 'point_5' in list_point:
                list_point.remove('point_5')
                return 5
                break
        if num==point_6:
            if 'point_6' in list_point:
                list_point.remove('point_6')
                return 6
                break
        if num==point_7:
            if 'point_7' in list_point:
                list_point.remove('point_7')
                return 7
                break
    
def points_cal(typer):
    global point_1,point_2,point_3,point_4,point_5,point_6,point_7
    for i in range(7):
        if i==0:
            for j in a:
                if j in typer:
                    point_1+=typer[j] 
        if i==1:
            for j in b:
                if j in typer: 
                    point_2+=typer[j]
        if i==2:
            for j in c:
                if j in typer: 
                    point_3+=typer[j]
        if i==3:
            for j in d:
                if j in typer: 
                    point_4+=typer[j]
        if i==4:
            for j in e:
                if j in typer: 
                    point_5+=typer[j]
        if i==5:
            for j in f:
                if j in typer: 
                    point_6+=typer[j]
        if i==6:
            for j in g:
                if j in typer: 
                    point_7+=typer[j]

points_cal(batsman)
points_cal(bowler)
total_points.append(point_1)
total_points.append(point_2)
total_points.append(point_3)
total_points.append(point_4)
total_points.append(point_5)
total_points.append(point_6)
total_points.append(point_7)
asc_points=sorted(total_points,reverse=True)

winsound.PlaySound(r'C:\Users\Sreekanth\Desktop\Twist BGM.wav', winsound.SND_ASYNC)
time.sleep(2)
j=0
for i in asc_points:
    z=anouncer(float(i))
    if j==0:
        print("\nThe First place goes to Player_",z,"==>",func_team(z))
        time.sleep(1)        
    if j==1:
        print("\nThe Second place goes to Player_",z,"==>",func_team(z))
        time.sleep(1)
    if j==2:
        print("\nThe Third place goes to Player_",z,"==>",func_team(z))
        time.sleep(1)
    if j==3:
        print("\nThe Fourth place goes to Player_",z,"==>",func_team(z))
        time.sleep(1)
    if j==4:
        print("\nThe Fifth place goes to Player_",z,"==>",func_team(z))
        time.sleep(1)
    if j==5:
        print("\nThe Sixth place goes to Player_",z,"==>",func_team(z))
        time.sleep(1)
    if j==6:
        print("\nThe Seventh place goes to Player_",z,"==>",func_team(z))
        time.sleep(1)
    j+=1


asc_points=[]
total_points=[]

time.sleep(3)
print("\nCricket Premier League Auctions...\nWishes for Every player...\n\n>Best of luck and Keep it up for First and Second place...\n\n>Very good Try from Your Teams..Put little more efforts with intelligence purchases...for Third and Fourth places...\n\n>Poor Performance...Make Right Choices to purchase...Remember You still have a chance to win First place...For Fifth,Sixth and Seventh places\n")
time.sleep(3)
print("\nWe came to mid-break of our CPL Auctions...Let's have 30 seconds")
time.sleep(15)

print("\n\nWelcome back to Cricket Premier League Auctions..")
print("Hope all teams would have planned very well to buy their players in this mid_break..")
print("Let's Start..")
print("\n")
winsound.PlaySound(r'C:C:\Users\Sreekanth\Desktop\Pumping Sound.wav', winsound.SND_FILENAME)

allrounder={'Dwanye Bravo':5, 'Sunil Narine':5, 'Andrew Russell':5, 'Ben Stokes':5, 'Chris Morris':5, 'Shakib Al Hassan':5, 'Ravindra Jadeja':4.5, 'Hardik Pandya':4.5, 'Andrew Tye':4.5, 'Shane Watson':4.0, 'Moeen Ali':4.0,'Mitchell Santner':4.0, 'Kieron Pollard':4.0, 'Krunal Pandya':4.0, 'J P Duminy':4.0, 'Glenn Maxwell':4.0, 'Axar Patel':4.0, 'James Faulkner':4.0, 'Angelo Mathews':4.0, 'Moises Henriques':4.0, 'Marlon Samuels':3.5, 'Corey Anderson':3.5, 'Yuvaraj Singh':3.5, 'Carlos Brathwaite':3.5, 'Thisara Perera':3.5, 'Alb Morkel':3.5, 'Jason Holder':3.5, 'Daniel Christian':3.5, 'Pawan Negi':3.0, 'Mitchell Marsh':3.0, 'Karn Sharma':3.0, 'David Willey':3.0 ,'Mitchell McClenaghan':3.0, 'Deepak Hooda':3.0}
list_allrounder=list(allrounder.keys())

print("==>Allrounders Auction")
print("\nThe CPL Second Half Auction starts with Allrounders...Hope all the teams ready to buy their allrounders for their respective teams...\n Let's start\n")
def allrounder_auc():
        global show
        show='Allrounder Auction'
        time.sleep(2)
        print("==>Cricket Premier League Auctions of Allrounders...")
        time.sleep(2)
        print(" C\n")
        time.sleep(1)
        print("   P\n")
        time.sleep(1)
        print("     L\n")
        time.sleep(1)
        print("       Auctions...")
        global list_allrounder
        global rand_player
        rand_player=random.choice(list_allrounder)
        list_allrounder.remove(rand_player)
        time.sleep(3)
        print("\nHere the Allrounder for auction on your tables...\n ==>",rand_player)
        time.sleep(1)
        print("\nThe bearers have to type their number..and Press Enter")
        time.sleep(1)
        global base_price
        set_base_price(allrounder)
        base_price=fixed_base_price
        print("The Base Price for batsman=>",base_price)
        global inp
        set_max_price(allrounder)
        while 1:
            t=Timer(5,random_play)
            t.start()
            if (base_price>1.0 and base_price%0.4==0) or base_price>rand_maxprice:
                global count
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
                if count==3:
                    time.sleep(2)
                    last=Timer(2,declare)
                    last.start()
            def auto_player():
               for i in range(1): 
                   global inp
                   if inp=='Exit':
                       break
                   global base_price
                   if base_price>rand_maxprice:
                       break
                   if base_price<rand_maxprice:
                       if inp not in comp_players:
                           time.sleep(3)
                           inp=random.choice(comp_players)
                           print("\nPlayer_",inp)
                           base_price+=0.1
                           print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if base_price==fixed_base_price:
                first=Timer(2,first_bearer)
                first.start()
            if result=='over':
               break 
            inp=input("Player_")
            global status
            status=0
            if inp=='Exit':
                time.sleep(3)
                break
            if inp=='0':
                break
            if inp not in string_users:                
                time.sleep(3)
                print("Due to invalid input you will not able to buy this player... ")
                status='invalid'
                break
            if int(inp) in comp_players:
                time.sleep(3)
                print("You can't access players which are not under user's control...So you will not able to buy this player... ")
                status='invalid'
                break
            base_price+=0.1
            print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if base_price<rand_maxprice and base_price>0.9:
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
                if count==3:
                    time.sleep(2)
                    last=Timer(2,declare)
                    last.start()
            if game=='Multiplayer':
                    t=Timer(3,multi)
                    t.start()
                    inp=input("Player_")
                    if inp=='Exit':
                        time.sleep(3)
                        break
                    if inp=='0':
                        break
                    if inp not in string_users:
                        time.sleep(3)
                        print("Due to invalid input you will not able to buy this player... ")
                        status='invalid'
                        break
                    if int(inp) in comp_players:
                        time.sleep(3)
                        print("You can't access players which are not under user's control...So you will not able to buy this player... ")
                        status='invalid'
                        break
                    base_price+=0.1
                    print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
                    if base_price<rand_maxprice and base_price>0.9:
                        count=1
                        print("\nLet's Countdown Begins...")
                        for i in range(3):    
                            s=Timer(1,countdown)
                            s.start()
                            time.sleep(1)
                            if count==3:
                                time.sleep(2)
                                last=Timer(2,declare)
                                last.start()
            if game=='Singleplayer':
                if base_price>=rand_maxprice:
                    break
            if base_price<=rand_maxprice and result!='unsold':
                    auto_player()
                    
num_allrounder=len(list_allrounder)                    
for i in range(len(list_allrounder)):
    if comp_players==[] and n_users!=7:
        bat='over'
        break                           
    allrounder_auc()
    if inp=='Exit' or status=='invalid':
        print("\nPlease Wait...Processing")
        time.sleep(2)
        inp=random.choice(comp_players)
        print('\n')
        print("",rand_player,"is sold for",rand_maxprice,"crores to",func_team(int(inp)))
        base_price=rand_maxprice
        store_player(int(inp))
    time.sleep(4)
    print('\n\n>>Player_1=>'+player_1,'has',round(amount_1,1),'crores left','\n\n>>Player_2=>'+player_2,'has',round(amount_2,1),'crores left','\n\n>>Player_3=>'+player_3,'has',round(amount_3,1),'crores left','\n\n>>Player_4=>'+player_4,'has',round(amount_4,1),'crores left','\n\n>>Player_5=>'+player_5,'has',round(amount_5,1),'crores left','\n\n>>Player_6=>'+player_6,'has',round(amount_6,1),'crores left','\n\n>>Player_7=>'+player_7,'has',round(amount_7,1),'crores left')
    result='not yet done'
    time.sleep(3)
    def dec():
        global decide
        try:
            decide=input("Do you want to continue the CPL Auctions of Allrounders?\nYes=>to continue..and..No=>to exit...\n\n Enter Yes or No...\n")
            if decide not in list_decide:
                raise ValueError
        except ValueError:
            print("\nPlease Enter Yes or No..Invalid input can't be considered")
            dec()
    dec()
    if decide in ['Yes','Y','yes','y','YES']:
        num_bowl-=1
        print("\nThere are only",num_allrounder,"allrounders left in CPL Auctions...\nRemember CPL Auctions of Bowlers will be quit if All other players don't want to continue auctions...")
        print("\n")
        continue
    def auto_dec():
        global auto
        try:
            auto=input("If you want to autoplay by the computer,Please Enter Yes or No..")
            if auto not in list_decide:
                raise ValueError
        except ValueError:
            print("Please Enter Yes or No..Invalid input can't be considered")
            auto_dec()
    if decide in ['No','no','n','No','NO']:
        auto_dec()
        if auto=='Yes':
            want='auto'
        assign()
        want='unauto'
        bat='over'
        break
    
wicket_keeper={'M S Dhoni':5, 'K L Rahul':4.5, 'Jos Buttler':4.5, 'Rishab Pant':4.5, 'Dinesh Karthik':4, 'Robin Uttappa':4, 'Sam Billings':4, 'Sanju Samson':4, 'Quinton De Kock':4, 'Wriddhiman Saha':3.5}
list_wicketkeeper=list(wicket_keeper.keys())

print("\n\n==>WicketKeepers Auction")
print("\nThe CPL Auction ends with Wicket Keeper...Hope all the teams ready to buy atleast ONE Wicket Keeper for their respective teams...Otherwise Team gets disqualified from CPL Auctions\n Let's start\n")
def wicket_keeper_auc():
        global show
        show='Wicket keeper Auction'
        time.sleep(2)
        print("==>Cricket Premier League Auctions of Wicket Keepers...")
        time.sleep(2)
        print(" C\n")
        time.sleep(1)
        print("   P\n")
        time.sleep(1)
        print("     L\n")
        time.sleep(1)
        print("       Auctions...")
        global list_wicketkeeper
        global rand_player
        rand_player=random.choice(list_wicketkeeper)
        list_wicketkeeper.remove(rand_player)
        time.sleep(3)
        print("\nHere the Wicket Keeper for auction on your tables...\n ==>",rand_player)
        time.sleep(1)
        print("\nThe bearers have to type their number..and Press Enter")
        time.sleep(1)
        global base_price
        set_base_price(wicket_keeper)
        base_price=fixed_base_price
        print("The Base Price for batsman=>",base_price)
        global inp
        set_max_price(wicket_keeper)
        while 1:
            t=Timer(5,random_play)
            t.start()
            if (base_price>1.0 and base_price%0.4==0) or base_price>rand_maxprice:
                global count
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
                if count==3:
                    time.sleep(2)
                    last=Timer(2,declare)
                    last.start()
            def auto_player():
               for i in range(1): 
                   global inp
                   if inp=='Exit':
                       break
                   global base_price
                   if base_price>rand_maxprice:
                       break
                   if base_price<rand_maxprice:
                       if inp not in comp_players:
                           time.sleep(3)
                           inp=random.choice(comp_players)
                           print("\nPlayer_",inp)
                           base_price+=0.1
                           print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if base_price==fixed_base_price:
                first=Timer(2,first_bearer)
                first.start()
            if result=='over':
               break 
            inp=input("Player_")
            global status
            status=0
            if inp=='Exit':
                time.sleep(3)
                break
            if inp=='0':
                break
            if inp not in string_users:                
                time.sleep(3)
                print("Due to invalid input you will not able to buy this player... ")
                status='invalid'
                break
            if int(inp) in comp_players:
                time.sleep(3)
                print("You can't access players which are not under user's control...So you will not able to buy this player... ")
                status='invalid'
                break
            base_price+=0.1
            print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
            if base_price<rand_maxprice and base_price>0.9:
                count=1
                print("\nLet's Countdown Begins...")
                for i in range(3):    
                    s=Timer(1,countdown)
                    s.start()
                    time.sleep(1)
                if count==3:
                    time.sleep(2)
                    last=Timer(2,declare)
                    last.start()
            if game=='Multiplayer':
                    t=Timer(3,multi)
                    t.start()
                    inp=input("Player_")
                    if inp=='Exit':
                        time.sleep(3)
                        break
                    if inp=='0':
                        break
                    if inp not in string_users:
                        time.sleep(3)
                        print("Due to invalid input you will not able to buy this player... ")
                        status='invalid'
                        break
                    if int(inp) in comp_players:
                        time.sleep(3)
                        print("You can't access players which are not under user's control...So you will not able to buy this player... ")
                        status='invalid'
                        break
                    base_price+=0.1
                    print("The new bearer to buy",rand_player,"now...",func_team(int(inp)),"==>",round(base_price,1),"crores")
                    if base_price<rand_maxprice and base_price>0.9:
                        count=1
                        print("\nLet's Countdown Begins...")
                        for i in range(3):    
                            s=Timer(1,countdown)
                            s.start()
                            time.sleep(1)
                            if count==3:
                                time.sleep(2)
                                last=Timer(2,declare)
                                last.start()
            if game=='Singleplayer':
                if base_price>=rand_maxprice:
                    break
            if base_price<=rand_maxprice and result!='unsold':
                    auto_player()

num_wicketkeeper=len(list_wicketkeeper) 
for i in range(len(list_wicketkeeper)):
    if comp_players==[] and n_user!=7:
        bat='over'
        break                              
    wicket_keeper_auc()
    if inp=='Exit' or status=='invalid':
        print("\nPlease Wait...Processing")
        time.sleep(2)
        inp=random.choice(comp_players)
        print('\n')
        print("",rand_player,"is sold for",rand_maxprice,"crores to",func_team(int(inp)))
        base_price=rand_maxprice
        store_player(int(inp))
    time.sleep(4)
    print('\n\n>>Player_1=>'+player_1,'has',round(amount_1,1),'crores left','\n\n>>Player_2=>'+player_2,'has',round(amount_2,1),'crores left','\n\n>>Player_3=>'+player_3,'has',round(amount_3,1),'crores left','\n\n>>Player_4=>'+player_4,'has',round(amount_4,1),'crores left','\n\n>>Player_5=>'+player_5,'has',round(amount_5,1),'crores left','\n\n>>Player_6=>'+player_6,'has',round(amount_6,1),'crores left','\n\n>>Player_7=>'+player_7,'has',round(amount_7,1),'crores left')
    result='not yet done'
    time.sleep(3)
    def dec():
        global decide
        try:
            decide=input("Do you want to continue the CPL Auctions of Wicket keepers?\nYes=>to continue..and..No=>to exit...\n\n Enter Yes or No...\n")
            if decide not in list_decide:
                raise ValueError
        except ValueError:
            print("\nPlease Enter Yes or No..Invalid input can't be considered")
            dec()
    dec()
    if decide in ['Yes','Y','yes','y','YES']:
        num_bowl-=1
        print("\nThere are only",num_wicketkeeper,"wicketkeepers left in CPL Auctions...\nRemember CPL Auctions of Bowlers will be quit if All other players don't want to continue auctions...")
        print("\n")
        continue
    def auto_dec():
        global auto
        try:
            auto=input("If you want to autoplay by the computer,Please Enter Yes or No..")
            if auto not in list_decide:
                raise ValueError
        except ValueError:
            print("Please Enter Yes or No..Invalid input can't be considered")
            auto_dec()
    if decide in ['Yes','no','n','No','NO']:
        auto_dec()
        if auto=='Yes':
            want='auto'
        assign()
        want='unauto'
        bat='over'
        break

print("\n\nCPL Auctions are ended with immense competitions between players...")
time.sleep(3)

comp_players=list(range(n_users+1,8))
def min_players(item):
    if len(item)>13:
        print("Please Select Your 'Best 13 Players' of Your Team to exhibit Place of Standings...")
        while len(item)>13:
            rem_player=("Enter one of the player of Your Team to remove from your squad==>")
            if rem_player not in item:
                print("",rem_player,"is not found to be in Your team...or You would have spelled him wrong")
                rem_player=input("So Please Enter Player of Your team correctly==>")
            item.remove(rem_player)

def print_cricketers(i,item):
        print("\nPlayer_",i,"==>",func_team(int(i)))
        time.sleep(2)
        if i not in comp_players:
            for j in item:
                print('>',j)
                time.sleep(1)
            time.sleep(3)
            min_players(item)
        print("'Best 13' from Player_",i,"\n==>",func_team(int(i))) 
        for j in item:
            print('>',j)
            time.sleep(0.5)
        print("\n")
        time.sleep(2)

def captain():
    global a,b,c,d,e,f,cap_1,cap_2,cap_3,cap_4,cap_5,cap_6,cap_7
    print("\n\nChoosing Good Rated Player as Captain can benefit you in Place of Standings...")
    for i in range(1,8):
        if i==1:
            cap_1=input("\nPlease Your Team Captain for Player_1==>")
            if cap_1 not in a:
                    cap_1=input("Please Enter Your Captain Correctly otherwise you will be disqualified==>")
            a.append(cap_1)
            print("\n>",cap_1,"is chosen as their Captain for",player_1)
        if i==2:
            if i in comp_players:
                cap_2=random.choice(b)
            else:
                cap_2=input("\nPlease Your Team Captain for Player_2==>")
                if cap_2 not in b:
                    cap_2=input("Please Enter Your Captain Correctly otherwise you will be disqualified==>")
            b.append(cap_2)
            print("\n>",cap_2,"is chosen as their Captain for",player_2)
        if i==3:
            if i in comp_players:
                cap_3=random.choice(c)
            else:
                cap_3=input("\nPlease Your Team Captain for Player_2==>")
                if cap_3 not in c:
                    cap_3=input("Please Enter Your Captain Correctly otherwise you will be disqualified==>")
            c.append(cap_3)
            print("\n>",cap_3,"is chosen as their Captain for",player_3)
        if i==4:
            if i in comp_players:
                cap_4=random.choice(d)
            else:
                cap_4=input("\nPlease Your Team Captain for Player_4==>")
                if cap_4 not in d:
                    cap_4=input("Please Enter Your Captain Correctly otherwise you will be disqualified==>")
            d.append(cap_4)
            print("\n>",cap_4,"is chosen as their Captain for",player_4)
        if i==5:
            if i in comp_players:
                cap_5=random.choice(e)
            else:
                cap_5=input("\nPlease Your Team Captain for Player_5==>")
                if cap_5 not in e:
                    cap_5=input("Please Enter Your Captain Correctly otherwise you will be disqualified==>")
            e.append(cap_5)
            print("\n>",cap_5,"is chosen as their Captain for",player_5)
        if i==6:
            if i in comp_players:
                cap_6=random.choice(f)
            else:
                cap_6=input("\nPlease Your Team Captain for Player_6==>")
                if cap_6 not in f:
                    cap_2=input("Please Enter Your Captain Correctly otherwise you will be disqualified==>")
            f.append(cap_6)
            print("\n>",cap_6,"is chosen as their Captain for",player_6)
        if i==7:
            if i in comp_players:
                cap_7=random.choice(g)
            else:
                cap_7=input("\nPlease Your Team Captain for Player_7==>")
                if cap_7 not in g:
                    cap_7=input("Please Enter Your Captain Correctly otherwise you will be disqualified==>")
            g.append(cap_7)
            print("\n>",cap_7,"is chosen as their Captain for",player_7)

print_cricketers(1,a)
print_cricketers(2,b)
print_cricketers(3,c)
print_cricketers(4,d)
print_cricketers(5,e)
print_cricketers(6,f)
print_cricketers(7,g)
captain()

total_points=[]
asc_points=[]

list_point=['point_1','point_2','point_3','point_4','point_5','point_6','point_7']
points_cal(allrounder)
points_cal(wicket_keeper)
total_points.append(point_1)
total_points.append(point_2)
total_points.append(point_3)
total_points.append(point_4)
total_points.append(point_5)
total_points.append(point_6)
total_points.append(point_7)

asc_points=sorted(total_points)
time.sleep(4)        
print("\n\nLet's look into Most Exciting and Awaiting Presentation now...")
time.sleep(2)
print("\nPlace of Standings are as follows...")

j=0  
for i in asc_points:
    z=anouncer(float(i))
    if j==5:
        z=anouncer(float(asc_points[-1]))
        print("\n\nHere The Most Awaiting and Exciting Winnner as well as Champion of CPL Auctions...")
        print("\nLet's Countdown begins...")
        time.sleep(1)
        print('\nC')
        time.sleep(1)
        print('\n   P')
        time.sleep(1)
        print('\n      L')
        time.sleep(2)
        print("\nLet's Go...")
        time.sleep(2)
        print("\n\nChampion of Cricket Premier Auctions goes to Player_",z,"==>",func_team(z))
        print("Congratulatins...Excellent and Fabulous Performance from your side")   
        winsound.PlaySound(r'C:\Users\Sreekanth\Desktop\Project.wav', winsound.SND_FILENAME)
    if j==6:
        z=anouncer(float(asc_points[-2]))
        time.sleep(2)
        print("\n\nRunner Up of Cricket Premier League goes to Player_",z,"==>",func_team(z))
        print("Missed Championship in a small edge...Awesome Performance from your side")
    if j==4:
        time.sleep(3)
        print("\n\nThe Third place goes to Player_",z,"==>",func_team(z))
        print("Very Good Performance...Better Luck next time...")
    if j==3:
        time.sleep(2)
        print("\n\nThe Fourth place goes to Player_",z,"==>",func_team(z))
        print("Good Performance...Right Choices can make perfect team...")
    if j==2:
        time.sleep(2)
        print("\n\nThe Fifth place goes to Player_",z,"==>",func_team(z))
        print("Average Performance...Awesome Efforts from your side...")
    if j==1:
        time.sleep(2)
        print("\n\nThe Sixth place goes to Player_",z,"==>",func_team(z))
        print("Well Tried...Do the best next time...")
    if j==0:
        time.sleep(3)
        print("\n\nThe Seventh place goes to Player_",z,"==>",func_team(z))
        print("Poor Performance...Lost from Underrated purchases")
    j+=1
    
time.sleep(2)
print("\nThanks for participating in Cricket Premier League Auctions..Hope you like it...")
winsound.PlaySound(r'C:\Users\Sreekanth\Desktop\Project.wav', winsound.SND_FILENAME)