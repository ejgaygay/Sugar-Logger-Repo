# This one has type in boxes for the hours instead of the drop down combo boxes
#For next time from 12/31/20 5:20am - find out how to clear that label that tells you you added data
#add a function to remove the last entry
from tkinter import *
from tkinter.ttk import *
from datetime import datetime

class MonthGUI:
    def destroyit(self):
        self.master.destroy()
        file = open(self.get_month()+"_log_" + str(datetime.now().year) + ".txt",'w')
        file.write(self.get_month()+"\n")
        file.close()
        menu2 = Tk()
        dataMenu = SugarDataGUI(menu2)
        menu2.mainloop()

    def __init__(self,master):
        self.master = master
        master.title("Month Menu")
        master.geometry("250x250")

        self.monthChoices = StringVar(master)
        self.monthBox = Combobox(master, textvariable=self.monthChoices)
        self.monthBox.set("January")
        self.monthBox['values'] = (
            "January","February",'March',
            'April','May','June',
            'July','August','September',
            'October','November','December'
        )
        self.monthBox.pack()

        self.dayChoices = StringVar(master)
        self.days = Combobox(master, textvariable=self.dayChoices)
        self.days.set('1')
        self.days['values'] = (
            '1',
            '2','3','4','5','6','7','8','9','10',
            '11','12','13','14','15','16','17','18','19',
            '20','21','22','23','24','25','26','27','28','29',
            '30','31'
        )
        self.days.pack()

        self.proceedButton = Button(
            master, text = 'Enter', command=self.destroyit).pack()

    def get_month(self):
        return str(self.monthChoices.get())

    def get_day(self):
        return str(self.dayChoices.get())

class SugarDataGUI:
    def __init__(self,master):
        self.dayCounter = 0
        listMonth30 = ['april','june','september','november']
        listMonth31 = ['january','march','may','july','october','december']
        if monthMenu.get_month().lower() in listMonth31:
            self.endDay = 31
        elif monthMenu.get_month().lower() in listMonth30:
            self.endDay = 30
        elif datetime.now().year%4 == 0 and datetime.now().year%100 != 0:
            self.endDay = 29
        elif datetime.now().year%100 == 0 and datetime.now().year ==0:
            self.endDay = 29
        else:
            self.endDay = 28
        self.day = int(monthMenu.get_day())
        file = open(monthMenu.get_month()+"_log_" + str(datetime.now().year) + ".txt",'a')
        file.write(str(self.day)+ " - ")
        file.close
        self.master = master
        master.title("Enter Data")

        self.dataLabel = Label(master,text = "").grid(row=12,column=0)

        self.daylabel = Label(master,text = "Day " + \
                              str(self.day)).grid(row=0,column=0)
        self.hourLabel = Label(master,text='Hour').grid(row=1,column=0)
        self.hourEntry = Entry(master)
        self.hourEntry.grid(row = 2, column = 0)

        self.minutesLabel = Label(master,text='Minute').grid(row=3,column=0)
        self.minuteEntry = Entry(master)
        self.minuteEntry.grid(row = 4, column = 0)
#This is if i want it as a combo box
        self.timeChoices = StringVar(master)
        '''
        self.timeDay = Combobox(master, textvariable=self.timeChoices)
        self.timeDay.set("AM")
        self.timeDay['values'] = (
            'AM','PM'
        )
        self.timeDay.grid(row=5,column=0)
        '''
#Not a combo box version
        self.time1 = Radiobutton(
            master, text = "AM", variable = self.timeChoices,value = "AM"
        ).grid(row = 5, column = 0)
        self.time2 = Radiobutton(
            master,text = "PM", variable = self.timeChoices, value = "PM"
        ).grid(row = 6, column = 0)

        Label(master,text= 'Pick one').grid(row=0,column = 1)
        self.mealWhen = StringVar(master)
        self.beforeBre = Radiobutton(
            master,text='Before Breakfast',variable = self.mealWhen, value = 'Before Breakfast')
        self.beforeBre.grid(row=1,column=1)
        self.afterBre = Radiobutton(
            master,text='After Breakfast',variable = self.mealWhen,value = 'After Breakfast')
        self.afterBre.grid(row=2,column=1)
        self.beforeLu = Radiobutton(
            master,text='Before Lunch',variable = self.mealWhen, value = 'Before Lunch')
        self.beforeLu.grid(row=3,column=1)
        self.afterLu = Radiobutton(
            master,text='After Lunch',variable = self.mealWhen,value = 'After Lunch')
        self.afterLu.grid(row=4,column=1)
        self.beforeDi = Radiobutton(
            master,text='Before Dinner',variable = self.mealWhen, value = 'Before Dinner')
        self.beforeDi.grid(row=5,column=1)
        self.afterDi = Radiobutton(
            master,text='After Dinner',variable = self.mealWhen,value = 'After Dinner')
        self.afterDi.grid(row=6,column=1)
        self.unknownMeal = Radiobutton(
            master, text = "Do not know", variable = self.mealWhen, value = 'Do not know')
        self.unknownMeal.grid(row=7,column=1)
        self.forgot = Radiobutton(
            master,text = 'Forgot to Check', variable = self.mealWhen, value = "Forgot to Check")
        self.forgot.grid(row=8,column=1)

        self.sugarLabel = Label(master,text='Sugar Level').grid(row=7,column=0)
        self.dataEntry = Entry(master)
        self.dataEntry.grid(row=8,column=0)

        self.enterButton = Button(
            master,text="Enter",command=self.writeData).grid(row=9,column=0)
        self.quitButton = Button(
            master, text='Quit', command=self.quit).grid(row=10,column=0)

    def writeData(self):
        file = open(monthMenu.get_month()+"_log_" + str(datetime.now().year) + ".txt",'a')
        if self.mealWhen.get().lower() == "forgot to check":
            file.write(self.mealWhen.get() + " - ")
            self.dataLabel = Label(self.master, text = "Forgot to Check added").grid(row=12,column=0)
        else:
            file.write(str(self.mealWhen.get()) + " at " + str(self.hourEntry.get()) + ":"+str(
                self.minuteEntry.get()) + self.timeChoices.get() + " - " + str(self.dataEntry.get()) + "mg/dL - ")
            self.dataLabel = Label(self.master,text = 
              self.dataEntry.get() + "mg/dL at "  + self.hourEntry.get() + ":" + self.minuteEntry.get()\
                  + self.timeChoices.get() + " added").grid(row=12,column=0)
        file.close()
        self.dataEntry.delete(0,'end')
        self.hourEntry.delete(0,'end')
        self.minuteEntry.delete(0,'end')
        self.mealWhen.set(-1)
        self.timeChoices.set(-1)
        self.dayCounter +=1 
        if self.dayCounter == 3:
            self.dayCounter = 0
            self.newDay()       

    def newDay(self):
        file = open(monthMenu.get_month()+"_log_" + str(datetime.now().year) + ".txt",'a')
        self.day += 1
        if self.day > self.endDay:
            quit()
        self.dayLabel = Label(self.master,text = "Day " + \
                              str(self.day)).grid(row=0,column=0)
        file.write("\n" + str(self.day) + " - ")
        file.close()

    def quit(self):
        self.master.destroy()
        quit()

menu1 = Tk()
monthMenu = MonthGUI(menu1)
menu1.mainloop()
