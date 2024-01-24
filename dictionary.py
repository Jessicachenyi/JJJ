mobile1 = {
      "brand" : "apple",   # brand is key apple is value
      "series" : "iphone 14 pro",
      "capacity" : "512GB",
      "color" : "purple"
}

mobile2 = {
      "brand" : "xiaomi",   # brand is key apple is value
      "series" : "mi 10",
      "capacity" : "256GB",
      "color" : "black"
}

mobile3 = {
      "brand" : "blackberry",   # brand is key apple is value
      "series" : "model 2",
      "capacity" : "128GB",
      "color" : "blue"
}
#print(mobile["series"])
#print(mobile.get("color", "no info found.")) #.get is to search for some unknow info. can also use if else to do this.
#if "series" in mobile:
#    print(mobile["series"])
#else:
#    print("no info found")

#mobile["capacity"] = "256GB" , to modify
#print(mobile)

#mobile.popitem() clear the last item, .pop is to clearn the item typed in the ()
#print(mobile)

#mobile.clear() # clear all
#print(mobile)

#for list in mobile.keys(): 
#    print(list)

#for list in mobile.values():
#    print(list)

#for list in mobile.items():
#    print(list)

#for title, format in mobile.items():
#    print(f"The {title} is {format}.")

#inventory = [mobile1, mobile2, mobile3]
#print(inventory[2]["series"])

#inventory = [mobile1, mobile2, mobile3]
##search = input("please enter the brand name you want to search:")
#if search in str(inventory):
#    print("there are in stock")
#else:
#    print(f"no items available.") 

inventory = [mobile1, mobile2, mobile3]
search = input("please enter the brand name you want to search:")
if search in str(inventory):
    for mobile in inventory:
        if mobile["brand"] == search:
            print(f"currently we have {mobile['color']} in stock. It is {mobile['series']}, with capacity of {mobile['capacity']}.")
else:
    print(f"no {search} available.") 