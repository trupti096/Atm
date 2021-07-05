print("Welcome! please insert your card")
print("Hi, please do not remove your chip card,Leave your card inserted during the entire transaction")
language=input("Please select language \n1-English \n2-Hindi:  ")
num=int(input("Enter any number between 10 and 99 for e.g.""25:  "))
if num>10 and num<99:
      print("Yes")
else:
      print("No")
pin=int(input("Please enter your 4 digit PIN number:  "))
if pin==1234:
    """if pin is correct then it will go to transaction other wise it will go on else condition.."""
    print (1234)
else:
	print("Wrong PIN!, Try Again")
print("PINGENERATION")
phonenumber=int(input("Enter your 10 digit phone number:  "))
if phonenumber==9876543210:
	print(9876543210)
else:
	print("Wrong Phone Number!, Try Again")
balance = 150000
print("\n1-Mini Statement \n2-Withdrawl \n3-Deposit \n4-Pin Change \n5-Exit")
option=int(input("Enter transaction:  "))
if(option==1):
	print("Your balance is:",balance)
elif(option==2):
	withdrawal=input("Select Account Type \n1-Kcc \n2-Current \n3-Savings:  ")
	withdraw=float(input("Enter amount to withdraw:  "))
	if withdraw>500 and withdraw<10000:
	 	total=balance - withdraw
	 	print("Success")
	 	print("Collect Cash")
	 	print("Available Balance:",total)
	else:
		print("Can not withdraw above 10000")
elif(option==3):
		deposit=float(input("Enter amount to deposit:  "))
		totalbalance=balance + deposit
		print("Success")
		print("Total balance now is:", totalbalance)
elif(option==4):
	    account=int(input("Enter your 15 digit account number:  "))
	    if account==123456789123456:
	    	 print(123456789123456)
	    else:
	    	print("Wrong account number!, Try Again")
	    pin=int(input("Please enter your recent pin:  "))
	    pin=int(input("Please enter your new pin:  "))
	    pin=int(input("Please re-enter your new pin:  "))
	    print("Your pin has been changed successfully")
elif(option==5):
		print("Closing the program...")
		exit()
		print("Your transaction is being processed.Please wait")
print("Transaction Complete")