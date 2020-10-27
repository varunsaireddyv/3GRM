import pandas
import os
 print(os.curdir)
 print("please select the item id:\n")
df = pandas.read_csv("/home/sai/Desktop/FoodDataSet.csv", usecols = ['Menu_Item_ID','Item_Name','Food_Category'])
print(df)
a = input('enter your numbers')
