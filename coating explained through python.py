#Coating as explained through python coding

print("So you're coating today, that must suck!")
answer=input("Are you coating today? Type 1:for yes, Type 2 for no.")
answer = int(answer)
if answer == 1:
    print("That sucks, but lets have some fun!")
else:
    print("Well, lucky you, go make some batches!")

#insert something here regarding checking brix, insert looop once figured out
print("What number is your brix?")
brix=input("Insert the number of the brix here:")
brix=int(brix)
if brix == 70 or brix ==71 or brix == 72:
    print("You can coat!")
elif brix > 72:
    print("Add some water in because that is too damn high!")
#insert something like of a menu to choose things here     
print("Lets find our your target weight")
CW=input("What is your starting core weight?")
CW = float(CW)
print("okay, cool so...")

#Enter here to find Final weight
TP=input("Enter total percentage coated here: ")
TP=float(TP)
if TP == 1.00:
    core_weight = input("insert CW from above")
    core_weight = float(core_weight)
    print(TP, "*.39", "+", core_weight, "=",TP *.39 + core_weight)
    print("This is your final weight and you are done!")
elif TP < 0.70:
    core_weight=input("insert CW from above")
    core_weight = float(core_weight)
    print(TP, "*.39", "+", core_weight, "=", TP *.39 + core_weight)
    print("You're not quite there yet!")
elif TP == 0.70 or TP == 0.80 or TP == 0.90:
    core_weight=input("insert CW from above")
    core_weight = float(core_weight)
    print(TP, "*.39", "+", core_weight, "=", TP *.39 + core_weight)
    print("Add flavor in")
elif TP ==0.25:
    core_weight=input("insert CW from above")
    core_weight=float(core_weight)
    print(TP, "*.39", "+", core_weight, "=", TP *.39 + core_weight)
    print("Add sweeteners in and stop adding powder.")
elif  TP < 0.25:
    core_weight=input("insert CW from above")
    core_weight=float(core_weight)
    print(TP, "*.39", "+", core_weight, "=", TP *.39 + core_weight)
    print("Add solution and add powder to stop it from sticking!")



    
    


