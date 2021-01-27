import pandas
import os

orders=[]
df = pandas.read_csv("\\Users\\Harshitha\\Desktop\\varun\\3GRM\\Programming\\diet\\FoodDataSet.csv")
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
    # CaloriesOverflowQuestion=input('there are bit too much of calories in your diet  do you want to romve a few items?  :')
    # if CaloriesOverflowQuestion == 'yes' :
    #     FoodCalorieFinder=Total_Calories-700
    #     def closest(order, FoodCalorieFinder): 
      
    #         return order[min(range(len(order)), key = lambda i: abs(order[i]-FoodCalorieFinder))] 
    #     print(closest(order, FoodCalorieFinder)) 


    Difference_Adder=Total_Calories - 666
    print(str(Difference_Adder) + ' calories above the required amount for a meal')
    
