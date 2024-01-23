breakfast = ["egg", "sandwiches", "burger", "sausages"]
beverages = ["soyomilk", "blacktea", "milktea"]
amount = 0
for order in breakfast:
    for drinks in beverages:
    #print(order)
    #if order == "burger":
       # break, to stop from the chosen one
        #continue to skip the one chosen
        print(f"{order} with {drinks}")
        amount += 1
    print (f"In total there are {amount} menu sets.")

numbers = [1,2,3,4,5,6,-1,-2,-3]
list = []
grade = 1
positive = []
negative = []
for number in numbers :
    #if number > 3:
    if number > 0:
        positive .append(number)
    else:
        negative .append(number)
        #list .append(number)
    grade *= number
print(grade)
print(list)
print(f"positive numbers are {positive}.")
print(f"negitive numbers are {negative}.")

for x in range (5, 10, 2): # output is 5,7,9.
    print(x)

