from tkinter import *
from tkinter import filedialog


#button faunctionalitty
def fileopener():
    root.filename=filedialog.askopenfile(initialdir='\home', title='select file to import', 
    filetypes=(('csv files', '*.csv'), ('all files', '*.*')))
def train():
    networktrained_3rdstep.config(text='training brain for simulation.....')
def run():
    savedmodeltodisk_3rdstep.config(text='running simulation of brain....')    


root= Tk()
# add file text in this line
networktained_4thsteptextbox=Text(root, height=1, width=20)
networktrained_3rdsteptextbox=Text(root, height=1, width=20)
savedmodeltodisk_3rdsteptextbox=Text(root, height=1, width=20)
savedmodeltodisk_4thsteptextbox=Text(root, height=1, width=20)
targetcolumnstatus=Text(root, height=1, width=20)
filestatustextbox=Text(root, height=1, width=20)
filenametextbox=Text(root, height=1, width=20)


networktained_4thsteptextbox.insert(END, 'dummy text')
networktrained_3rdsteptextbox.insert(END, 'dummy text')
savedmodeltodisk_3rdsteptextbox.insert(END, 'dummy text')
savedmodeltodisk_4thsteptextbox.insert(END, 'dummy text')
targetcolumnstatus.insert(END, 'dummy text')
filestatustextbox.insert(END, 'dummy text')
filenametextbox.insert(END, 'dummy text')
targetcolumntextbox=Text(root, height=1, width=20)
FileNameWidget=Label(root, text='step 1: file name', justify=LEFT, anchor="w")
FileNameWidgetDisplay=Label(root, text='dummy text', justify=LEFT, anchor="w")
targetcolumntextbox.insert(END, 'dummy text')
#add target column here
TargetColumnWidget=Label(root, text='step 2: target column')
TargetColumnWidgetDisplay=Label(root, text='test text')

step_3=Label(root, text='step 3: Neural Network Regresser')
step_3_reggression=Label(root, text='Regression')
step_3_pickle=Label(root, text='Pickle')

step_3_trainbutton=Button(root, text='Train', command=train)
step_3_runbutton=Button(root, text='Run', command=run)

step_4=Label(root, text='step 4: Neurel Network Classifier')
step_4_classifier=Label(root, text='Classifier')

step_4_trainbutton=Button(root, text='Train')
step_4_runbutton=Button(root, text='Run')
#place holders
placeholder=Label(root, text='')

#action results

networktrained_3rdstep=Label(root, text='dummy text')
savedmodeltodisk_3rdstep=Label(root, text='dummy text')
networktained_4thstep=Label(root, text='dummy text')
savedmodeltodisk_4thstep=Label(root, text='dummy text')
action_resultFoundorNOTfound=Label(root, text='dummy text')


#import buttons
importfile=Button(root, text='import file', command=fileopener)
importtarget=Button(root, text='import target')



#placement
filestatustextbox.grid(row=0, column=3)
targetcolumnstatus.grid(row=1, column=3)
filenametextbox.grid(row=0, column=1)
targetcolumntextbox.grid(row=1, column=1)
step_3.grid(row=2, column=0)

step_3_reggression.grid(row=3, column=0)
step_3_trainbutton.grid(row=3, column=1)
networktrained_3rdsteptextbox.grid(row=3,column=2)


step_3_pickle.grid(row=4, column=0)
step_3_runbutton.grid(row=4, column=1)
savedmodeltodisk_3rdsteptextbox.grid(row=4, column=2)

step_4.grid(row=5, column=0)
step_4_classifier.grid(row=6,column=0)
step_4_trainbutton.grid(row=6, column=1)
step_4_runbutton.grid(row=7, column=1)
networktained_4thsteptextbox.grid(row=6, column=2)
savedmodeltodisk_4thsteptextbox.grid(row=7, column=2)
placeholder.grid(row=7, column=0)



FileNameWidget.grid(sticky = W, column=0,row=0)

importfile.grid(row=0, column=2)

TargetColumnWidget.grid(sticky = W, row=1, column=0)


importtarget.grid(row=1, column=2)




root.mainloop()