print("Now we'll calculate your marketing: \nPrices: \nTomato=3 NIS\nCucumber=2 NIS\nCola=5 NIS\nChicken=20 NIS\n ")
tomato=int(input("Enter how many tomato?"))
cucumber=int(input("Enter how many cucumber?"))
cola=int(input("Enter how many cola?"))
chicken=int(input("Enter how many chicken?"))
print("Summary of your order:\ntomato " + str(tomato) + "\ncucumber: " + str(cucumber) + "\ncola: " + str(cola) + "\nchicken: " + str(chicken))
'''
sum1=tomato*3
sum2=cucumber*2
sum3=cola*5
sum4=chicken*20
'''
summary=(tomato*3) + (cucumber*2) + (cola*5) + (chicken*20)
print("\nYou have to pay: " + str(summary) + " NIS without tax")
print("\nYou have to pay: " + str("%.2f" % (summary*1.17)) + " NIS with tax")