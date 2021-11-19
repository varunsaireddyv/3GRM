import builtins
from tkinter import *
from tkinter import filedialog
import sqlite3
#import Diet_Dynamic
import sqlite3



connection = sqlite3.connect('/home/rajesh/Desktop/3grmvarun/3GRM/Programming/diet/DietAssistantDatabase.db')
cursor= connection.cursor()

root=Tk()
first_name_var=StringVar()
last_name_var=StringVar()
age_name_var=StringVar()
mail_name_var=StringVar()


frame=LabelFrame(root, text='', pady=5, padx=5)
frame.pack()

root.title('Diet Asistant')
root.geometry('570x540')

def clear():
    connection = sqlite3.connect('/home/rajesh/Desktop/3grmvarun/3GRM/Programming/diet/DietAssistantDatabase.db')
    cursor=connection.cursor()    
    for widget in frame.winfo_children():
        widget.destroy()

    menu_options=['beverages', 'sandwiches', 'aptizers', 'salads']
    
    global cliked_submenu
    cliked_submenu= StringVar()
    cliked_submenu.set(menu_options[0])

    submenu_dropdown=OptionMenu(frame, cliked_submenu, *menu_options, command=itempopup)
    submenu_dropdown.pack()

    Params = {'first': first_name_var.get(), 'last': last_name_var.get(), 'mail': mail_name_var.get(), 'age': age_name_var.get()}
    query = "INSERT INTO UserDataDiet(first, last, mail, age) VALUES (:first, :last, :mail, :age)"
    cursor.execute(query, Params)
    query2="INSERT INTO UserDataDisease VALUES (:cancer, :dt1, :dt2, :chf, :kidney, :bonebreak, :mail)"
    Params2={'cancer': cancerpatient.get(), 'dt1': dt1patient.get(), 'dt2': dt2patient.get(), 'chf': CHFpatient.get(), 'kidney': kidneypatient.get(), 'bonebreak': bonebreak.get(), 'mail':mail_name_var.get()}
    cursor.execute(query2, Params2)
    connection.commit
    
def itempopup(event):
    dessicionlabel=Label(frame, text=cliked_submenu.get())
    if cliked_submenu.get() == 'beverages':
        beverages_options=['mocha', 'frappe', 'soda', 'cola']
        quantity=['1', '2', '3', '4', '5']

        clicedbeverages= StringVar()
        clicedbeverages.set(beverages_options[0])
        clickedquantity=StringVar()
        clickedquantity.set(quantity[0])

        global quantity_dropdown
        global beverage_dropdown
        beverage_dropdown=OptionMenu(frame, clicedbeverages, *beverages_options,)
        beverage_dropdown.pack()
        quantity_dropdown=OptionMenu(frame, clickedquantity, *quantity)
        quantity_dropdown.pack( )
        dessicionlabel=Label(frame, text=clicedbeverages.get())
        itempopupcuntinue=Button(frame, text='continue', command=reset).pack()
        checkout=Button(frame, text='check out', command=calorielow).pack()

def reset():
    quantity_dropdown.destroy()
    beverage_dropdown.destroy()

def calorielow():
    for widget in frame.winfo_children():
        widget.destroy()
    calorielowsdisplay=Label(frame, text='you dont have enough calories in this meal').pack()       
    addtocurrentmeal=Button(frame, text='add caliries to this meal').pack()
    addtonextmeal=Button(frame, text='add calories to next meal ').pack()
    proceed=Button(frame, text='procced').pack()


def caloriehigh():


    for widget in frame.winfo_children():
        widget.destroy()
    caloriehighsdisplay=Label(frame, text='you dont have enough calories in this meal').pack()       
    removefromcurrentmeal=Button(frame, text='add caliries to this meal').pack()
    removefromnextmeal=Button(frame, text='add calories to next meal ').pack()
    proceed=Button(frame, text='procced').pack()  




     

def login():
    email_input=Entry(frame,   width='40')
    email_input.insert(END, 'enter email for login')
    email_input.pack()

        
        
def signup():
    for widget in frame.winfo_children():
        widget.destroy()
    global first_name
    global last_name
    global age
    global mail
    global cancerpatient
    global dt1patient
    global dt2patient
    global CHFpatient
    global kidneypatient
    global bonebreak

    
    first_name=Entry(frame, textvariable = first_name_var, width='40')
    last_name=Entry(frame,  textvariable = last_name_var, width='40')
    age=Entry(frame, textvariable = age_name_var, width='40')
    mail=Entry(frame, textvariable = mail_name_var, width='40')


    first_name.pack()
    last_name.pack()
    age.pack()
    mail.pack()
    cancerpatient=StringVar()
    cancerpatientdiplay=Label(frame, text='do you have cancer').pack()
    Radiobutton(frame, text='yes', variable=cancerpatient, value=1).pack()
    Radiobutton(frame, text='no', variable=cancerpatient, value=0).pack() 

    dt1patient=StringVar()
    dt1patientdisply=Label(frame, text='do you have diabeties type1').pack()
    Radiobutton(frame, text='yes', variable=dt1patient, value=1).pack()
    Radiobutton(frame, text='no', variable=dt1patient, value=0).pack()

    dt2patient=StringVar()
    dt2patientdiplay=Label(frame, text='do you have diabeteis type2').pack()
    Radiobutton(frame, text='yes', variable=dt2patient, value=1).pack()
    Radiobutton(frame, text='no', variable=dt2patient, value=0).pack()

    CHFpatient=StringVar()
    CHFpatientdisplay=Label(frame, text='did you have a chronic stroke in the past few weeks or have them regularly').pack()
    Radiobutton(frame, text='yes', variable=CHFpatient, value=1).pack()
    Radiobutton(frame, text='no', variable=CHFpatient, value=0).pack()

    kidneypatient=StringVar()
    kidneypatientdisplay=Label(frame, text='do you have kidney stones').pack()
    Radiobutton(frame, text='yes', variable=kidneypatient, value=1).pack()
    Radiobutton(frame, text='no', variable=kidneypatient, value=0).pack()

    bonebreak=StringVar()
    bonebreakdisplay=Label(frame, text='where you in a accident in recent months').pack()
    Radiobutton(frame, text='yes', variable=bonebreak, value=1).pack()
    Radiobutton(frame, text='no', variable=bonebreak, value=0).pack()
    continuebutton=Button(frame, text='continue', command=clear).pack()

    

    


loginbutton=Button(frame, text='login', command=login).pack()
signupbutton=Button(frame, text='sign up', command=signup).pack()


frame.mainloop() 
connection.commit
