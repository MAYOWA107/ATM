#This program is the continuation of atm project

import atm, sys
#Since i don't have the user balance with me. 
#I need to know his /her balance before any transaction.
balance = int(input("Enter your balance: "))
A = atm.ATM(balance)

a = 'y'
try:
    actual_pin = int(input("input the actual pin: "))
    A.greetings()    
except:
    print("ERROR has ocurred: Invalid input.")
    sys.exit()
actual_pin = str(actual_pin)
while a == 'y' or a == 'yes':
    select = int(input("Enter your option: "))
    if select == 2:
            another = 'y'
            while another == 'y' or another == 'yes':
                print("Please enter your Pin")
                try:
                    pin = int(input(": "))
                except:
                    print("Invalid input...")
                    sys.exit()
                pin = str(pin)
                if pin == actual_pin:
                    print("Please Select the desire service")
                    print('1. Quickletter\t\t 2. Withdrawal')
                    print('3. Payarena Bills')
                    print("5. Transfer\t\t 6.Airtime Topup")
                    print('7. Account opening\t\t 8. More Service')
                    print()
                    print("9. Cancel")
                    print("Enter your option")
                    try:
                        opt = int(input(":"))
                    except:
                        print("ERROR has occured.")
                        print("Please wait.....")
                        a = 'y'
                    if opt == 1:
                        print("Select group of payment.")
                        print("1. Cable\t\t 2. Airtime Topup")
                        print("3. Electricity\t\t 4. Transfer")
                        print()
                        try:
                            opt = int(input("Enter option: "))
                        except:
                            print("ERROR has occured: Invalid input.")
                            print("Please wait......")
                            a = 'y'
                            if opt == 1:
                                
                                    print("1. GOTV\t\t 2. DSTV")
                                    try:
                                        choice = int(input("Enter your choice"))
                                    except:
                                        print("ERROR has occured: Invalid input.")
                                        print("Please wait.......")
                                        a = 'y'
                                    if choice == 1:
                                        print("Select the payment company")
                                        print("1.GoTV Value\t\t 2. GOTV Max")
                                        print("3. GOTV Plus\t\t 4. GOTV Lite")
                                        print()
                                        print("Enter your choice")
                                        
                                        try:
                                            choice = int(input(":"))
                                        except:
                                            print("ERROR has occurred: Invalid input.")
                                            print("Please wait......")
                                            a = 'y'
                                        if choice == 1 or choice == 2 or choice ==3 or choice ==4:
                                            try:
                                                print("Please enter smart card number")
                                                card = int(input(":"))
                                            except:
                                                print("Invalid input.")
                                            card = str(card)   

                                            if len(card) > 11:
                                                print("ERROR OCCURRED: Invalid input.")
                                                print("Try again.....")
                                                a = 'y'
                                            elif len(card) == 11:
                                                print('Please confirm the number.', card)
                                                print("are you sure? Yes/No")
                                                ans = input(":").lower()
                                                if ans != 'yes':
                                                
                                                    a = 'y'


                                                else:
                                                    print("Enter amount")
                                                    amount = int(input(":"))
                                                    A.set_Quickteller_Bills(amount)
                                                    print("Subscribed succesfully.\nYou now have #", A.get_Quickteller())
                                                    a = 'y'
                                                
                                                    print("Please wait.......")
                                                    a = 'y'
                                        else: 
                                            
                                            print("ERROR OCCURED: Invalid input")
                                            print("Try again.....")
                                            a = 'y'
                                                    
                                    
                                    elif choice == 2:
                                        print("Select the payment company")
                                        print("1. DSTV Value\t\t 2. DSTV Max")
                                        print("3. DSTV Plus\t\t 4. DSTV Lite")
                                        print()
                                        print("Enter your choice")
                                        
                                        choice = int(input(":"))
                                        if choice!=1 or choice!=2 or choice!=3 or choice!= 4:
                                            print("ERROR OCCURED: Invalid input")
                                            print("Try again.....")
                                            a = 'y'
                                        if choice == 1 or choice == 2 or choice ==3 or choice ==4:
                                            try:
                                                print("Please enter smart card number")
                                                card = int(input(":"))
                                            except:
                                                print("Invalid input.")
                                            card = str(card)   

                                            if len(card) > 11:
                                                print("ERROR OCCURRED: Invalid input.")
                                                print("Try again.....")
                                                a = 'y'
                                            elif len(card) == 11:
                                                print('Please confirm the number.', card)
                                                print("are you sure? Yes/No")
                                                ans = input(":").lower()
                                                if ans != 'yes':
                                                
                                                    a = 'y'


                                            
                                                    print("Enter amount")
                                                    amount = int(input(":"))
                                                    A.set_Quickteller_Bills(amount)
                                                    print("You now have #", A.get_Quickteller())
                                                    a = 'y'
                                                else:
                                                    print("Please wait.......")
                                                    a = 'y'
                                    
                                    else:
                                        print("ERROR OCCURED: Invalid input.")
                                        print("Try again......")
                                        a = 'y'

                    
                        if opt !=1 or opt != 2 or opt!= 3 or opt != 4:
                            print("ERROR OCCURED: invalid input")
                            print("Try again.....")
                            a = 'yes'
                        
                        if opt == 2:
                            print("1. Glo topup\t\t 2. MTN topup")
                            print("3. Etisalat topup\t\t 4. Airtel topup")
                            print()
                            option = int(input("Enter your option: "))
                            
                            if option != 1 or option!= 2 or option!=3 or opt!= 4:
                                print("ERROR OCCURED: Please input valid number.")
                                print("Try again...")
                                a = 'y'
                            
                            if option == 1 or option == 2 or option == 3 or option == 4:

                                try:
                                    print("Please enter 11 digits. ")
                                    digit = int(input(":"))
                                except:
                                    print("ERROR has occured")
                                    a = 'y'
                                digit = str(digit)
                                if len(digit) >11:
                                    print("Number out of range. Invalid input.")
                                else:
                                    print("confirm the digit./You're sending it to ",digit)
                                    print('Press yes to confirm or no to decline.')
                                    ans = input(":").lower()
                                    if ans == 'yes':
                                        print("Please select amount you wish to pay.")
                                        print("1. 200\t\t 2. 500")
                                        print("2. 1000\t\t 3. 2000")
                                        print("5. others")
                                        opt = int(input("Enter your option"))
                                        if opt == 1:
                                            amount = 200
                                            A.Airtime_Top_up(amount)
                                            print("You now have #",A.get_Airtime_topup())
                                            a = 'y'
                                        if opt == 2:
                                            amount = 500
                                            A.Airtime_Top_up(amount)
                                            print("You now have #",A.get_Airtime_topup())
                                            a = 'y'

                                        if opt == 3:
                                            amount = 1000
                                            A.Airtime_Top_up(amount)
                                            print("You now have #",A.get_Airtime_topup())
                                            a = 'y'
                                        if opt == 4:
                                            amount = 2000
                                            A.Airtime_Top_up(amount)
                                            print("You now have #",A.get_Airtime_topup())
                                            a = 'y'
                                        if opt == 5:
                                            try:
                                                amount = int(input("Enter the amount: "))
                                                A.Airtime_Top_up(amount)
                                                print("You now have #",A.get_Airtime_topup())
                                                a = 'y'
                                            except:
                                                print("ERROR OCCURED: Invalid input.")
                                                a = 'y'

                        if opt == 3:
                            print("Select Payment company")
                            print("1. EKO Disco Postpaid\t\t 2. EKO Disco Prepaid")
                            print("3. IBADAN Disco postpaid \t\t 4. IBADAN Disco prepaid")
                            print("5. BENIN Disco pospaid\t\t 6. BENIN Disco Prepaid")
                            print()
                            ans = int(input("Enter your option:"))
                            if ans != 1 or ans!= 2 or ans!=3 or ans!=4 or ans !=5 or ans!= 6:
                                print("ERROR OCCURRED: Invalid input.")
                                a = 'y'
                            if ans == 1 or ans == 2 or ans == 3 or ans== 4 or ans == 5 or ans == 6:
                                print("Pls enter meter number")
                                try:
                                    num = int(input(":"))
                                    print("Make sure you confirm the meter number very well.")
                                    print("Are you sure the meter number is ", num)
                                except:
                                    print("ERROR OCCURECD: Invalid input.")
                                    a = 'y'
                    
                                ans = input("Enter yes to continue or any key to cancel").lower()
                                if ans == 'yes':
                                    print("Enter amount: ")
                                    amount = input(":")
                                    A.set_Quickteller_Bills(amount)
                                    print("You have the remaining balance",A.get_Quickteller())
                                    a = 'y'
                                else:
                                    print("Please wait.......")
                                    a = 'y'
                        if opt == 4:
                            print("Select the payment company")
                            print("1. ACCESS BANK\t\t 2. FIDELITY BANK")
                            print("3. FCMB\t\t 4. ZENITH BANK")
                            print("5. UNITY\t\t 6. ECO BANK")
                            opt = int(input("Enter your option"))
                            if opt != 1 or opt != 2 or opt != 3 or opt != 4 or opt != 5 or opt != 6:
                                print("ERROR OCCURED: Invalid input.")
                                print("Try again......")
                                a = 'y'

                            else:
                                if opt == 1 or opt == 2 or opt == 3 or opt == 4 or opt == 5 or opt == 6:
                                    print("please enter the account number")
                                try:
                                    acct_num = int(input(":"))
                                    print("are you sure you want to trasfer to this acct number", acct_num)
                                except:
                                    print("ERROR has occured.")
                                    print("Try again......")
                                    a = 'y'
                                    ans = input("Enter yes/no")
                                    if ans == 'yes':
                                        print("Enter amount you want to transfer")
                                    try:
                                        amount = int(input(":"))
                                        A.Transfer(amount)
                                        print("You now have #",A.get_Transfer())
                                        print("for another trasaction")
                                        a = 'y'
                                    except:
                                        print("Invalid amount.")
                                        print("Try again....")
                                        a = 'y'
                                        
                                else:
                                    print("Please wait.......")

                                    a = 'y'
                            

                    if opt == 2:
                            print("Please note that your 4th withdrawal and above within a month on the ")
                            print("Bank's ATMs will attract a surcharge fee of #35.00")
                            try:
                                print("Enter the amount you want to withdraw")
                                amount= int(input(":"))
                            except:
                                print("ERROR has occured. Invalid amount")
                                a = 'y'
                            print("Please wait.......")
                            A.Withdraw(amount)

                            print("withdraw succesful.\nYou now have #", A.get_Withdraw())
                            print("Do you want to perform another transaction?\nyes/no")
                            ans = input(":").lower()
                            if ans == 'yes':
                                a = 'y'
                            else:
                                print("Thanks for banking with us.")
                                
                                sys.exit()
                    


                                                        



                    if opt == 3:
                        print("Select group of payment.")
                        print("1. Cable\t\t 2. Airtime Topup")
                        print("3. Electricity\t\t 4. Transfer")
                        print()
                        try:
                            opt = int(input("Enter option: "))
                        except:
                            print("Invalid input.")
                            a = 'y'
                        if opt == 1:
                            print("1. GOTV\t\t 2. DSTV")
                            choice = int(input("Enter your choice"))
                            if choice == 1:
                                print("Select the payment company")
                                print("1.GoTV Value\t\t 2. GOTV Max")
                                print("3. GOTV Plus\t\t 4. GOTV Lite")
                                print()
                                print("Enter your choice")
                                choice = int(input(":"))
                                if choice == 1 or choice == 2 or choice ==3 or choice ==4:
                                    print("Please enter smart card number")
                                    card = int(input(":"))
                                    if card:
                                        print('Please confirm the number.')

                                        print("Enter amount")
                                        amount = int(input(":"))
                                        A.set_Quickteller_Bills(amount)
                                        print("You now have", A.get_Quickteller())
                                        print("Do you want to perform another transaction?\nyes/no")
                                        ans = input(":").lower()
                                        if ans == 'yes':
                                            a = 'y'
                                        else:
                                            print("Thanks for banking with us.")
                                
                                            sys.exit()
                    
                                else:
                                    print("Invalid input.")
                                    print("Do you want to perform another transaction?\nyes/no")
                                    ans = input(":").lower()
                                    if ans == 'yes':
                                        a = 'y'
                                    else:
                                        print("Thanks for banking with us.")
                                
                                        sys.exit()
                    

                            if choice == 2:
                                print("Select the payment company")
                                print("1. DSTV value\t\t 2. DSTV Max")
                                print("3. DSTV Plus\t\t 4. DSTV Lite")
                                print()
                                print("Enter your choice")
                                choice = int(input(":"))
                                if choice == 1 or choice == 2 or choice ==3 or choice ==4:
                                    try:
                                        print("Please enter smart card number")
                                        card = int(input(":"))
                                    except:
                                        print("Invalid number...")
                                        print("Please try again..")
                                        a = 'y'
                                    if card:
                                        print('Please confirm the number.')

                                        try:
                                            print("Enter amount")
                                            amount = int(input(":"))
                                        except:
                                            print("Invalid input...")
                                            print("Try again.....")
                                            a = 'y'
                                        A.set_Quickteller_Bills(amount)
                                        print("You now have", A.get_Quickteller())
                                        print("Do you want to perform another transaction?\nyes/no")
                                        ans = input(":").lower()
                                        if ans == 'yes':
                                            a = 'y'
                                        else:
                                            print("Thanks for banking with us.")
                                
                                            sys.exit()
                    
                                else:
                                    print("Invalid input.")
                                    print("Do you want to perform another transaction?\nyes/no")
                                    ans = input(":").lower()
                                    if ans == 'yes':
                                        a = 'y'
                                    else:
                                        print("Thanks for banking with us.")
                                
                                        sys.exit()
                    


                                
                        if opt!=1 or opt!= 2 or opt!=3 or opt!= 4:        
                            print("Invalid input...")
                            print("Please try again")
                            a = 'y'


                        if opt == 2:
                            print("1. Glo topup\t\t 2. MTN topup")
                            print("3. Etisalat topup\t\t 4. Airtel topup")
                            print()
                            try:
                                option = int(input("Enter your option: "))
                                if option == 1 or option == 2 or option == 3 or option == 4:
                                    
                                        print("Please enter 11 digits. ")
                                        digit = int(input(":"))
                                    
                                        print("Invalid digit....")
                                        print("Try again.....")
                                        a = 'y'
                                        digit = str(digit)
                                        if len(digit) >11 or len(digit)<11:
                                            print("Error occured.. Invalid number")
                                            a = 'y'
                                        else:
                                            print("confirm the digit./You're sending it to ",digit)
                                            print('Press yes to confirm or no to decline.')
                                            ans = input(":").lower()
                                            if ans == 'yes':
                                                print("Please select amount you wish to pay.")
                                                print("1. 200\t\t 2. 500")
                                                print("2. 1000\t\t 3. 2000")
                                                print("5. others")
                                                opt = int(input("Enter your option"))
                                                if opt == 1:
                                                    amount = 200
                                                    A.Airtime_Top_up(amount)
                                                    print("You now have #",A.get_Airtime_topup())
                                                    print("Do you want to perform another transaction?\nyes/no")
                                                    ans = input(":").lower()
                                                    if ans == 'yes':
                                                        a = 'y'
                                                    else:
                                                        print("Thanks for banking with us.")
                                    
                                                        sys.exit()
                        
                                                if opt == 2:
                                                    amount = 500
                                                    A.Airtime_Top_up(amount)
                                                    print("You now have #",A.get_Airtime_topup())
                                                    print("Do you want to perform another transaction?\nyes/no")
                                                    ans = input(":").lower()
                                                    if ans == 'yes':
                                                        a = 'y'
                                                    else:
                                                        print("Thanks for banking with us.")
                                        
                                                        sys.exit()
                            
                                                if opt == 3:
                                                    amount = 1000
                                                    A.Airtime_Top_up(amount)
                                                    print("You now have #",A.get_Airtime_topup())
                                                    print("Do you want to perform another transaction?\nyes/no")
                                                    ans = input(":").lower()
                                                    if ans == 'yes':
                                                        a = 'y'
                                                    else:
                                                        print("Thanks for banking with us.")
                                        
                                                        sys.exit()
                            
                                                if opt == 4:
                                                    amount = 2000
                                                    A.Airtime_Top_up(amount)
                                                    print("You now have #",A.get_Airtime_topup())
                                                    print("Do you want to perform another transaction?\nyes/no")
                                                    ans = input(":").lower()
                                                    if ans == 'yes':
                                                        a  = 'y'
                                                    else:
                                                        print("Thanks for banking with us.")
                                        
                                                        sys.exit()
                                                            
                                                if opt == 5:
                                                    
                                                    amount = int(input("Enter the actual amount: "))

                                                    A.Airtime_Top_up(amount)
                                                    print(Amount, 'has been withdrawn succesfully.')
                                                    print("You now have #",A.get_Airtime_topup())
                                                    print("Do you want to perform another transaction?\nyes/no")
                                                    ans = input(":").lower()
                                                    if ans == 'yes':
                                                        a = 'y'
                                                    else:
                                                        print("Thanks for banking with us.")
                                        
                                                        sys.exit()
                        
                            except:
                                print("Invalid input: Error occurred.")
                                a = 'y'

                        if opt == 3:
                            print("Select Payment company")
                            print("1. EKO Disco Postpaid\t\t 2. EKO Disco Prepaid")
                            print("3. IBADAN Disco postpaid \t\t 4. IBADAN Disco prepaid")
                            print("5. BENIN Disco pospaid\t\t 6. BENIN Disco Prepaid")
                            print()
                            try:
                                ans = int(input("Enter your option:"))
                            
                                print("Invalid response.")
                                print("Try again.....")
                                a = 'y'
                            
                                if ans == 1 or ans == 2 or ans == 3 or ans== 4 or ans == 5 or ans == 6:
                                    print("Pls enter meter number")
                                    num = int(input(":"))
                                    print("Make sure you confirm the meter number very well.")
                                    print("Are you sure the meter number is ", num)
                                    ans = input("yes or no").lower()
                                    if ans == 'yes':
                                        print("Enter amount: ")
                                        amount = input(":")
                                        A.set_Quickteller_Bills(amount)
                                        print("You have the remaining balance",A.get_Quickteller())
                                        print("Do you want to perform another transaction?\nyes/no")
                                        ans = input(":").lower()
                                        if ans == 'yes':
                                            a = 'y'
                                        else:
                                            print("Thanks for banking with us.")
                                    
                                            sys.exit()
                                else:
                                    print("Invalid input...")
                                    print("Please try again...")
                                    a = 'y'

                            except:
                                print("ERROR occured: invalid input.")
                                a = 'y'
                        if opt == 4:
                            print("Select the payment company")
                            print("1. ACCESS BANK\t\t 2. FIDELITY BANK")
                            print("3. FCMB\t\t 4. ZENITH BANK")
                            print("5. UNITY\t\t 6. ECO BANK")
                            try:
                                opt = int(input("Enter your option"))
                                
                                
                                if opt == 1 or opt == 2 or opt == 3 or opt == 4 or opt == 5 or opt == 6:
                                    print("please enter the account number")
                                    
                                    acct_num = int(input(":"))
                                    print("are you sure you want to trasfer to this acct number", acct_num)
                                
                                    
                                    ans = input("Enter yes/no")
                                    if ans == 'yes':
                                        print("Enter amount you want to transfer")
                                    
                                        amount = int(input(":"))
                                    
                                        
                                        A.Transfer(amount)
                                        print(amount,"withdraw succesfully.\nYou now have #",A.get_Transfer())
                                        print("for another trasaction")
                                        a = 'y'
                                    else:
                                        a = 'y'
                                else:
                                    print("sorry, invalid response.")
                                    a = 'y'
                            except:
                                print("Invalid input... ERROR occurred")
                                a = 'y'

                        #Withdraw            
                    if opt == 5:
                        print("Select the payment company")
                        print("1. ACCESS BANK\t\t 2. FIDELITY BANK")
                        print("3. FCMB\t\t 4. ZENITH BANK")
                        print("5. UNITY\t\t 6. ECO BANK")
                        
                        try:
                            opt = int(input("Enter your option"))
                            
                            if opt == 1 or opt == 2 or opt == 3 or opt == 4 or opt == 5 or opt == 6:
                                print("please enter the account number")
                                
                                acct_num = int(input(":"))
                                print("are you sure you want to trasfer to this acct number", acct_num)
                                ans = input("Enter 'y' for yes or any other key to cancel.").lower()
                                if ans == 'y':
                                    print("Enter amount you want to transfer")
                        
                                                        
                                    amount = int(input(":"))
                                    A.Transfer(amount)
                            
                                    print("Transfered succesfully.\nYou now have #",A.get_Transfer())
                                    print()
                                    print("for another transaction")
                                    a = 'y'

                                else:
                                    print("Cancelling.")
                                    print("Please wait.....")
                                    a = 'y'
                                    

                                    
                            else:
                                print("sorry, invalid response.")
                                a = 'y'
                                
                                    
                        except:
                            print("ERROR occured: invalid input.")
                            a = 'y'
                        #The Airtime topup
                                    
                    if opt == 6:
                            print("1. Glo topup\t\t 2. MTN topup")
                            print("3. Etisalat topup\t\t 4. Airtel topup")
                            print()
                            option = int(input("Enter your option: "))
                            if option == 1 or option == 2 or option == 3 or option == 4:
                                print("Please enter 11 digits. ")
                                digit = input(":")
                                print("confirm the digit./You're sending it to ",digit)
                                print('Press yes to confirm or no to decline.')
                                ans = input(":").lower()
                                if ans == 'yes':
                                    print("Please select amount you wish to pay.")
                                    print("1. 200\t\t 2. 500")
                                    print("2. 1000\t\t 3. 2000")
                                    print("5. others")
                                    opt = int(input("Enter your option"))
                                    if opt == 1:
                                        amount = 200
                                        A.Airtime_Top_up(amount)
                                        print("You now have #",A.get_Airtime_topup())
                                        print("Do you want to perform another transaction?\nyes/no")
                                        ans = input(":").lower()
                                        if ans == 'yes':
                                            a = 'y'
                                        else:
                                            print("Thanks for banking with us.")
                                
                                            sys.exit()
                    
                                    if opt == 2:
                                        amount = 500
                                        A.Airtime_Top_up(amount)
                                        print("You now have #",A.get_Airtime_topup())
                                        print("Do you want to perform another transaction?\nyes/no")
                                        ans = input(":").lower()
                                        if ans == 'yes':
                                            a = 'y'
                                        else:
                                            print("Thanks for banking with us.")
                                
                                            sys.exit()
                    
                                    if opt == 3:
                                        amount = 1000
                                        A.Airtime_Top_up(amount)
                                        print("You now have #",A.get_Airtime_topup())
                                        print("Do you want to perform another transaction?\nyes/no")
                                        ans = input(":").lower()
                                        if ans == 'yes':
                                            a = 'y'
                                        else:
                                            print("Thanks for banking with us.")
                                
                                            sys.exit()
                    
                                    if opt == 4:
                                        amount = 2000
                                        A.Airtime_Top_up(amount)
                                        print("You now have #",A.get_Airtime_topup())
                                        print("Do you want to perform another transaction?\nyes/no")
                                        ans = input(":").lower()
                                        if ans == 'yes':
                                            a = 'y'
                                        else:
                                            print("Thanks for banking with us.")
                                
                                            sys.exit()
                    
                                    if opt == 5:
                                        try:
                                            amount = int(input("Enter the amount: "))
                                        except:
                                            print("Invalid input... ERROR has occured.")
                                            print("Please wait........")
                                            a = 'y'
                                        A.Airtime_Top_up(amount)
                                        print("You now have #",A.get_Airtime_topup())
                                        print("Do you want to perform another transaction?\nyes/no")
                                        ans = input(":").lower()
                                        if ans == 'yes':
                                            a = 'y'
                                        else:
                                            print("Thanks for banking with us.")
                                
                                            sys.exit()
                            else:
                                print("ERROR occured: Invalid input.")
                                print("please wait........")
                                a = 'y'
                                
                    
                    
                    if opt == 8:
                        print("More service.")
                        print("1. Pin Change\t\t Pin Unblock")
                        print("3.Report Dispense Error\t\t 4. Open credit account")
                        print("5. Account opening")
                        print()
                        print("Enter your choice")
                        try:
                            choice = int(input(":"))
                        except:
                            print("Invalid input: ERROR has occured.")
                            print("please wait.........")
                            a = 'y'
                        if choice == 1:
                            print("Enter your pin")
                            pin = (input(":"))
                            if pin == actual_pin:
                                try:
                                    print("Please Enter new pin")
                                    new_pin = int(input(":"))
                                    print("Please Reenter new pin")
                                    new_pin2 = int(input(":"))
                                except:
                                    print("ERROR OCCURRED: Invalid pin.")
                                if new_pin == new_pin2:
                                    print("changed successfully")
                                    print("Do you want to perform another transaction?\nyes/no")
                                    ans = input(":").lower()
                                    if ans == 'yes':
                                        a = 'y'
                                    else:
                                        print("Thanks for banking with us.")
                                
                                        sys.exit()
                    
                                else:
                                    print("Sorry, Pin does not match")
                                    print()
                                    print("Do you want to perform another transaction?\nyes/no")
                                    ans = input(":").lower()
                                    if ans == 'yes':
                                        a = 'y'
                                    else:
                                        print("Thanks for banking with us.")
                                
                                        sys.exit()
                    

                            else:
                                print("ERROR: Invalid pin")
                                print()
                                print("Do you want to perform another transaction?\nyes/no")
                                ans = input(":").lower()
                                if ans == 'yes':
                                    a = 'y'
                                else:
                                    print("Thanks for banking with us.")
                                
                                    sys.exit()
                    
                                

                        if choice == 3:
                            print("Which card was used for the transaction you want to report")
                            print("1. Other bank\t\t 2. Access bank")
                            try:
                                card = int(input("Enter the bank"))
                            except:
                                print("ERROR has occured: Invalid input.")
                                print("please wait........")
                                a = 'y'
                            if card == 1:
                                print("Thanks for using this service")
                                print()
                                print("Kindly contact your bank to register this complaint.")
                                print("We will assist your bank with any information they may require to reverse your transaction.")
                                print()

                                print("Do you want to perform another transaction?\nyes/no")
                                ans = input(":").lower()
                                if ans == 'yes':
                                    a = 'y'
                                else:
                                    print("Thanks for banking with us.")
                                
                                    sys.exit()
                    



                        if choice ==4:
                            print("Application Error.")
                            print()
                            print("Do you want to perform another transaction?\nyes/no")
                            ans = input(":").lower()
                            if ans == 'yes':
                                a = 'y'
                            else:
                                print("Thanks for banking with us.")
                                
                                sys.exit()
                    

                        if choice == 5:
                            print("Instant savings account.")
                            print("Please enter your mobile number")
                            try:
                                num = int(input(":"))
                            except:
                                print("ERROR OCCURRED: Invalid input.")
                                print("Please wait......")
                                a = 'y'
                            if num:
                                print("Enter your bvn number.")
                                try:
                                    bvn = int(input(":"))
                                except:
                                    print("ERROR OCCURED: Invalid input.")
                                    print("Please wait........")
                                    a = 'y'
                                print("Confirm the details")
                                print("Phone number: ",num)
                                print("Account type: Savings")
                                print("BVN: ",bvn)
                                print("Acount created succesfully.")
                                print()
                                print("Do you want to perform another transaction?\nyes/no")
                                ans = input(":").lower()
                                if ans == 'yes':
                                    a = 'y'
                                else:
                                    print("Thanks for banking with us.")
                                
                                    sys.exit()

                        a = 'yes'


                else:
                    print("Invalid pin: Pin is not match.")

    
    elif select >5 or select<0:
        print("ERROR: Invalid input.")
        a = 'yes'


    elif select == 5:
        print("Thanks for banking with us.")
        sys.exit()

    else:
        print("Language not available.")
        print("Would you like to continue? Yes/No")
        ans = input(":").lower()
        if ans == 'yes':
            a= 'y'
        else:
            a = 'n'