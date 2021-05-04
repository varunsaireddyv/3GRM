import pandas
import os
import sqlite3
LoginSignupQuestion=input('will you login, signup or use incognito :')

if LoginSignupQuestion == 'sign up':
    first_name=input('please enter your first name ')
    last_name=input('please enter your last name ')
    age=input('please enter your age ')
    mail=input('please enter your mail id ')

    connection = sqlite3.connect('/home/rajesh/Desktop/3grmvarun/3GRM/Programming/diet/DietDatabase.db')
    cursor= connection.cursor()
    cursor.execute("INSERT INTO UserDataDiet VALUES (:first, :last, :age, :mail)", {'first': first_name, 'last': last_name, 'age': age, 'mail': mail})

    print('your sign up has been completed please awnser this questions in order to customize your menu')
    cancerpatient=input('do you have cancer yes or no :')
    dt1patient=input('do you have diabeties type 1 yes or no :')
    dt2patient=input('do you have diabeties type 2 yes or no :')
    CHFpatient=input('do you have chronic heart stroks yes or no :')
    kidneypatient=input('do you have kidney stones or kidney disease yes or no :')
    bonebreak=input('did you break your bones recently in a accident yes or no :')
    cursor.execute("INSERT INTO UserDataDiseseas VALUES (:cancer, :dt1, :dt2, :chf, :kidney, :bonebreak, :mail)", {'cancer': cancerpatient, 'dt1': dt1patient, 'dt2': dt2patient, 'chf': CHFpatient, 'kidney': kidneypatient, 'bonebreak': bonebreak, 'mail': mail})
    connection.commit()
if LoginSignupQuestion == 'login':
    loginemail=input('use your email to login :' )
    loginquery='SELECT * FROM UserDataDiseseas WHERE mail=%s'
    cursor.execute(loginquery, loginemail)
    



else:
    orders=[]
    df = pandas.read_csv("/home/rajesh/Desktop/3grmvarun/3GRM/Programming/diet/FoodDataSet.csv")
    print((orders))
    catageries = df["Food_Category"].unique()
    print((catageries[0]))

    a=1
    while a == 1 :
        x=1
        for i in catageries :
            print(x, i)
            x=x+1
        CatIndex = input("please select the id: ")

        if CatIndex == 'exit' :
            break
        else :
            Bool_Items=df["Food_Category"]==catageries[int(CatIndex)-1]
            Items=df[Bool_Items]
            y=1
            for i in Items['Item_Name'] :
                print(y, i)
                y=y+1
            Item_index=input("please select the item id:\n")
            orders.append(Items.iloc[int(Item_index)-1, :])
    Total_Calories=0
    for order in orders:
        print(order[12])
        Total_Calories=Total_Calories + order[12]
    print('this is the total amount of calories: ' , Total_Calories)
    if Total_Calories in range(500,700):
        print('you have have had had a healthy amount of calories for a meal ')
    elif Total_Calories<500 :

        print(str(500-Total_Calories) + ' calories to be added to the next meal')
        
    else :
        CaloriesOverflowQuestion=input('there are bit too much of calories in your diet  do you want to romve a few items?  :')
        if CaloriesOverflowQuestion == 'yes' :
            FoodCalorieFinder=Total_Calories-700
            def closest(order, FoodCalorieFinder): 
        
                return order[min(range(len(order)), key = lambda i: abs(order[i]-FoodCalorieFinder))] 
            print(closest(order, FoodCalorieFinder)) 


        Difference_Adder=Total_Calories - 666
        print(str(Difference_Adder) + ' calories above the required amount for a meal')
