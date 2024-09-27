import tkinter as tk
import tkinter as ttk
from tkinter.messagebox import showinfo
from tkinter import *
import random
import time

root = tk.Tk()
root.title("Lottery")

win_width = 600
win_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - win_width / 2)
center_y = int(screen_height/2 - win_height / 2)

root.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')

picked = 0
dawin = 0
inputnum = 1
nums = []

## We gotta make a function to every button, so that when they get clicked, the script adds the assigned value to the list.
def gambluuh1():
   inputnum = 1 
   gambluuh(inputnum)
def gambluuh2():
   inputnum = 2 
   gambluuh(inputnum)
def gambluuh3():
   inputnum = 3 
   gambluuh(inputnum)
def gambluuh4():
   inputnum = 4 
   gambluuh(inputnum)
def gambluuh5():
   inputnum = 5 
   gambluuh(inputnum)
def gambluuh6():
   inputnum = 6 
   gambluuh(inputnum)
def gambluuh7():
   inputnum = 7 
   gambluuh(inputnum)
def gambluuh8():
   inputnum = 8 
   gambluuh(inputnum)
def gambluuh9():
   inputnum = 9 
   gambluuh(inputnum)
def gambluuh10():
   inputnum = 10 
   gambluuh(inputnum)
def gambluuh11():
   inputnum = 11 
   gambluuh(inputnum)
def gambluuh12():
   inputnum = 12 
   gambluuh(inputnum)
def gambluuh13():
   inputnum = 13 
   gambluuh(inputnum)
def gambluuh14():
   inputnum = 14 
   gambluuh(inputnum)
def gambluuh15():
   inputnum = 15 
   gambluuh(inputnum)
def gambluuh16():
   inputnum = 16 
   gambluuh(inputnum)
def gambluuh17():
   inputnum = 17 
   gambluuh(inputnum)
def gambluuh18():
   inputnum = 18 
   gambluuh(inputnum)
def gambluuh19():
   inputnum = 19 
   gambluuh(inputnum)
def gambluuh20():
   inputnum = 20 
   gambluuh(inputnum)
def gambluuh21():
   inputnum = 21 
   gambluuh(inputnum)
def gambluuh22():
   inputnum = 22 
   gambluuh(inputnum)
def gambluuh23():
   inputnum = 23 
   gambluuh(inputnum)
def gambluuh24():
   inputnum = 24 
   gambluuh(inputnum)
def gambluuh25():
   inputnum = 25 
   gambluuh(inputnum)
def gambluuh26():
   inputnum = 26 
   gambluuh(inputnum)
def gambluuh27():
   inputnum = 27 
   gambluuh(inputnum)
def gambluuh28():
   inputnum = 28 
   gambluuh(inputnum)
def gambluuh29():
   inputnum = 29 
   gambluuh(inputnum)
def gambluuh30():
   inputnum = 30 
   gambluuh(inputnum)
def gambluuh31():
   inputnum = 31 
   gambluuh(inputnum)
def gambluuh32():
   inputnum = 32 
   gambluuh(inputnum)
def gambluuh33():
   inputnum = 33 
   gambluuh(inputnum)
def gambluuh34():
   inputnum = 34 
   gambluuh(inputnum)
def gambluuh35():
   inputnum = 35 
   gambluuh(inputnum)
def gambluuh36():
   inputnum = 36 
   gambluuh(inputnum)
def gambluuh37():
   inputnum = 37 
   gambluuh(inputnum)
def gambluuh38():
   inputnum = 38 
   gambluuh(inputnum)
def gambluuh39():
   inputnum = 39 
   gambluuh(inputnum)
def gambluuh40():
   inputnum = 40 
   gambluuh(inputnum)
def gambluuh41():
   inputnum = 41 
   gambluuh(inputnum)
def gambluuh42():
   inputnum = 42 
   gambluuh(inputnum)
def gambluuh43():
   inputnum = 43 
   gambluuh(inputnum)
def gambluuh44():
   inputnum = 44 
   gambluuh(inputnum)
def gambluuh45():
   inputnum = 45 
   gambluuh(inputnum)
def gambluuh46():
   inputnum = 46 
   gambluuh(inputnum)
def gambluuh47():
   inputnum = 47 
   gambluuh(inputnum)
def gambluuh48():
   inputnum = 48 
   gambluuh(inputnum)
def gambluuh49():
   inputnum = 49 
   gambluuh(inputnum)
def gambluuh50():
   inputnum = 50 
   gambluuh(inputnum)
def gambluuh51():
   inputnum = 51 
   gambluuh(inputnum)
def gambluuh52():
   inputnum = 52 
   gambluuh(inputnum)
def gambluuh53():
   inputnum = 53 
   gambluuh(inputnum)
def gambluuh54():
   inputnum = 54 
   gambluuh(inputnum)
def gambluuh55():
   inputnum = 55 
   gambluuh(inputnum)
def gambluuh56():
   inputnum = 56 
   gambluuh(inputnum)
def gambluuh57():
   inputnum = 57 
   gambluuh(inputnum)
def gambluuh58():
   inputnum = 58 
   gambluuh(inputnum)
def gambluuh59():
   inputnum = 59 
   gambluuh(inputnum)
def gambluuh60():
   inputnum = 60 
   gambluuh(inputnum)
def gambluuh61():
   inputnum = 61 
   gambluuh(inputnum)
def gambluuh62():
   inputnum = 62 
   gambluuh(inputnum)
def gambluuh63():
   inputnum = 63 
   gambluuh(inputnum)
def gambluuh64():
   inputnum = 64 
   gambluuh(inputnum)
def gambluuh65():
   inputnum = 65 
   gambluuh(inputnum)
def gambluuh66():
   inputnum = 66 
   gambluuh(inputnum)
def gambluuh67():
   inputnum = 67 
   gambluuh(inputnum)
def gambluuh68():
   inputnum = 68 
   gambluuh(inputnum)
def gambluuh69():
   inputnum = 69 
   gambluuh(inputnum)
def gambluuh70():
   inputnum = 70 
   gambluuh(inputnum)
def gambluuh71():
   inputnum = 71 
   gambluuh(inputnum)
def gambluuh72():
   inputnum = 72 
   gambluuh(inputnum)
def gambluuh73():
   inputnum = 73 
   gambluuh(inputnum)
def gambluuh74():
   inputnum = 74 
   gambluuh(inputnum)
def gambluuh75():
   inputnum = 75 
   gambluuh(inputnum)
def gambluuh76():
   inputnum = 76 
   gambluuh(inputnum)
def gambluuh77():
   inputnum = 77 
   gambluuh(inputnum)
def gambluuh78():
   inputnum = 78 
   gambluuh(inputnum)
def gambluuh79():
   inputnum = 79 
   gambluuh(inputnum)
def gambluuh80():
   inputnum = 80 
   gambluuh(inputnum)
def gambluuh81():
   inputnum = 81 
   gambluuh(inputnum)
def gambluuh82():
   inputnum = 82 
   gambluuh(inputnum)
def gambluuh83():
   inputnum = 83 
   gambluuh(inputnum)
def gambluuh84():
   inputnum = 84 
   gambluuh(inputnum)
def gambluuh85():
   inputnum = 85 
   gambluuh(inputnum)
def gambluuh86():
   inputnum = 86 
   gambluuh(inputnum)
def gambluuh87():
   inputnum = 87 
   gambluuh(inputnum)
def gambluuh88():
   inputnum = 88 
   gambluuh(inputnum)
def gambluuh89():
   inputnum = 89 
   gambluuh(inputnum)
def gambluuh90():
   inputnum = 90 
   gambluuh(inputnum)
def gambluuh91():
   inputnum = 91 
   gambluuh(inputnum)
def gambluuh92():
   inputnum = 92 
   gambluuh(inputnum)
def gambluuh93():
   inputnum = 93 
   gambluuh(inputnum)
def gambluuh94():
   inputnum = 94 
   gambluuh(inputnum)
def gambluuh95():
   inputnum = 95 
   gambluuh(inputnum)
def gambluuh96():
   inputnum = 96 
   gambluuh(inputnum)
def gambluuh97():
   inputnum = 97 
   gambluuh(inputnum)
def gambluuh98():
   inputnum = 98 
   gambluuh(inputnum)
def gambluuh99():
   inputnum = 99 
   gambluuh(inputnum)

## The winning numbers are "pulled" here.
def winnums():
   count = 0
   points = 0
   for x in nums:
      time.sleep(1.4)
      dawin = random.randint(1, 99)
      if dawin in nums:
         print(dawin)
         print("YOU GOT ONEEEE")
      else:
         if dawin+1 in nums:
            print(dawin)
            print("close")
         else:
            if dawin-1 in nums:
               print(dawin)
               print("close")
            else:
               print(dawin)
               print("AWW DANG IT")

## If the items in the list reached the amount of five, it'll start pulling the winning numbers
def gambluuh(inputnum):
    nums.append(inputnum)
    print(nums)
    if len(nums) == 5:
        winnums()

## These are the buttons ---------------------------------------------------------------------------------------------------------------------------------
## Obviously, this was procedurally created by another python script;

#     while counter < 99:
#         f.write("gamble_button"+str(numbahs)+" = ttk.Button(\n")
#         f.write(" root,\n")
#         f.write(" text="+str(numbahs)+",\n")
#         f.write(" compound=tk.LEFT,\n")
#         f.write(" command=gambluuh"+str(numbahs)+"\n")
#         f.write(")\n")

#         f.write("gamble_button"+str(numbahs)+".pack(\n")
#         f.write(" ipadx=5,\n")
#         f.write(" ipady=5,\n")
#         f.write(" expand=False\n")
#         f.write(")\n")
#         if x == 540:
#             x = 30
#             y += 30
#             f.write("gamble_button"+str(numbahs)+".place(x="+str(x)+", y="+str(y)+")\n")
#         else:
#             x += 30
#             f.write("gamble_button"+str(numbahs)+".place(x="+str(x)+", y="+str(y)+")\n")
#         counter +=1
#         numbahs +=1
# f.flush
# f.close

## -----------------------------------------------------------------------------------------------------------------------------------------------------


gamble_button1 = ttk.Button(
 root,
 text=1,
 compound=tk.LEFT,
 command=gambluuh1
)
gamble_button1.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button1.place(x=30, y=10)
gamble_button2 = ttk.Button(
 root,
 text=2,
 compound=tk.LEFT,
 command=gambluuh2
)
gamble_button2.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button2.place(x=60, y=10)
gamble_button3 = ttk.Button(
 root,
 text=3,
 compound=tk.LEFT,
 command=gambluuh3
)
gamble_button3.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button3.place(x=90, y=10)
gamble_button4 = ttk.Button(
 root,
 text=4,
 compound=tk.LEFT,
 command=gambluuh4
)
gamble_button4.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button4.place(x=120, y=10)
gamble_button5 = ttk.Button(
 root,
 text=5,
 compound=tk.LEFT,
 command=gambluuh5
)
gamble_button5.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button5.place(x=150, y=10)
gamble_button6 = ttk.Button(
 root,
 text=6,
 compound=tk.LEFT,
 command=gambluuh6
)
gamble_button6.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button6.place(x=180, y=10)
gamble_button7 = ttk.Button(
 root,
 text=7,
 compound=tk.LEFT,
 command=gambluuh7
)
gamble_button7.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button7.place(x=210, y=10)
gamble_button8 = ttk.Button(
 root,
 text=8,
 compound=tk.LEFT,
 command=gambluuh8
)
gamble_button8.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button8.place(x=240, y=10)
gamble_button9 = ttk.Button(
 root,
 text=9,
 compound=tk.LEFT,
 command=gambluuh9
)
gamble_button9.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button9.place(x=270, y=10)
gamble_button10 = ttk.Button(
 root,
 text=10,
 compound=tk.LEFT,
 command=gambluuh10
)
gamble_button10.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button10.place(x=300, y=10)
gamble_button11 = ttk.Button(
 root,
 text=11,
 compound=tk.LEFT,
 command=gambluuh11
)
gamble_button11.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button11.place(x=330, y=10)
gamble_button12 = ttk.Button(
 root,
 text=12,
 compound=tk.LEFT,
 command=gambluuh12
)
gamble_button12.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button12.place(x=360, y=10)
gamble_button13 = ttk.Button(
 root,
 text=13,
 compound=tk.LEFT,
 command=gambluuh13
)
gamble_button13.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button13.place(x=390, y=10)
gamble_button14 = ttk.Button(
 root,
 text=14,
 compound=tk.LEFT,
 command=gambluuh14
)
gamble_button14.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button14.place(x=420, y=10)
gamble_button15 = ttk.Button(
 root,
 text=15,
 compound=tk.LEFT,
 command=gambluuh15
)
gamble_button15.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button15.place(x=450, y=10)
gamble_button16 = ttk.Button(
 root,
 text=16,
 compound=tk.LEFT,
 command=gambluuh16
)
gamble_button16.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button16.place(x=480, y=10)
gamble_button17 = ttk.Button(
 root,
 text=17,
 compound=tk.LEFT,
 command=gambluuh17
)
gamble_button17.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button17.place(x=510, y=10)
gamble_button18 = ttk.Button(
 root,
 text=18,
 compound=tk.LEFT,
 command=gambluuh18
)
gamble_button18.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button18.place(x=540, y=10)
gamble_button19 = ttk.Button(
 root,
 text=19,
 compound=tk.LEFT,
 command=gambluuh19
)
gamble_button19.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button19.place(x=30, y=40)
gamble_button20 = ttk.Button(
 root,
 text=20,
 compound=tk.LEFT,
 command=gambluuh20
)
gamble_button20.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button20.place(x=60, y=40)
gamble_button21 = ttk.Button(
 root,
 text=21,
 compound=tk.LEFT,
 command=gambluuh21
)
gamble_button21.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button21.place(x=90, y=40)
gamble_button22 = ttk.Button(
 root,
 text=22,
 compound=tk.LEFT,
 command=gambluuh22
)
gamble_button22.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button22.place(x=120, y=40)
gamble_button23 = ttk.Button(
 root,
 text=23,
 compound=tk.LEFT,
 command=gambluuh23
)
gamble_button23.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button23.place(x=150, y=40)
gamble_button24 = ttk.Button(
 root,
 text=24,
 compound=tk.LEFT,
 command=gambluuh24
)
gamble_button24.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button24.place(x=180, y=40)
gamble_button25 = ttk.Button(
 root,
 text=25,
 compound=tk.LEFT,
 command=gambluuh25
)
gamble_button25.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button25.place(x=210, y=40)
gamble_button26 = ttk.Button(
 root,
 text=26,
 compound=tk.LEFT,
 command=gambluuh26
)
gamble_button26.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button26.place(x=240, y=40)
gamble_button27 = ttk.Button(
 root,
 text=27,
 compound=tk.LEFT,
 command=gambluuh27
)
gamble_button27.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button27.place(x=270, y=40)
gamble_button28 = ttk.Button(
 root,
 text=28,
 compound=tk.LEFT,
 command=gambluuh28
)
gamble_button28.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button28.place(x=300, y=40)
gamble_button29 = ttk.Button(
 root,
 text=29,
 compound=tk.LEFT,
 command=gambluuh29
)
gamble_button29.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button29.place(x=330, y=40)
gamble_button30 = ttk.Button(
 root,
 text=30,
 compound=tk.LEFT,
 command=gambluuh30
)
gamble_button30.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button30.place(x=360, y=40)
gamble_button31 = ttk.Button(
 root,
 text=31,
 compound=tk.LEFT,
 command=gambluuh31
)
gamble_button31.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button31.place(x=390, y=40)
gamble_button32 = ttk.Button(
 root,
 text=32,
 compound=tk.LEFT,
 command=gambluuh32
)
gamble_button32.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button32.place(x=420, y=40)
gamble_button33 = ttk.Button(
 root,
 text=33,
 compound=tk.LEFT,
 command=gambluuh33
)
gamble_button33.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button33.place(x=450, y=40)
gamble_button34 = ttk.Button(
 root,
 text=34,
 compound=tk.LEFT,
 command=gambluuh34
)
gamble_button34.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button34.place(x=480, y=40)
gamble_button35 = ttk.Button(
 root,
 text=35,
 compound=tk.LEFT,
 command=gambluuh35
)
gamble_button35.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button35.place(x=510, y=40)
gamble_button36 = ttk.Button(
 root,
 text=36,
 compound=tk.LEFT,
 command=gambluuh36
)
gamble_button36.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button36.place(x=540, y=40)
gamble_button37 = ttk.Button(
 root,
 text=37,
 compound=tk.LEFT,
 command=gambluuh37
)
gamble_button37.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button37.place(x=30, y=70)
gamble_button38 = ttk.Button(
 root,
 text=38,
 compound=tk.LEFT,
 command=gambluuh38
)
gamble_button38.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button38.place(x=60, y=70)
gamble_button39 = ttk.Button(
 root,
 text=39,
 compound=tk.LEFT,
 command=gambluuh39
)
gamble_button39.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button39.place(x=90, y=70)
gamble_button40 = ttk.Button(
 root,
 text=40,
 compound=tk.LEFT,
 command=gambluuh40
)
gamble_button40.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button40.place(x=120, y=70)
gamble_button41 = ttk.Button(
 root,
 text=41,
 compound=tk.LEFT,
 command=gambluuh41
)
gamble_button41.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button41.place(x=150, y=70)
gamble_button42 = ttk.Button(
 root,
 text=42,
 compound=tk.LEFT,
 command=gambluuh42
)
gamble_button42.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button42.place(x=180, y=70)
gamble_button43 = ttk.Button(
 root,
 text=43,
 compound=tk.LEFT,
 command=gambluuh43
)
gamble_button43.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button43.place(x=210, y=70)
gamble_button44 = ttk.Button(
 root,
 text=44,
 compound=tk.LEFT,
 command=gambluuh44
)
gamble_button44.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button44.place(x=240, y=70)
gamble_button45 = ttk.Button(
 root,
 text=45,
 compound=tk.LEFT,
 command=gambluuh45
)
gamble_button45.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button45.place(x=270, y=70)
gamble_button46 = ttk.Button(
 root,
 text=46,
 compound=tk.LEFT,
 command=gambluuh46
)
gamble_button46.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button46.place(x=300, y=70)
gamble_button47 = ttk.Button(
 root,
 text=47,
 compound=tk.LEFT,
 command=gambluuh47
)
gamble_button47.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button47.place(x=330, y=70)
gamble_button48 = ttk.Button(
 root,
 text=48,
 compound=tk.LEFT,
 command=gambluuh48
)
gamble_button48.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button48.place(x=360, y=70)
gamble_button49 = ttk.Button(
 root,
 text=49,
 compound=tk.LEFT,
 command=gambluuh49
)
gamble_button49.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button49.place(x=390, y=70)
gamble_button50 = ttk.Button(
 root,
 text=50,
 compound=tk.LEFT,
 command=gambluuh50
)
gamble_button50.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button50.place(x=420, y=70)
gamble_button51 = ttk.Button(
 root,
 text=51,
 compound=tk.LEFT,
 command=gambluuh51
)
gamble_button51.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button51.place(x=450, y=70)
gamble_button52 = ttk.Button(
 root,
 text=52,
 compound=tk.LEFT,
 command=gambluuh52
)
gamble_button52.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button52.place(x=480, y=70)
gamble_button53 = ttk.Button(
 root,
 text=53,
 compound=tk.LEFT,
 command=gambluuh53
)
gamble_button53.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button53.place(x=510, y=70)
gamble_button54 = ttk.Button(
 root,
 text=54,
 compound=tk.LEFT,
 command=gambluuh54
)
gamble_button54.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button54.place(x=540, y=70)
gamble_button55 = ttk.Button(
 root,
 text=55,
 compound=tk.LEFT,
 command=gambluuh55
)
gamble_button55.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button55.place(x=30, y=100)
gamble_button56 = ttk.Button(
 root,
 text=56,
 compound=tk.LEFT,
 command=gambluuh56
)
gamble_button56.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button56.place(x=60, y=100)
gamble_button57 = ttk.Button(
 root,
 text=57,
 compound=tk.LEFT,
 command=gambluuh57
)
gamble_button57.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button57.place(x=90, y=100)
gamble_button58 = ttk.Button(
 root,
 text=58,
 compound=tk.LEFT,
 command=gambluuh58
)
gamble_button58.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button58.place(x=120, y=100)
gamble_button59 = ttk.Button(
 root,
 text=59,
 compound=tk.LEFT,
 command=gambluuh59
)
gamble_button59.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button59.place(x=150, y=100)
gamble_button60 = ttk.Button(
 root,
 text=60,
 compound=tk.LEFT,
 command=gambluuh60
)
gamble_button60.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button60.place(x=180, y=100)
gamble_button61 = ttk.Button(
 root,
 text=61,
 compound=tk.LEFT,
 command=gambluuh61
)
gamble_button61.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button61.place(x=210, y=100)
gamble_button62 = ttk.Button(
 root,
 text=62,
 compound=tk.LEFT,
 command=gambluuh62
)
gamble_button62.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button62.place(x=240, y=100)
gamble_button63 = ttk.Button(
 root,
 text=63,
 compound=tk.LEFT,
 command=gambluuh63
)
gamble_button63.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button63.place(x=270, y=100)
gamble_button64 = ttk.Button(
 root,
 text=64,
 compound=tk.LEFT,
 command=gambluuh64
)
gamble_button64.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button64.place(x=300, y=100)
gamble_button65 = ttk.Button(
 root,
 text=65,
 compound=tk.LEFT,
 command=gambluuh65
)
gamble_button65.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button65.place(x=330, y=100)
gamble_button66 = ttk.Button(
 root,
 text=66,
 compound=tk.LEFT,
 command=gambluuh66
)
gamble_button66.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button66.place(x=360, y=100)
gamble_button67 = ttk.Button(
 root,
 text=67,
 compound=tk.LEFT,
 command=gambluuh67
)
gamble_button67.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button67.place(x=390, y=100)
gamble_button68 = ttk.Button(
 root,
 text=68,
 compound=tk.LEFT,
 command=gambluuh68
)
gamble_button68.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button68.place(x=420, y=100)
gamble_button69 = ttk.Button(
 root,
 text=69,
 compound=tk.LEFT,
 command=gambluuh69
)
gamble_button69.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button69.place(x=450, y=100)
gamble_button70 = ttk.Button(
 root,
 text=70,
 compound=tk.LEFT,
 command=gambluuh70
)
gamble_button70.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button70.place(x=480, y=100)
gamble_button71 = ttk.Button(
 root,
 text=71,
 compound=tk.LEFT,
 command=gambluuh71
)
gamble_button71.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button71.place(x=510, y=100)
gamble_button72 = ttk.Button(
 root,
 text=72,
 compound=tk.LEFT,
 command=gambluuh72
)
gamble_button72.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button72.place(x=540, y=100)
gamble_button73 = ttk.Button(
 root,
 text=73,
 compound=tk.LEFT,
 command=gambluuh73
)
gamble_button73.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button73.place(x=30, y=130)
gamble_button74 = ttk.Button(
 root,
 text=74,
 compound=tk.LEFT,
 command=gambluuh74
)
gamble_button74.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button74.place(x=60, y=130)
gamble_button75 = ttk.Button(
 root,
 text=75,
 compound=tk.LEFT,
 command=gambluuh75
)
gamble_button75.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button75.place(x=90, y=130)
gamble_button76 = ttk.Button(
 root,
 text=76,
 compound=tk.LEFT,
 command=gambluuh76
)
gamble_button76.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button76.place(x=120, y=130)
gamble_button77 = ttk.Button(
 root,
 text=77,
 compound=tk.LEFT,
 command=gambluuh77
)
gamble_button77.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button77.place(x=150, y=130)
gamble_button78 = ttk.Button(
 root,
 text=78,
 compound=tk.LEFT,
 command=gambluuh78
)
gamble_button78.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button78.place(x=180, y=130)
gamble_button79 = ttk.Button(
 root,
 text=79,
 compound=tk.LEFT,
 command=gambluuh79
)
gamble_button79.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button79.place(x=210, y=130)
gamble_button80 = ttk.Button(
 root,
 text=80,
 compound=tk.LEFT,
 command=gambluuh80
)
gamble_button80.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button80.place(x=240, y=130)
gamble_button81 = ttk.Button(
 root,
 text=81,
 compound=tk.LEFT,
 command=gambluuh81
)
gamble_button81.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button81.place(x=270, y=130)
gamble_button82 = ttk.Button(
 root,
 text=82,
 compound=tk.LEFT,
 command=gambluuh82
)
gamble_button82.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button82.place(x=300, y=130)
gamble_button83 = ttk.Button(
 root,
 text=83,
 compound=tk.LEFT,
 command=gambluuh83
)
gamble_button83.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button83.place(x=330, y=130)
gamble_button84 = ttk.Button(
 root,
 text=84,
 compound=tk.LEFT,
 command=gambluuh84
)
gamble_button84.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button84.place(x=360, y=130)
gamble_button85 = ttk.Button(
 root,
 text=85,
 compound=tk.LEFT,
 command=gambluuh85
)
gamble_button85.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button85.place(x=390, y=130)
gamble_button86 = ttk.Button(
 root,
 text=86,
 compound=tk.LEFT,
 command=gambluuh86
)
gamble_button86.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button86.place(x=420, y=130)
gamble_button87 = ttk.Button(
 root,
 text=87,
 compound=tk.LEFT,
 command=gambluuh87
)
gamble_button87.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button87.place(x=450, y=130)
gamble_button88 = ttk.Button(
 root,
 text=88,
 compound=tk.LEFT,
 command=gambluuh88
)
gamble_button88.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button88.place(x=480, y=130)
gamble_button89 = ttk.Button(
 root,
 text=89,
 compound=tk.LEFT,
 command=gambluuh89
)
gamble_button89.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button89.place(x=510, y=130)
gamble_button90 = ttk.Button(
 root,
 text=90,
 compound=tk.LEFT,
 command=gambluuh90
)
gamble_button90.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button90.place(x=540, y=130)
gamble_button91 = ttk.Button(
 root,
 text=91,
 compound=tk.LEFT,
 command=gambluuh91
)
gamble_button91.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button91.place(x=30, y=160)
gamble_button92 = ttk.Button(
 root,
 text=92,
 compound=tk.LEFT,
 command=gambluuh92
)
gamble_button92.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button92.place(x=60, y=160)
gamble_button93 = ttk.Button(
 root,
 text=93,
 compound=tk.LEFT,
 command=gambluuh93
)
gamble_button93.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button93.place(x=90, y=160)
gamble_button94 = ttk.Button(
 root,
 text=94,
 compound=tk.LEFT,
 command=gambluuh94
)
gamble_button94.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button94.place(x=120, y=160)
gamble_button95 = ttk.Button(
 root,
 text=95,
 compound=tk.LEFT,
 command=gambluuh95
)
gamble_button95.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button95.place(x=150, y=160)
gamble_button96 = ttk.Button(
 root,
 text=96,
 compound=tk.LEFT,
 command=gambluuh96
)
gamble_button96.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button96.place(x=180, y=160)
gamble_button97 = ttk.Button(
 root,
 text=97,
 compound=tk.LEFT,
 command=gambluuh97
)
gamble_button97.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button97.place(x=210, y=160)
gamble_button98 = ttk.Button(
 root,
 text=98,
 compound=tk.LEFT,
 command=gambluuh98
)
gamble_button98.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button98.place(x=240, y=160)
gamble_button99 = ttk.Button(
 root,
 text=99,
 compound=tk.LEFT,
 command=gambluuh99
)
gamble_button99.pack(
 ipadx=5,
 ipady=5,
 expand=False
)
gamble_button99.place(x=270, y=160)

root.mainloop()
