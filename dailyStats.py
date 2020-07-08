import matplotlib.pyplot as plt 
import pandas as pd 

myData = pd.read_excel("./DailyStuffs.xlsx", "daily", index_col=None, na_values=['NA'])

print(myData.head())

print("\n")

print(print(myData.describe()))

fig_1 = plt.figure("1st Figure", figsize=(14.4, 8.8)) #custom figure
chart_1 = fig_1.add_subplot(221) #1st chart , 121 = grid position
chart_2 = fig_1.add_subplot(222)  #2nd chart
chart_3 = fig_1.add_subplot(223)
chart_4 = fig_1.add_subplot(224)


chart_1.bar(myData["Date"], myData["Coding"], label="Coding", color = 'g')

chart_2.bar(myData["Date"], myData["Gaming"], label="Gaming", color = 'c')
chart_3.bar(myData["Date"], myData["Learning"], label="Learning(Videos etc)", color = 'r')
chart_4.bar(myData["Date"], myData["Others(Movies, Series)"], label="Entertainment", color = 'y')

plt.xlabel("Date")
plt.ylabel("Miniutes Spent")



fig_1.legend()
plt.show()

input("Press Any Key to Exit.....")
