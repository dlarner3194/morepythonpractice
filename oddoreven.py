number_1 = int(raw_input("Please enter your number: "))
if number_1 % 2 == 0:
	print ("Your number is even.")
elif number_1 % 2 != 0:
	print ("Your number is odd")
else:
	print ("You must have not provided a number.")
if number_1 % 4 == 0:
	print("Your number is divisible by four.")