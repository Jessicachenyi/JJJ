def hello_world(name, age):
    print(f" {name} is {age} this year.")

hello_world("jess",27)  #order has to be the same order as shown in the "print" 

#discount= 0.9 putting here as global variables.
def wholesale(sale, shipment=50):  #this shipment can be given or not be given, it will still show in the output.
    global discount
    discount= 0.9 #putting here as local variables, but if we put global upper row, it will become global variables.
    return int(sale*discount + shipment) 
    print("wont show")
#print(f"the total amount is {wholesale(sale=1000)}.") will show 950,using the previus value
print(f"the total amount is {wholesale(sale=1000, shipment=80)}.")   
print(f"the current discount is {int(100-discount*100)}% off.")
#if here has a new shipment value, will use the new value instead of the previous one

#if discount=0.9 this is outside the def, both print will display. global variables 全域变数可以后面都可以拿来用
# if inside def, only will be used in the def. wont show the result of the second "print".  loca variables 只能用在函数内， 
#put is between def and return. local and also become global. 


def addition(x,y):
    return x + y
def subtrabtion(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    quotient = x // y
    remainder = x % y
    return quotient , remainder
print(division(10,3)[0]) # 0 and 1, the order of the value in the list. 取出商数
print(division(10,3)[1]) # 取出余数

while True:
    caltype =input("please enter caltype(1)+(2)-(3)*(4)/(or press any button to end):")
    if caltype in ("1", "2", "3", "4"):
        value1= int(input("please enter the fist number:"))
        value2= int(input("please enter the second number:"))
        if caltype == "1":
            print(f"{value1} + {value2} = {addition(value1, value2)}")
        elif caltype == "2":
            print(f"{value1} - {value2} = {subtrabtion(value1, value2)}")
        elif caltype == "3":
            print(f"{value1} * {value2} = {multiplication(value1, value2)}")
        elif caltype == "4":
            if value1 % value2 == 0:
                print(f"{value1} / {value2} = {division(value1, value2)[0]}")
            else:
                print(f"{value1} / {value2} = {division(value1, value2)[0]} and the remainder is {division(value1, value2)[1]}")
            #print(f"{value1}) + {value2} = {division(value1, value2)}")
    else:
        print("bye")
        break

