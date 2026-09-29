'''Accept product details and calculate the final bill.
Requirements:
• Input product name, quantity and price.
• Calculate subtotal and total.
• Display a formatted invoice.
'''

def store():
    hardware_products = {
        "Hammer": 450, "Screwdriver": 180,"Tape": 250,"Drill": 3200,"Pipe": 520,"Tap": 650,"Bag": 420,
        "Brush": 120,"Bulb": 180,"Board": 550,"Nail": 140,"Wrench": 650,"Pliers": 380,
        "Sandpaper": 30,"Adhesive": 220,"Helmet": 550,"Grinder": 4200,"Valve": 380,"MCB": 450,
        "Wire": 1800
        }
    # A=list(hardware_products.keys())
    
    for i in hardware_products.keys():
        print(i)
    
    Bill=[]
    
    Total=0        
    while(True):
        produce={}
        product=input("Enter product: ")
        quantity=int(input("Enter the Quantity: "))
        price=hardware_products[product]
        amount=price*quantity
        produce['Product']=product
        produce['Quantity']=quantity
        produce['Price']=price
        produce['Amount']=amount
        Bill.append(produce)              
        Total=amount+Total
        print(f"Total is now {Total}")
          
        choice = input("Add another product? (Press N or n to finish): ")
        if choice=='N' or choice=='n':
            print(f"Final total price to Pay {Total} only")
            break
        else:
            continue
    
    print("=" * 50)
    print("HARDWARE STORE".center(50))
    print("=" * 50)

    print(f"{'Product':<25}{'Qty':<8}{'Price':<10}{'Amount'}")
    print("-" * 50)
    for item in Bill:
        print(f"{item['Product']:<25}{item['Quantity']:<8}{item['Price']:<10}{item['Amount']}") 
    
    print("-" * 50)
    print(f"{'Total':<43}{Total}")
    print("=" * 50)


store()

    

