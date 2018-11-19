import Tkinter
import random
win = Tkinter.Tk()
win.title('Dice Roller')

def mainloop():
    class Die:
        def __init__(self,ivalue, parent):
            self.value = ivalue
            self.display = Tkinter.Label(parent,relief='ridge',borderwidth=4, text=str(self.value))
        def roll(self):
            self.value = random.randint(1,6)
            self.display.config(text=str(self.value))
    class diceRoller:    
        def rolldice():
            d1.roll()
            d2.roll()
            d3.roll()
        def __init__(self):
                self.diceList = []
                self.win = Tkinter.Tk("Dice Roller")

                for i in range(3):
                    di = Die(self.win)
                    self.dieList.append(di)
                    rolldice()

    row1 = Tkinter.Frame(win)
    row2 = Tkinter.Frame(win)
    d1.roll.display.pack(side="left")
    d2.roll.display.pack(side="left")
    d3.roll.display.pack(side="left")
    row1.pack()
    rolldice = Tkinter.Button(row2, command=rolldice(), text = "Roll")
    rolldice.pack()
    row2.pack()


 win.mainloop()