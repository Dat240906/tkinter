from tkinter import *
import random,tkinter
from random import randint
from time import sleep
from tkinter import font

from PIL import Image,ImageTk
import tkinter as tk
from tkinter import messagebox
from itertools import product
root = Tk()
root.geometry('600x350+330+200')

# TẠO HÌNH TRÒN
def tao_hinh_tron():
    global c
    c= Canvas(root,width=400, height=400)
    c.place(x=170,y=20)
    c.create_oval(60,60,200,200)
tao_hinh_tron()
    # TEXT IN RA SỐ TIỀN CƯỢC
def text_tien_cuoc():
    global coin_bet_tai
    global coin_bet_xiu
    coin_bet_tai = Label(root,text=0,bg='#F0F0F0',font=('Convection',9),fg='#000000')
    coin_bet_tai.place(x=100,y=170)

    coin_bet_xiu = Label(root,text=0,bg='#F0F0F0',font=('Convection',9),fg='#000000')
    coin_bet_xiu.place(x=440,y=170)
text_tien_cuoc()
#TEXT thời gian ĐẾM NGƯỢC
def in_dem_nguoc():
    global text_dem_nguoc
    text_dem_nguoc = Label(c,text=30,fg='#000000',font=('@Gungsuh',27))
    text_dem_nguoc.place(x=110,y=90)
in_dem_nguoc()
# TEXT_DICE
def dice(root,text,x,y,color_text):
    global m
    m = Label(root,text=text,fg=color_text,font=('@Gungsuh',30))
    m.place(x=x,y=y)
# RANDOM VỊ TRÍ NGẪU NHIÊN CỦA XÚC SẮC
list_index = [100,150,96]
rd1 = random.choice(list_index)
list_index.remove(rd1)
rd2= random.choice(list_index)
list_index.remove(rd2)
rd3 = list_index[0]
if rd1 == 100:
    y1 =70
    if rd2 == 150:
        y2 = 130
        #rd3
        y3 = 96
    else:
        y2 = 140
        #rd3
        y3= 150
elif rd1 == 150:
    y1 = 130
    if rd2 == 100:
        y2 = 70
        #rd3
        y3=96
    else:
        y2= 140
        y3 = 100
elif rd1==96:

    y1=140
    if rd2 ==100:
        y2= 70
        y3 = 150
    else:
        y2 = 130
        y3 = 100
def tra_ve_in_ra_3_xx():
    global rd_x_dice_1 
    global rd_x_dice_3
    global rd_x_dice_2
    global ymain1
    global ymain2
    global ymain3
    list_rd=[rd1,rd2,rd3]
    rd_x_dice_1 = random.choice(list_rd)
    list_rd.remove(rd_x_dice_1)
    rd_x_dice_2 = random.choice(list_rd)
    list_rd.remove(rd_x_dice_2)
    rd_x_dice_3 = random.choice(list_rd)
    if rd_x_dice_1 ==  96:
        ymain1 = 140
        if rd_x_dice_2 == 150:
            ymain2 = 130
            #rd_x_dice_3=100
            ymain3 = 70
        else:#rd_x_dice_2= 100
            ymain2 = 70
            #rd_x_dice_3 = 150
            ymain3 = 130
    elif rd_x_dice_1 ==100:
        ymain1 = 70
        if rd_x_dice_2 ==96:
            ymain2 = 140
            #rd_x_dice_3 = 150
            ymain3 = 130
        else:#rd_x_dice_2 = 150
            ymain2 = 130
            #rd_x_dice_3 = 96
            ymain3 = 140
    else:#rd_x_dice_1 = 150
        ymain1= 130
        if rd_x_dice_2== 96:
            ymain2 = 140
            #rd_x_dice_3 = 100
            ymain3 = 70
        else:#rd_x_dice_2 = 100
            ymain2 = 70
            #rd_x_dice_3 = 96
            ymain3 = 140
tra_ve_in_ra_3_xx()
def show_dices():

    global d_1
    global d_2
    global d_3
    global d_4
    global d_5
    global d_6

    # global dice1
    # global dice2
    # global dice3
    # global dice4
    # global dice5
    # global dice6
    global rd_list_dice_1
    global rd_list_dice_2
    global rd_list_dice_3


    def d_1(x,y):
        global dice1
            # dice1 = dice(c,'⚀',x,y,'#FF0000')
        dice1 = Label(c,text='⚀',fg='#FF0000',font=('@Gungsuh',30))
        dice1.place(x=x,y=y)
    def d_2(x,y):
        global dice2
            # dice2 = dice(c,'⚁',x,y,'#000000')
        dice2 = Label(c,text='⚁',fg='#000000',font=('@Gungsuh',30))
        dice2.place(x=x,y=y)        
    def d_3(x,y):
        global dice3
        dice3 = Label(c,text='⚂',fg='#000000',font=('@Gungsuh',30))
        dice3.place(x=x,y=y)
            # dice3 = dice(c,'⚂',x,y,'#000000')
    def d_4(x,y):
        global dice4
        dice4 = Label(c,text='⚃',fg='#FF0000',font=('@Gungsuh',30))
        dice4.place(x=x,y=y)
            # dice4 = dice(c,'⚃',x,y,'#FF0000')
    def d_5(x,y):
        global dice5
        dice5 = Label(c,text='⚄',fg='#000000',font=('@Gungsuh',30))
        dice5.place(x=x,y=y)
            # dice5 = dice(c,'⚄',x,y,'#000000')
    def d_6(x,y):
        global dice6
        dice6 = Label(c,text='⚅',fg='#000000',font=('@Gungsuh',30))
        dice6.place(x=x,y=y)
            # dice6 = dice(c,'⚅',x,y,'#000000')
    list_def_dices = [d_1,d_2,d_3,d_4,d_5,d_6]
    rd_list_dice_1 = random.choice(list_def_dices)
    list_def_dices.remove(rd_list_dice_1)
    rd_list_dice_2 = random.choice(list_def_dices)
    list_def_dices.remove(rd_list_dice_2)
    rd_list_dice_3 = random.choice(list_def_dices)
    return rd_list_dice_1(rd_x_dice_1,ymain1),rd_list_dice_2(rd_x_dice_2,ymain2), rd_list_dice_3(rd_x_dice_3,ymain3)

def xet_value_dice():
    global valur_dice1
    global valur_dice2
    global valur_dice3
    valur_dice1=0
    valur_dice2=0
    valur_dice3=0
    global coin_da_cuoc_tai
    global coin_da_cuoc_xiu
    global Tong_value
            # DICE VALUE 1
    if rd_list_dice_1 == d_1:
        valur_dice1 = 1
    elif rd_list_dice_1 == d_2:
        valur_dice1 = 2
    elif rd_list_dice_1 == d_3:
        valur_dice1 = 3
    elif rd_list_dice_1 == d_4:
        valur_dice1 = 4
    elif rd_list_dice_1 == d_5:
        valur_dice1 = 5
    else: 
        valur_dice1 = 6
            # DICE VALUE 3
    if rd_list_dice_2 == d_1:
        valur_dice2 = 1
    elif rd_list_dice_2 == d_2:
        valur_dice2 = 2
    elif rd_list_dice_2 == d_3:
        valur_dice2 = 3
    elif rd_list_dice_2 == d_4:
        valur_dice2 = 4
    elif rd_list_dice_2 == d_5:
        valur_dice2 = 5
    else: 
        valur_dice2 = 6
            #   DICE VALUE 3
    if rd_list_dice_3 == d_1:
        valur_dice3 = 1
    elif rd_list_dice_3 == d_2:
        valur_dice3 = 2
    elif rd_list_dice_3 == d_3:
        valur_dice3 = 3
    elif rd_list_dice_3 == d_4:
        valur_dice3 = 4
    elif rd_list_dice_3 == d_5:
        valur_dice3 = 5
    else: 
        valur_dice3 = 6
    Tong_value = valur_dice1 + valur_dice2 + valur_dice3
#TẠO LIST RANDOM VÀ XET TRƯỜNG HỢP
def cong_tru_coin():
    global coin_cong
    if Tong_value <= 10:# XỈU
        if coin_bet_tai['text']!= 0: 
            if coin_bet_xiu['text'] == 0:# CƯỢC TÀI
                    #ra xỉu mà cược tài => xử thua
                pass
            else:  #coin_bet_xiu['text'] != 0 # CƯỢC CẢ 2
                    #trừ tiền bên tài cộng tiền bên xỉu x1.98
                coin_cong= int(coin_bet_xiu['text']*1.98)
                coin_tong = coin_money['text']+coin_cong
                coin_money['text']= coin_tong
        else  :#coin_bet_tai['text'] == 0
            if coin_bet_xiu['text']==0: # K CƯỢC GÌ
                pass# KHÔNG LÀM GÌ
            else:# coin_bet_xiu['text']!=0 #CƯỢC XỈU
                    # CỘNG TIỀN CHO XỈU
                coin_cong= int(coin_bet_xiu['text']*1.98)
                coin_tong = coin_money['text']+coin_cong
                coin_money['text']= coin_tong
    
    else:# RA TÀI
        if coin_bet_tai['text'] != 0 :
            if coin_bet_xiu['text'] == 0: #CƯỢC TÀI
                        # CỘNG TIỀN CHO TÀI
                coin_cong= int(coin_bet_tai['text']*1.98)
                coin_tong = coin_money['text']+coin_cong
                coin_money['text']= coin_tong
            else :#coin_bet_tai['text'] !=0 #CƯỢC CẢ 2
                        #cộng tiền cho cả hai
                coin_cong= int(coin_bet_tai['text']*1.98)
                coin_tong = coin_money['text']+coin_cong
                coin_money['text']= coin_tong
        else:# coin_bet_tai['text'] ==0 
            if coin_bet_xiu['text']!= 0 :# CƯỢC XỈU
                        # TRỪ TIỀN
                pass
            else :#coin_bet_xiu['text'] == 0 # K CƯỢC
                        #  k làm gì
                pass
    
def dem_nguoc():
    global dem
    dem=int(text_dem_nguoc['text'])-1
    if dem >=0:  
        text_dem_nguoc['text']=dem
        root.after(1000, dem_nguoc)
    if dem <= 5:
        text_dem_nguoc['fg'] = '#CC0000'
        update_coin()
        if dem ==1:
            ham_nan()
        if dem==0:
            text_dem_nguoc.destroy()
            show_dices()
dem_nguoc()
#TEXT coin fake
def text_coin_fake():
    global text_coin_fake_tai
    global text_coin_fake_xiu
    text_coin_fake_tai = Label(root,text=0,bg='#CCFF00',font=('@Gungsuh',12))
    text_coin_fake_tai.place(anchor='w',x=80,y=150)
    text_coin_fake_xiu = Label(root,text=0,bg='#CCFF00',font=('@Gungsuh',12))
    text_coin_fake_xiu.place(anchor='e',x=490,y=150)
text_coin_fake()
def ham_nan():
    global dem_nguoc
    global mesbox
    mesbox = messagebox.showinfo('!!!','______________NẶN_____')
    if mesbox == 'ok':
        # XÓA DICES ĐỂ CHẠY PHIÊN KHÁC
                    #XÉT RANDOM_DICE1
        if rd_list_dice_1 == d_1:
            dice1.destroy()
        if rd_list_dice_1 == d_2:
            dice2.destroy()
        if rd_list_dice_1 == d_3:
            dice3.destroy()
        if rd_list_dice_1 == d_4:
            dice4.destroy()
        if rd_list_dice_1 == d_5:
            dice5.destroy()
        if rd_list_dice_1 == d_6:
            dice6.destroy()
                    #XÉT RANDOM_DICE2
        if rd_list_dice_2 == d_1:
            dice1.destroy()
        if rd_list_dice_2 == d_2:
            dice2.destroy()
        if rd_list_dice_2 == d_3:
            dice3.destroy()
        if rd_list_dice_2 == d_4:
            dice4.destroy()
        if rd_list_dice_2 == d_5:
            dice5.destroy()
        if rd_list_dice_2 == d_6:
            dice6.destroy()
                    #XÉT RANDOM_DICE3
        if rd_list_dice_3 == d_1:
            dice1.destroy()
        if rd_list_dice_3 == d_2:
            dice2.destroy()
        if rd_list_dice_3 == d_3:
            dice3.destroy()
        if rd_list_dice_3 == d_4:
            dice4.destroy()
        if rd_list_dice_3 == d_5:
            dice5.destroy()
        if rd_list_dice_3 == d_6:
            dice6.destroy()
        text_dem_nguoc.destroy
        # RESET THUỘC TÍNH KHI START VÁN MỚI

        text_coin_fake_tai['text'] = 0
        text_coin_fake_xiu['text'] = 0

        xet_value_dice()
        in_dem_nguoc()
        dem_nguoc()
        update_coin()
        Tiencuoc()
        cong_tru_coin()        
        # main_Anim() 
        coin_bet_xiu['text']= 0
        coin_bet_tai['text']= 0      
# HÀM CHẠY 2 FUNs TRONG 1 COMMAND IN BUTTON
def hai_ham(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func
# TEXT IN RA SỐ TIỀN CƯỢC
def coin_bet():
    global coin_bet_tai
    global coin_bet_xiu
    coin_bet_tai = Label(root,text=0,bg='#F0F0F0',font=('Convection',9),fg='#000000')
    coin_bet_tai.place(x=100,y=170)
        
    coin_bet_xiu = Label(root,text=0,bg='#F0F0F0',font=('Convection',9),fg='#000000')
    coin_bet_xiu.place(x=440,y=170)
coin_bet()
def Tiencuoc():
    global update_coin_cuoc_tai
    global update_coin_cuoc_xiu
    global coin_da_cuoc_tai
    global coin_da_cuoc_xiu
    global coin_bet_xiu
    global coin_bet_tai
    #DEF IN RA TIỀN KHI CƯỢC
    def update_coin_cuoc_tai():
        global coin_da_cuoc_tai
        if dem >= 5:
            if coin_money['text']>=0:
                if int(inputValue_tai) <= coin_money['text']:
                    coin_da_cuoc_tai = coin_bet_tai['text'] + int(inputValue_tai)
                    coin_bet_tai['text'] = coin_da_cuoc_tai
                else:pass
            else:pass
        else:
            messagebox.showinfo('!!!','HẾT THỜI GIAN CƯỢC!')

    def update_coin_cuoc_xiu():
        global coin_da_cuoc_xiu
        if dem >= 5:
            if coin_money['text']>=0:
                if int(inputValue_xiu) <= coin_money['text']:
                    coin_da_cuoc_xiu = coin_bet_xiu['text'] + int(inputValue_xiu)
                    coin_bet_xiu['text']= coin_da_cuoc_xiu
                else:pass
            else:pass
        else:
            messagebox.showinfo('!!!','HẾT THỜI GIAN CƯỢC!')
Tiencuoc()
# TEXT COIN MAIN
def hienthi_coin_icon():
    global coin_icon
    global coin_money
    coin_icon = Label(root,text='$',bg='#888888',font=('Convection',13),fg='#FFFF33').place(x=240)
    coin_money = Label(c,text=100000,bg='#888888',font=('Convection',13),fg='#FFFF00')
    coin_money.place(y=0,x=100)
hienthi_coin_icon()
# INPUT COIN 
def nhap_tien_cuoc_tai():
    global textBox_tai
    var1 = tkinter.StringVar()
    textBox_tai = tkinter.Entry(root, textvariable=var1)
    textBox_tai.place(x=60,y=200)
    var1.set('')
nhap_tien_cuoc_tai()
def nhap_tien_cuoc_xiu():
    global textBox_xiu
    var2 = tkinter.StringVar()
    textBox_xiu = tkinter.Entry(root, textvariable=var2)
    textBox_xiu.place(x=380,y=200)
    var2.set('')  
nhap_tien_cuoc_xiu()
# TẠO HỘP CHUYỂN ĐỘNG KHI CÔNG COIN
# def main_Anim():
#     global bien_tam
#     global x_,y_
#     bien_tam = 0
#     x_ = 10
#     y_ = 20
#     def anim():
#         global bien_tam
#         global x_
#         global y_
#         if bien_tam <= 10:
#             y_+=0.3
#             box_coin = Label(root,text='+'+str(coin_bet_tai['text']),fg='#FFFF00',font=('@Gungsuh',7),bg='#999999',borderwidth=2, relief="solid")
#             box_coin.place(x=x_,y=y_)
#             box_coin.destroy
#             bien_tam+=1
            
#             root.after(7,anim)
#         elif bien_tam ==0:
#             pass
    


# LẤY VALUE CỦA COIN NHẬP VÀO
def retrieve_input_tai():
    global textBox_tai
    global inputValue_tai
    inputValue_tai=textBox_tai.get()
    return inputValue_tai
def retrieve_input_xiu():
    global textBox_xiu
    global inputValue_xiu
    inputValue_xiu=textBox_xiu.get()
    return inputValue_xiu 
retrieve_input_xiu()  
# DEF TRỪ TIỀN KHI CƯỢC
def tru_coin_khi_cuoc_tai():
    if coin_money['text']>=0:
        if int(inputValue_tai) <= coin_money['text']:
            da_tru = coin_money['text']-int(inputValue_tai)
            coin_money['text'] = da_tru
        else:
            messagebox.showwarning('$ THIẾU!')
    else:
        messagebox.showwarning('$ THIẾU!') 
def tru_coin_khi_cuoc_xiu():
    if coin_money['text']>=0:
        if int(inputValue_xiu) <= coin_money['text']:
            da_tru = coin_money['text']-int(inputValue_xiu)
            coin_money['text'] = da_tru
        else:
            messagebox.showwarning('$ THIẾU!')
    else:
        messagebox.showwarning('$ THIẾU!')      
# NHẬP CODE   
code  = 'may'
def reset_code():
    var = StringVar()
    var.set(' ')
    code_entry.config(textvariable =  var)
def get_code():
    if code_entry.get() == 'may':
        coin_money['text']+=1000000
    else:print('code sai')
def code():
    global code_entry
    code_entry= Entry(root, width= 15)
    code_entry.place(anchor='se',x=400,y=325)
code()
btcode = Button(root,text='Nhận code',activebackground='#66FF66',activeforeground= '#FFFFFF',command=get_code)
btcode.place(anchor='se',x=400,y=350)
# HÀM RESET BOX CƯỢC 2 BÊN
def reset_box_tai():
    var = StringVar()
    var.set(' ')
    textBox_tai.config(textvariable =  var)
def reset_box_xiu():
    var = StringVar()
    var.set(' ')
    textBox_xiu.config(textvariable =  var)
#   BUTTON ĐẶT CƯỢC
def button_bet():
    bt_dat_tai=Button(root, height=1, width=10, text="BET",command=hai_ham(retrieve_input_tai,reset_box_tai,update_coin_cuoc_tai,tru_coin_khi_cuoc_tai)).grid(row=0,column=1,pady=230)
    bt_dat_xiu=Button(root, height=1, width=10, text="BET",command=hai_ham(retrieve_input_xiu,reset_box_xiu,update_coin_cuoc_xiu,tru_coin_khi_cuoc_xiu)).grid(row=0,column=2)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
button_bet()
#TEXT TX
def text_tx_big():
    text_Tai = Label(root,text='TÀI',fg='#000000',bg='#CCCCCC',font=('Perpetua',40)).place(anchor='w',x=80,y=100)
    text_XIU = Label(root,text='XỈU ',fg='#FFFFFF',bg='#444444',font=('Convection',34)).place(anchor='e',x=490,y=95)
text_tx_big()
# CHẠY TIỀN ẢO
def update_coin():
    if dem >= 5:
        global dem1
        global dem2
        global coin_fake_tai
        global coin_fake_xiu
        dem1 = random.randint(100000,700000)+random.randint(100000,700000)
        dem2 = random.randint(100000,700000)+random.randint(100000,700000)
        coin_fake_tai = text_coin_fake_tai['text'] + dem1
        text_coin_fake_tai['text'] = coin_fake_tai
        coin_fake_xiu = text_coin_fake_xiu['text'] + dem2
        text_coin_fake_xiu['text'] = coin_fake_xiu
        root.after(500, update_coin)
update_coin()

    



root.resizable(0,0)
root.mainloop()