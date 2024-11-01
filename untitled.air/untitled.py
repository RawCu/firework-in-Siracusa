# -*- encoding=utf8 -*-
__author__ = " "

from airtest.core.api import *
from PIL import Image
import os
import logging
from airtest.core.helper import set_logdir

#simulator config: width 2572, height 1224, dpi 280

current_filepath = os.getcwd()
#log config
logger = logging.getLogger("airtest")
handler = logging.FileHandler(current_filepath+"\\log\\log.txt",encoding="utf-8")
logger.addHandler(handler)
logger.setLevel(logging.ERROR)
#log setting
log_path = current_filepath+"\\log\\"
set_logdir(log_path)

auto_setup(__file__)
again=False
sign1=True
sign2=True
not_game_time=0
game_round=0

def screenshots_clear():
    for filename in os.listdir(log_path):
        log_file_path = os.path.join(log_path, filename)
        if os.path.isfile(log_file_path):
            try:
                os.remove(log_file_path)
            except:
                print("\nshots clear complete\n")

def check_lapland():
    #shot for checking lapland
    picfile2 = snapshot(current_filepath+"\\pic\\pic2.jpg",msg="shot for checking lapland")
    img2 = Image.open(current_filepath+"\\pic\\pic2.jpg")
    #scan
    hair_color1 = img2.getpixel((860,905))#should be 255 255 255
    hair_color2 = img2.getpixel((920,855))#should be 238 238 238
    hairpin_color = img2.getpixel((1030,885))#should be 58 58 58
    #calc
    lapland1 = ((255-hair_color1[0])<20 and (255-hair_color1[1])<20 and (255-hair_color1[2])<20)
    lapland2 = ((238-hair_color2[0])<20 and (238-hair_color2[1])<20 and (238-hair_color2[2])<20)
    lapland3 = ((hairpin_color[0]-58)<5 and (hairpin_color[1]-58)<5 and (hairpin_color[2]-58)<5)
    return (lapland1 and lapland2 and lapland3)

def check_board():
    #shot for checking board
    picfile1 = snapshot(current_filepath+"\\pic\\pic1.jpg",msg="shot for checking board.")
    img1 = Image.open(current_filepath+"\\pic\\pic1.jpg")

    color1 = []
    color2 = []
    #upper board
    color1.append(img1.getpixel((250,430)))
    color1.append(img1.getpixel((340,430)))
    color1.append(img1.getpixel((430,430)))
    color1.append(img1.getpixel((520,430)))
    color1.append(img1.getpixel((610,430)))

    color1.append(img1.getpixel((250,520)))
    color1.append(img1.getpixel((340,520)))
    color1.append(img1.getpixel((430,520)))
    color1.append(img1.getpixel((520,520)))
    color1.append(img1.getpixel((610,520)))

    color1.append(img1.getpixel((250,610)))
    color1.append(img1.getpixel((340,610)))
    color1.append(img1.getpixel((430,610)))
    color1.append(img1.getpixel((520,610)))
    color1.append(img1.getpixel((610,610)))

    color1.append(img1.getpixel((250,700)))
    color1.append(img1.getpixel((340,700)))
    color1.append(img1.getpixel((430,700)))
    color1.append(img1.getpixel((520,700)))
    color1.append(img1.getpixel((610,700)))

    color1.append(img1.getpixel((250,790)))
    color1.append(img1.getpixel((340,790)))
    color1.append(img1.getpixel((430,790)))
    color1.append(img1.getpixel((520,790)))
    color1.append(img1.getpixel((610,790)))

    #lower board
    color2.append(img1.getpixel((230,1020)))
    color2.append(img1.getpixel((320,1020)))
    color2.append(img1.getpixel((410,1020)))
    color2.append(img1.getpixel((500,1020)))
    color2.append(img1.getpixel((590,1020)))

    color2.append(img1.getpixel((230,1110)))
    color2.append(img1.getpixel((320,1110)))
    color2.append(img1.getpixel((410,1110)))
    color2.append(img1.getpixel((500,1110)))
    color2.append(img1.getpixel((590,1110)))

    color2.append(img1.getpixel((230,1200)))
    color2.append(img1.getpixel((320,1200)))
    color2.append(img1.getpixel((410,1200)))
    color2.append(img1.getpixel((500,1200)))
    color2.append(img1.getpixel((590,1200)))

    color2.append(img1.getpixel((230,1290)))
    color2.append(img1.getpixel((320,1290)))
    color2.append(img1.getpixel((410,1290)))
    color2.append(img1.getpixel((500,1290)))
    color2.append(img1.getpixel((590,1290)))

    color2.append(img1.getpixel((230,1380)))
    color2.append(img1.getpixel((320,1380)))
    color2.append(img1.getpixel((410,1380)))
    color2.append(img1.getpixel((500,1380)))
    color2.append(img1.getpixel((590,1380)))
    print("scan down")

    #calc
    sum=0
    for i in range(0,25):
        if(color1[i][0]-color2[i][0]>=20):
            sum+=1
            #print((i//5)+1,(i%5)+1)
    print(f"sum is {sum}")
    return sum


#main loop
while(1):
    #clear useless shots
    screenshots_clear()
    sign1=True
    if(again):
        #failed, now restart
        click((1120,620))
        sleep(5)
        click((1120,620))
        sleep(5)
    click((350,2300))
    sleep(9)
    again=True
    game_round=0
    
    while(sign1):
        sum = check_board()
        #touch
        #150/280 start, 240 step
        shi=sum//10
        ge=sum%10
        temp=0
        #print(f"shi:{shi},ge:{ge}")
        #touch qingchu button
        click((990,1878))
        #shiwei
        if(shi!=0):
            click((150+(shi-1)*240,2090))
        #gewei
        if(ge==0):
            click((280,1878))
        elif(ge<6):
            click((150+(ge-1)*240,2090))
        else:
            click((280+(ge-6)*240,2290))
        game_round+=1
        print(f"finish round {game_round}")

        #result check loop
        sign2=True
        wait_time1 = 0
        while(sign2):
            if(check_lapland() and wait_time1<13):
                print(f"waiting for results{wait_time1}s")
                not_game_time=0
                sleep(1)
                wait_time1+=1
            else:#gameplay over
                sign2=False
                not_game_time+=1
                print("go on\n====================")
        #new round check loop
        sleep(4)
        sign3=True
        wait_time2 = 0
        while(sign3):
            if(check_lapland() or wait_time2>5):#result over
                sign3=False
                print("go on new round\n====================")
            else:
                print(f"waiting for new round {wait_time2}s")
                sleep(1)
                wait_time2+=1

        #check if game over
        if(not_game_time>2):
            sign1=False
            print("\n#################\nfailed this round\n#################\n")


    