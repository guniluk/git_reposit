from tkinter import *
from random import *

NUM_MOLES = 3

window = Tk()
window.title("두더지 게임")

moleFrame = Frame(window) #첫번째 프레임 생성
moleFrame.grid(row=0, column=0) # 첫번째 프레임을 루트 윈도우에 배치
statusFrame = Frame(window)  # 두번째 프레임 생성
statusFrame.grid(row=0, column=1) #두번째 프레인을 루트윈도우에 배치

hitLabel = Label(statusFrame, text="0 Hits")
hitLabel.pack()
missedLabel=Label(statusFrame, text="0 Misses")
missedLabel.pack()

mole_image = PhotoImage(file="/users/guniluk/desktop/pg/data/byh.gif")
no_mole_image = PhotoImage(file="/users/guniluk/desktop/pg/data/b.png")

numHits = 0
numMissed = 0

def mole_hit(c):  #사용자가 두더지를 잡았는지 체크
    global numHits, numMissed, molesList, missedLabel, hitLabel
    if molesList[c]["text"] == "mole" :
         numHits += 1
         hitLabel["text"] =str(numHits) + "Hits"
    else:
        numMissed += 1
        missedLabel["text"] = str(numMissed) + "Misses"
molesList = []

def init():
    count = 0
    for r in range(NUM_MOLES):
        for c in range(NUM_MOLES):
            button = Button(moleFrame, command= lambda c=count : mole_hit(c))
            button["image"] = no_mole_image
            button["text"] = "no mole"
            button.grid(row=r, column=c)
            molesList.append(button)
            count += 1
        
def update():
    global molesList
    for i in range(NUM_MOLES*NUM_MOLES):
        button = molesList[i]
        button["text"] = "no mole"
        button["image"] = no_mole_image
    x= randint(0, NUM_MOLES*NUM_MOLES-1)
    molesList[x]["image"] = mole_image
    molesList[x]["text"] = "mole"
    window.after(1000, update)

init()
update()
window.mainloop()