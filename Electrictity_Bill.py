'''Create an electricity billing system.
Requirements:
• Use slab-based billing with if-elif-else.
• Validate negative input.
• Print total amount.
'''

def info_in(n):
    cust_name=input(f"Enter Customer Name{n}: ")
    cust_ID=input(f"Enter Customer ID BSES-Del{n}: ")
    Cust_M_No=input(f'Enter Meter No BSES-Del Met-No{n}: ')
    Cust_last=int(input("Enter the last Meter reading: "))
    Cust_Curr=int(input("Enter the Current Meter reading: "))
    
    return cust_name,cust_ID,Cust_M_No,Cust_Curr,Cust_last
    
def dispCustBillInfo(cust_name,cust_ID,Cust_M_NO):
    print("*"*80)
    print(f"The name of Customer :{cust_name}")
    print(f"The ID of Customer :{cust_ID}")
    print(f"The Meter No of Customer :{Cust_M_NO}")

def custBillAmount(Cust_last,Cust_Curr):
    total_amt=[]
    
    if Cust_Curr<Cust_last:
        print("Invalid Meter Reading")
        
    if Cust_Curr==Cust_last:
        print ("No payment is required")
    
    Total_unit=Cust_Curr-Cust_last
    u1=u2=u3=u4=u5=0
    amt1=amt2=amt3=amt4=amt5=0
                    
    if Total_unit>300:
        u1=Total_unit-300
        amt1=u1*8
        Total_unit-=u1
        total_amt.append(amt1)
        # print(f"Unit {u1} and Amount {amt1} Remaining {Total_unit}")
            
    if Total_unit>=250:
        u2=Total_unit-250
        amt2=u2*6
        Total_unit-=u2
        total_amt.append(amt2)
        # print(f"Unit{u2} and Amount{amt2} Remaining {Total_unit}")
            
    if Total_unit>=200:
        u3=Total_unit-200
        amt3=u3*4.5
        Total_unit-=u3
        total_amt.append(amt3)        
        # print(f"Unit{u3} and Amount{amt3} Remaining {Total_unit}")
            
    if Total_unit>=100:
        u4=Total_unit-100
        amt4=u4*3.5
        Total_unit-=u4
        total_amt.append(amt4)
        # print(f"Unit{u4} and Amount{amt4} Remaining {Total_unit}")
            
    if Total_unit>=0:
        u5=Total_unit-0
        amt5=u5*2
        Total_unit-=u5
        total_amt.append(amt5)
        # print(f"Unit{u5} and Amount{amt5} Remaining {Total_unit}")
        
    print("*"*60)
    print("Electricity Bill Calculation".center(60))
    print("*"*60)
    print(f'{"slabs":<15}{"Units":<15}{"Rate":<15}{"Amount":<15}')
    
    print(f'{"0-99":<15}{u5:<15}{2:<15}{amt5:<15}')
    print(f'{"100-199":<15}{u4:<15}{3.5:<15}{amt4:<15}')
    print(f'{"200-249":<15}{u3:<15}{4.5:<15}{amt3:<15}')
    print(f'{"250-299":<15}{u2:<15}{6:<15}{amt2:<15}')
    print(f'{"300 & Beyond":<15}{u1:<15}{8:<15}{amt1:<15}')
    print()

    
    
    
    return sum(total_amt)    
    

'''print("*"*50)
print("Electicity Slab System".center(50))
print("*"*50)

print(f"{"0-99":<25}{"2/unit":<15}")
print(f"{"100-199":<25}{"3.5/Unit":<15}")
print(f"{"200-249":<25}{"4.5/unit":<15}")
print(f"{"250-299":<25}{"6/unit":<15}")
print(f"{"300 above":<25}{"8/unit":<15}")

print('\n\n Alternative 2: Using Tabs (tab)')

print("*"*50)
print("Electicity Slab System".center(50))
print("*"*50)
print("Units\t\tRate")
print("0-99\t\t2/unit")
print("100-199\t\t3.5/unit")
print("200-249\t\t4.5/unit")

print('\n\n Alternative 3 : Using .format() (Very Common)\n')
print("*" * 50)
print("{:^50}".format("Electricity Slab System"))
print("*" * 50)

print("{:<25}{:<15}".format("0-99", "2/unit"))
print("{:<25}{:<15}".format("100-199", "3.5/unit"))
print("{:<25}{:<15}".format("200-249", "4.5/unit"))
print("{:<25}{:<15}".format("250-299", "6/unit"))
print("{:<25}{:<15}".format("300 above", "8/unit"))

print('\n\n Alternative 4 : Using ljust(), rjust(), and center()\n')
print("*" * 50)
print("Electricity Slab System".center(50))
print("*" * 50)

print("0-99".ljust(25) + "2/unit".ljust(15))
print("100-199".ljust(25) + "3.5/unit".ljust(15))
print("200-249".ljust(25) + "4.5/unit".ljust(15))
print("250-299".ljust(25) + "6/unit".ljust(15))
print("300 above".ljust(25) + "8/unit".ljust(15))


print('\n\n Alternative 5 : Store Data in a Dictionary and Loop (Recommended)\n')
slab = {
    "0-99": "2/unit",
    "100-199": "3.5/unit",
    "200-249": "4.5/unit",
    "250-299": "6/unit",
    "300 above": "8/unit"
}

print("*" * 50)
print("Electricity Slab System".center(50))
print("*" * 50)

for units, rate in slab.items():
    print(f"{units:<25}{rate:<15}")'''
    
# print('\n\n Alternative 6 : Store Data in a List of Tuples (My Favorite)\n')
print("Bill Calucation Rule based on below slab \n")
slabs = [
    ("0-99", "2/unit"),
    ("100-199", "3.5/unit"),
    ("200-249", "4.5/unit"),
    ("250-299", "6/unit"),
    ("300 above", "8/unit")
]
print("*" * 50)
print("Electricity Slab System".center(50))
print("*" * 50)
for unit, rate in slabs:
    print(f"{unit:<25}{rate:<15}")
    
# print('\n\n Alternative 7 : Using a Multi-line String\n')   
# print("""Bill Calucation Rule based on below slab \n
# **************************************************
#             Electricity Slab System
# **************************************************
# 0-99                     2/unit
# 100-199                  3.5/unit
# 200-249                  4.5/unit
# 250-299                  6/unit
# 300 above                8/unit
# """)

n=int(input("Enter Number of user to Print Bill"))

for i in range(n):
    cust_name, cust_ID, Cust_M_NO, Cust_Curr, Cust_last = info_in(i)
    dispCustBillInfo(cust_name,cust_ID,Cust_M_NO)
    BillAmount=custBillAmount(Cust_last,Cust_Curr)
    print("Total amount is:",BillAmount)
    print("\n\n")




