#!/usr/bin/python3
#!-*-encoding:utf-8-*-

import tkinter as tk
from functools import partial

def call_result(label_result, n1, n2):
    num1 = float((n1.get()))
    num2 = float((n2.get()))
    result = (num1)/(num2*num2)
    if result<=18.5:
        label_result.config(text="Vous êtes en souspoids.\n"
                                 "Votre BMI (IMC) est de : %d" % result)
        return
    elif result>=18.5 and result<=25:
        label_result.config(text="Votre BMI est dans les normes.\n"
                                 "Votre BMI (IMC) est de : %d" % result)
        return
    elif result>=18.5 and result<=25:
        label_result.config(text="Votre BMI est dans les normes.\n"
                                 "Votre BMI (IMC) est de : %d" % result)
        return
    else:
        label_result.config(text="Vous êtes en surpoids.\n"
                                 "Votre BMI (IMC) est de : %d" % result)  
        return


root = tk.Tk()
root.geometry('350x200+100+200')
root.title('Simple BMIcalculator')

number1 = tk.StringVar()
number2 = tk.StringVar()

labelTitle = tk.Label(root, text="Simple BMI").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Entrez le poids en Kg :").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Entrez la taille en M :").grid(row=2, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=4, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
call_result = partial(call_result, labelResult, number1, number2)
buttonCal = tk.Button(root, text="Calculer", command=call_result).grid(row=3, column=0)
buttonCal2 = tk.Button(root, text="Quitter", command=quit).grid(row=7, column=0)
root.mainloop()