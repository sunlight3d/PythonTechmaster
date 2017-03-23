import matplotlib.pyplot as pyplot

# x1Values = [1,3,5,7,9]
# y1Values = [4,5,8,7,12]
# pyplot.bar(x1Values, y1Values,width=0.2, label="This is bar1", color="red")
#
# x2Values = [2,4,6,8,10]
# y2Values = [2,3,4,5,10]
# pyplot.bar(x2Values, y2Values,width=0.2, label="This is bar2", color="blue")
#
# pyplot.xlabel("X Axis")
# pyplot.ylabel("Y Axis")
# pyplot.title("Bar chart example\nHope you enjoy!")
# pyplot.legend()
# pyplot.show()

mobileBranches = ["Apple", "Samsung", "Nokia", "Blackberry"]
slices = [30, 30, 20, 20]
colors = ["red", "blue", "yellow", "purple"]
explode = [0.1, 0, 0, 0]
pyplot.pie(slices,
           labels=mobileBranches,
           colors=colors,
           startangle=0,
           explode=explode,
           autopct="%1.1f%%"
            )
pyplot.title("This is a pie chart\nHope you like !")
pyplot.show()
