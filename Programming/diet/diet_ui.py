from tkinter import *
from tkinter import filedialog

root=Tk()
frame=LabelFrame(root, text='', pady=5, padx=5)
frame.pack()

def itempopup(event):
    dessicionlabel=Label(frame, text=cliked_submenu.get())
    if cliked_submenu.get() == 'beverages':
        beverages_options=['mocha', 'frappe', 'soda', 'cola']
        quantity=['1', '2', '3', '4', '5']

        clicedbeverages= StringVar()
        clicedbeverages.set(beverages_options[0])
        clickedquantity=StringVar()
        clickedquantity.set(quantity[0])

        beverage_dropdown=OptionMenu(frame, clicedbeverages, *beverages_options,)
        beverage_dropdown.pack()
        quantity_dropdown=OptionMenu(frame, clickedquantity, *quantity)
        quantity_dropdown.pack( )
        dessicionlabel=Label(frame, text=clicedbeverages.get())


def clear():
    for widget in frame.winfo_children():
        widget.destroy()
    submenu_options=['beverages', 'sandwiches', 'aptizers', 'salads']
    
    global cliked_submenu
    cliked_submenu= StringVar()
    cliked_submenu.set(submenu_options[0])

    submenu_dropdown=OptionMenu(frame, cliked_submenu, *submenu_options, command=itempopup)
    submenu_dropdown.pack()


def login():
    email_input=Text(frame, height='1',  width='40')
    email_input.insert(frame, 'enter email for ligin')
    email_input.pack()
def signup():
    for widget in frame.winfo_children():
        widget.destroy()
    first_name=Text(frame, height='1',  width='40')
    last_name=Text(frame, height='1',  width='40')
    age=Text(frame, height='1',  width='40')
    mail=Text(frame, height='1',  width='40')
    first_name.insert(END, 'first name')
    last_name.insert(END, 'last name')
    age.insert(END, 'age')
    mail.insert(END, 'mail')

    first_name.pack()
    last_name.pack()
    age.pack()
    mail.pack()
    cancerpatient=StringVar()
    cancerpatientdiplay=Label(frame, text='do you have cancer').pack()
    Radiobutton(frame, text='yes', variable=cancerpatient, value='yes').pack()
    Radiobutton(frame, text='no', variable=cancerpatient, value='no').pack() 

    dt1patient=StringVar()
    dt1patientdisply=Label(frame, text='do you have diabeties type1').pack()
    Radiobutton(frame, text='yes', variable=dt1patient, value='yes').pack()
    Radiobutton(frame, text='no', variable=dt1patient, value='no').pack()

    dt2patient=StringVar()
    dt2patientdiplay=Label(frame, text='do you have diabeteis type2').pack()
    Radiobutton(frame, text='yes', variable=dt2patient, value='yes').pack()
    Radiobutton(frame, text='no', variable=dt2patient, value='no').pack()

    CHFpatient=StringVar()
    CHFpatientdisplay=Label(frame, text='did you have a chronic stroke in the past few weeks or have them regularly').pack()
    Radiobutton(frame, text='yes', variable=CHFpatient, value='yes').pack()
    Radiobutton(frame, text='no', variable=CHFpatient, value='no').pack()

    kidneypatient=StringVar()
    kidneypatientdisplay=Label(frame, text='do you have kidney stones').pack()
    Radiobutton(frame, text='yes', variable=kidneypatient, value='yes').pack()
    Radiobutton(frame, text='no', variable=kidneypatient, value='no').pack()

    bonebreak=StringVar()
    bonebreakdisplay=Label(frame, text='where you in a accident in recent months').pack()
    Radiobutton(frame, text='yes', variable=bonebreak, value='yes').pack()
    Radiobutton(frame, text='no', variable=bonebreak, value='no').pack()
    continuebutton=Button(frame, text='continue', command=clear).pack()

    

    


loginbutton=Button(frame, text='login', command=login).pack()
signupbutton=Button(frame, text='sign up', command=signup).pack()


frame.mainloop() 