income = int(input("Welcome to Tax Calculator. What was your gross income last year?"))

def taxCalculator2000(number):
	y2000 = [0, 2650, 27850, 59900, 134200, 289950]
	rates2000 = [0, 0.15, 0.28, 0.31, 0.36, 0.396]
	income = number
	income = income - 9500
	under0 = income + 9500
	if income < 0:
		return 0

	#loopNum is the length of the list
	loopNum = 5
	#incat is the amount in a specific category of taxes
	incat = 0
	#total is the sum of taxes owed from all categories
	total = 0
	
	while income > 0:
		catergory = y2000[loopNum]
		if income > catergory:
			incat = (income - y2000[loopNum])
			#owed is taxes in the category
			owed = incat * rates2000[loopNum]
			income = income - incat
			loopNum = loopNum - 1
			total = total + owed
		else:
			loopNum = loopNum - 1

	return total

def taxCalculator2008(number):
	y2008 = [0, 8025, 32550, 78850, 164550, 357700]
	rates2008 = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35]
		
	income = number
	income = income - 9500
	under0 = income + 9500
	if income < 0:
		return 0
	
	#loopNum is the length of the list
	loopNum = 5
	#incat is the amount in a specific category of taxes
	incat = 0
	#total is the sum of taxes owed from all categories
	total = 0
	
	while income > 0:
		catergory = y2008[loopNum]
		if income > catergory:
			incat = (income - y2008[loopNum])
			owed = incat * rates2008[loopNum]
			income = income - incat
			loopNum = loopNum - 1
			total = total + owed
		else:
			loopNum = loopNum - 1

	return total

def taxCalculator2014(number):
	y2014 = [0, 8700, 35350, 85650, 178650, 388250]
	rates2014 = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35]
		
	income = number
	#remove this during the test 
	income = income - 9500
	under0 = income + 9500
	if income < 0:
		return 0
	
	#loopNum is the length of the list
	loopNum = 5
	#incat is the amount in a specific category of taxes
	incat = 0
	#total is the sum of taxes owed from all categories
	total = 0

	while income > 0:
		catergory = y2014[loopNum]
		if income > catergory:
			incat = (income - y2014[loopNum])
			owed = incat * rates2014[loopNum]
			income = income - incat
			loopNum = loopNum - 1
			total = total + owed
		else:
			loopNum = loopNum - 1
	return total
	
gross2000 = taxCalculator2000(income) / income 
gross2000 = gross2000 * 100
gross2000 = int(round(gross2000))
net2000 = income - taxCalculator2000(income)

gross2008 = taxCalculator2008(income) / income 
gross2008 = gross2008 * 100
gross2008 = int(round(gross2008))
net2008 = income - taxCalculator2008(income)

gross2014 = taxCalculator2014(income) / income 
gross2014 = gross2014 * 100
gross2014 = int(round(gross2014))
net2014 = income - taxCalculator2014(income)

#THE GREAT WALL OF PRINT STATEMENTS

print("Results for 2000 Plan.")
print("Taxes Owed: ${}".format(taxCalculator2000(income)))
print("Percent of Gross: {}%".format(gross2000))
print("Net Income: ${}".format((net2000)))

print()

print("Results for 2008 Plan.")
print("Taxes Owed: ${}".format(taxCalculator2008(income)))
print("Percent of Gross: {}%".format(gross2008))
print("Net Income: ${}".format((net2008)))

print()

print("Results for 2014 Plan.")
print("Taxes Owed: ${}".format(taxCalculator2014(income)))
print("Percent of Gross: {}%".format(gross2014))
print("Net Income: ${}".format((net2014)))