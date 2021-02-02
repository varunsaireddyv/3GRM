import pandas
import os

orders=[]
df = pandas.read_csv("/home/sai/Desktop/FoodDataSet.csv")
print(type(orders))
catageries = df["Food_Category"].unique()
print(type(catageries[0]))

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
    FoodCalorieFinder=Total_Calories-700
    CaloriesOverflowQuestion=input('there are bit too much of calories in your diet  do you want to remove a few items?  :')
    if CaloriesOverflowQuestion == 'yes' :
        for o in orders :
            if o.Calories in range(0, FoodCalorieFinder):
                print(o.Item_Name)
    else:
        WeightForEquation=input('then you have to exersize to burn those extra calories give me your weight and ill give you the amount of time to exersize ')
        PreferenceQuestion=input('would you prefer cyclyng or walking  :' )
        if PreferenceQuestion == 'walking':
            Walking_Equetion=2.9*3.5*float(WeightForEquation)/200
            CaloriesToBurn_float=Walking_Equetion/FoodCalorieFinder
            CaloriesToBurn_int=int(CaloriesToBurn_float)
            HoursToBurnCalories=CaloriesToBurn_int/60
            print('you have to walk for ' + str(HoursToBurnCalories) + ' hours to burn the exsese calories')


    # print(str(Difference_Adder) + ' calories above the required amount for a meal')
