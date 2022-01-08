import datetime
from tkinter import *

import currency_converter.currency_converter
from currency_converter import CurrencyConverter
import sys

# Tkinter Setup

main = Tk()
main.title("Currency Converter API")
main.geometry("500x500")
c = CurrencyConverter()

# List, Variable, Function of the program

CurrencyList = ["USD", "THB", "PHP", "IDR", "BGN", "ILS", "HUF", "NOK"]

FirstVar = StringVar()
FirstVar.set(CurrencyList[0])
SecondVar = StringVar()
SecondVar.set(CurrencyList[1])

Advancing = IntVar()


def AdvanceDate():
    if Advancing.get() == 1:
        YearDate.grid(row=3, column=1)
        YearDateValue.grid(row=4, column=1)
        MonthDate.grid(row=5, column=1)
        MonthDateValue.grid(row=6, column=1)
        Date.grid(row=7, column=1)
        DateValue.grid(row=8, column=1)
    elif Advancing.get() == 0:
        YearDate.grid_forget()
        YearDateValue.grid_forget()
        MonthDate.grid_forget()
        MonthDateValue.grid_forget()
        Date.grid_forget()
        DateValue.grid_forget()


def Converting(event):
    try:
        FCurrency = FirstVar.get()
        SCurrency = SecondVar.get()
        Amount = int(CurrencyAmount.get())
        Year = int(YearDateValue.get())
        Month = int(MonthDateValue.get())
        Date = int(DateValue.get())
        date_obj = datetime.datetime(Year, Month, Date, 18, 36, 28, 151012)
    except:
        print("Error occurred when getting values")
        print(sys.exc_info()[0])

    try:
        if Advancing.get() == 0:
            FinalValue = c.convert(Amount, FCurrency, SCurrency)
            ShowResults.configure(text=FinalValue)
        elif Advancing.get() == 1:
            FinalValue = c.convert(Amount, FCurrency, SCurrency, date_obj)
            ShowResults.configure(text=FinalValue)
    except currency_converter.currency_converter.RateNotFoundError:
        print("Error occurred when calculating")
        print(sys.exc_info()[0])
        ShowResults.configure(text="Data not found")
    except:
        print("Error occurred when calculating")
        print(sys.exc_info()[0])
        ShowResults.configure(text="Error occurred")



# Tkinter UI

DropFirstValue = OptionMenu(main, FirstVar, *CurrencyList)
DropFirstValue.grid(row=0, column=0)

DropSecondValue = OptionMenu(main, SecondVar, *CurrencyList)
DropSecondValue.grid(row=0, column=1)

CurrencyAmount = Entry(main)
CurrencyAmount.grid(row=0, column=2)

CalculateButton = Button(main, text="Calculate")
CalculateButton.bind("<Button-1>", Converting)
CalculateButton.grid(row=1)

YearDate = Label(main, text="Year")
YearDateValue = Entry(main)

MonthDate = Label(main, text="Month")
MonthDateValue = Entry(main)

Date = Label(main, text="Day")
DateValue = Entry(main)

YearDate.grid_forget()
YearDateValue.grid_forget()
MonthDate.grid_forget()
MonthDateValue.grid_forget()
Date.grid_forget()
DateValue.grid_forget()

Advanced = Checkbutton(main, text="Advance option", variable=Advancing, command=AdvanceDate)
Advanced.grid(row=1, column=1)

ShowResults = Label(main, text="")
ShowResults.grid(row=2, column=2)


main.mainloop()
