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
FileNameWidget=Label(root, text='step 1: file name')
FileNameWidgetDisplay=Label(root, text='dummy text')
#add target column here
TargetColumnWidget=Label(root, text='step 2: target column')
TargetColumnWidgetDisplay=Label(root, text='dummy text')

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
FileNameWidget.grid(row=0, column=0)
FileNameWidgetDisplay.grid(row=0, column=1)
importfile.grid(row=0, column=2)

TargetColumnWidget.grid(row=1, column=0)
TargetColumnWidgetDisplay.grid(row=1, column=1)
action_resultFoundorNOTfound.grid(row=1, column=3)
importtarget.grid(row=1, column=2)

step_3.grid(row=2, column=0)

step_3_reggression.grid(row=3, column=0)
step_3_trainbutton.grid(row=3, column=1)
networktrained_3rdstep.grid(row=3,column=2)


step_3_pickle.grid(row=4, column=0)
step_3_runbutton.grid(row=4, column=1)
savedmodeltodisk_3rdstep.grid(row=4, column=2)

step_4.grid(row=5, column=0)
step_4_classifier.grid(row=6,column=0)
step_4_trainbutton.grid(row=6, column=1)
step_4_runbutton.grid(row=7, column=1)
networktained_4thstep.grid(row=6, column=2)
savedmodeltodisk_4thstep.grid(row=7, column=2)
placeholder.grid(row=7, column=0)


root.mainloop()