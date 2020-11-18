import os
while True:
    try:  
        cmdtxt = 'start ' + input('which app do you want to use: ')
        os.system(cmdtxt)
        break
        
    except:
        print('no such application on this device')
       
     
   
