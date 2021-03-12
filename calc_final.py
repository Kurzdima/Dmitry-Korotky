input_str = input("Write please, what do you need to calculate ___  ")

P1 = 0
operation = "+"
pravilno = False
str_a = ""

for letter in input_str:
	if letter in "0123456789":
		pravilno = True
	if letter in "+-/*^" and pravilno:
		P2 = float(str_a)
		if operation == '/':
			if P2 == 0:
				P1 = "Inf"
			else:
				P1 = P1 / P2
		elif operation == "+":
			P1 = P1 + P2
		elif operation == "*":
			P1 = P1 * P2
		elif operation == "-":
			P1 = P1 - P2
		elif operation == "^":
			P1 = P1 ** P2
		else:
			P1 = None
		operation = letter
		pravilno = False
		str_a = ""
	else:
		str_a += letter

P2 = float(str_a)
if operation == '/':
	if P2 == 0:
		P1 = "Inf"
	else:
		P1 = P1 / P2
elif operation == "+":
	P1 = P1 + P2
elif operation == "*":
	P1 = P1 * P2	
elif operation == "-":
	P1 = P1 - P2	
elif operation == "^":
	P1 = P1 ** P2
else:
	P1 = None
		
print("Resault of calculate: " + str(P1))