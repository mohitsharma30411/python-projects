'''Assignment 4: ATM Eligibility
Check whether a customer can withdraw money.
Requirements:
• Validate PIN.
• Check account balance.
• Display meaningful messages.
'''

def info_collect():
    balance=int(input("Enter Opening Amount: "))
    while True:
        pin=input("Enter 6 digit Pin to set: ")
        if len(pin)==6 and pin.isdigit():
            return balance,pin
        else:
            print('wrong selection! Enter PIN Again!')


def balance_check(balance,pin):

    print("Let's confirm the PIN of ATM for Transaction")
    for i in range(3):
        print(f"{i}/3 attempt\n")
        pin_ver=input("Enter your 6 digit Pin: ")
        
        if pin_ver==pin:
            print("Your Pin is correct! Lets Continue:\n")   
            break                     
        else:
            print('Your pin is incorrect\n')
    else:
        print('Reach Threshold of the day! account block for 24 Hrs\n')
        return
        
    while True:    
        print("Please Enter Number as per Choice\n\n Press 1 for Balance Check\n Press 2 Withdraw\n Press 3 Pin Change\n Press 4 for exit\n")
        choice=int(input("Enter your Choice: "))
        if choice==1:
            print(f"Available Balance : {balance}\n")
        elif choice==2:       
            withdraw=int(input("Enter amnount to Withdraw: "))
            if withdraw>balance:
                print(f"Insufficent Amount to withdraw")
            else:
                print('Withdraw is successfull')
                print('Please collect your money')
                balance-=withdraw
                print(f"Remaining Balance: {balance}")
        elif choice==3:
            check_pin=input("Enter Old Pin: ")
            if check_pin==pin:
                new_pin=input("Enter New 6 digit Pin: ")
                if len(new_pin)==6 and new_pin.isdigit():
                    pin=new_pin
                    print("Your Pin Changed successfully")
                    
            else:
                print("Your Pin is inccorrect")
        elif choice==4:
            print("You choose to Exit! Thank for your Visit")
            break
                                    
def info_show():
    
    bal,pin=info_collect()
    
    balance_check(bal,pin)
    
info_show()