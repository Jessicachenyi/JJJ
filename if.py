#boolean(bool)
steak = 500
pork = 600
fish_steak = 400
menu = 80
#print ( not steak == pork)
#print (steak > pork and pork < fish_steak)
#if steak > pork:
#    print ("steak is more expensive than pork")
#else:
#    print ("pork is more expensive than steak")

#order = input ("which one do you want to order? (A) steak (B) pork:").upper()
#if order == "A":
#    print (f"the price for the steak is {steak}")
#else:
#    print (f"the price for the pork is {pork}")

order = input ("which one do you want to order? (A) steak (B) pork:").upper()
upgrade = input ("would you like an upgrade for a menu set? (Y)yes (N)no:").upper()
#if order == "A":
#    if upgrade == "Y":
#        print (f"the price for the steak is ${steak+ menu}")
#    else:
#        print (f"the price for the steak is $ {steak}")
    
#else:
#    if upgrade == "Y":
#        print (f"the price for the steak is ${pork+ menu}")
#    else:
#        print (f"the price for the steak is $ {pork}")

if order == "A" and upgrade == "Y":
    print ( f" your order is {steak + menu }.")
elif order == "A" and upgrade =="N":
    print (f"the price for the steak is ${steak}")
elif order == "B" and upgrade =="Y":
    print (f"the price for the pork is ${pork + menu}")  
else:
    print (f"your order price is ${pork}.")


