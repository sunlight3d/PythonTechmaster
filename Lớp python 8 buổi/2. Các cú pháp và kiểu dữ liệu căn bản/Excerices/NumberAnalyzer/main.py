from pprint import pprint

numbers = [1,3,5,7,10,20,6,8, 9, 12, 14, 13, 17]
sum = 0
for number in numbers:
    sum = sum + number
print("sum = "+str(sum))
print("average = "+str(sum /len(numbers)))

numberOfOverAverage = 0
for number in numbers:
    if number > sum /len(numbers):
        numberOfOverAverage = numberOfOverAverage + 1
print("Number of elements above average = "+str(numberOfOverAverage))

