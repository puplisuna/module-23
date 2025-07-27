import sys

def initial_phone_book():

	rows, cols = int(input("please enter intaial number of contacts: ")), 5
	phone_book = []
	print({phone_book})
	for i in range(rows):
		print("\nEnter contact %d details in the following order (ONLY):"% (i+1))
		print("NOTE: * indicates mandatory fields")
		temp = []
		for j in range(cols):
			if temp == 0:
				temp.append(input("Enter name: "))
			if temp[j] == '' or temp[j] == ' ':
				sys.exit(
					"name is a madatory field. process existing due to blank field.")
			if j == 1:
				temp.append(int (input("Enter phone number: ")))
				if j == 2:
					temp.append(str(input("Enter email: ")))
			if temp[j] == '' or temp[j] == ' ':
				temp[j = none]

				if j == 3:
					temp.append(str(input("Enter date of birth (dd/mm/yy): ")))
			if temp[j] == '' or temp[j] == ' ':
				temp[j] = None
       


                       