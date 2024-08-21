from Display_Instrument import Display_Details, Details_to_dictionary
import random
import datetime
Date=datetime.datetime.now()
currentDate=Date.strftime("%d-%m-%Y")
# rentProcess function for rent process
def rentProcess():
    global CustomerAmount
    global CustomerId
    global CustomerTime
    global Total_Amount
    Total_Amount=0
    global forId
    forId=[]
    global forAmount
    forAmount=[]
    global Dictionary_value
    Dictionary_value=Details_to_dictionary()
    yeploop=True
    while(yeploop):
        rentloop=True
        while(rentloop):
                print("\n----WELCOME TO OUR SHOP (ANKIT RENTAL SHOP) SIR/MAM----")
                print("\n----WE OFFER A VARIETY OF INSTRUMENTS FOR YOUR CHOICE----")
                Call= Details_to_dictionary()
                Display_Details(Call)
                user_confirmation_instrument_rent = input("\n----Do we have what you want? (Enter 'yes' or 'not' sir\mam):->").upper().strip()
                if user_confirmation_instrument_rent=="YES":
                        rentloop=False
                        print("\n----Proceeding....")
                        howrent=True
                        while(howrent):
                                # taking input of instrument id form customer
                                print("\n----Please sir/mam select the ID of the item you want to rent----")
                                try:
                                        CustomerId=int(input("\n=>>>>"))
                                        if CustomerId in Dictionary_value.keys():
                                                howrent=False
                                                forId.append(CustomerId)
                                        else:   
                                                print("\n----Please sir/mam enter a valid ID of the Instruments!----")
                                except ValueError:
                                        print("\n----Pleae sir/mam enter ID as Integer----")
                        print("\n----Our shop charges in range of 5 days for each instruments you will rent----")   
                        while(howrent==False):
                                # Taking time for rent time from customer as days
                                print("\n----Please sir/mam select the time(in days) for the renting process----")       
                                try:
                                        CustomerTime=int(input("\n=>>>>"))
                                        if CustomerTime<=0:
                                                print("\n----Please sir/mam select the time greater than zero----")
                                        else:
                                                howrent=True
                                except ValueError:
                                        print("\n----Please sir/mam select the Integer for time----")
                        while(howrent):
                                # Taking amount or quantity of instrument from customer
                                print("\n----Please sir/mam select the Amount of Instrument you want to rent----")
                                try:
                                        CustomerAmount=int(input("\n=>>>>"))
                                        if CustomerAmount<=0:
                                                print("\n----Please sir/mam select the Amount of Instrument more than zero----")
                                        elif CustomerAmount> int(Dictionary_value[CustomerId]['Amount']):
                                                print("\n----Sorry sir/mam the we dont have the seleted amount of this instrument----")
                                                howrent=False
                                        else:
                                                # updating dictionary
                                                Dictionary_value[CustomerId]['Amount']=int( Dictionary_value[CustomerId]['Amount'])-CustomerAmount
                                                with open("Details.txt", "w") as file:
                                                     for id, details in  Dictionary_value.items():
                                                        file.write(f"{details['Name']},{details['Color']},{details['Brand']},{details['Size']},{details['Price']},{details['Amount']}\n")
                                                file.close()
                                                
                                                
                                                forAmount.append(CustomerAmount)
                                                price=float(int(Dictionary_value[CustomerId]['Price'].replace("$", ""))*CustomerAmount*(CustomerTime/5))
                                                Total_Amount+=price
                                                howrent=False

                                except ValueError:
                                        print("\n----Please sir/mam select the Amount of Instrument as integer----")

                else:
                        print("\n----We are very sorry for your inconvenience!----")
                        rentloop=False
                # Asking Customer that he/she want to rent more or not
                print(f"\n----sir/mam Do you want to rent Anything else? (Enter 'yes' or 'Anything you want( for not)')----")
                cusmore=input("\n=>>>>").upper().strip()
                if cusmore=="YES":
                        rentloop=True
                else:
                        rentloop=False       
        yeploop=False  
# billProcess function for the bill generating process
def billProcess():  
       global CustomerName
       global CustomerNumber
       global CustomerAddress
       Rent_Cost=Total_Amount
       Dictionary_val=Details_to_dictionary()
       print("--------Hello! sir/mam--------\n\n----Inorder to provide you the Instrument from----\n\n----our shop we have to know the answer of followig questions----")
       user_confirmation = input("\n----Do you want to proceed? (Enter 'ok' or 'anything else(for no)' sir/mam):->").upper().strip()
       if user_confirmation == 'OK':
                print("\n----Proceeding....")
                inlooprent=False
                while(inlooprent==False):
                        # Taking name input of customer
                        print("\n----What is your Full Name sir/mam?----")
                        CustomerName=input("\n=>>>>").upper().strip()
                                                                                
                        if CustomerName=="":
                                print("\n----Pleae sir/mam enter Your Full Name----")
                        else:
                                inlooprent=True
                while(inlooprent):
                        # taking address input of customer
                        print(f"\n----What is your Address mrs./mr_{CustomerName}?----")
                        CustomerAddress=input("\n=>>>>").upper().strip()
                                                                        
                        if CustomerAddress=="":
                                print(f"\n----Please mrs./mr_{CustomerName}  enter Your Address----")
                        else:
                                inlooprent=False
                                                        
                while(inlooprent==False):
                        # taking phone number input of customer 
                        print(f"\n----Please mrs/mr_{CustomerName} enter you Phone Number----")       
                        try:
                                        CustomerNumber=int(input("\n=>>>>"))
                                        if CustomerNumber<0:
                                                print("\n----Please sir/mam select the valid Number----")
                                        else:
                                                inlooprent=True
                        except ValueError:
                                        print(f"\n----Please mrs/mr_{CustomerName} select the Integer for Number----")
                while(inlooprent):
                        print(f"\n----mr/mrs_{CustomerName} you have two ways to rent the Instruments----")
                        print("\n1).Visit our shop with the CostPrice----")
                        print("\n2).Our workers will Deliver the instruments to your Address (cost $100 extra charge)----")
                        choose=input("Type 'one' or 'two':->").strip().upper()
                        if choose=="ONE":
                                # taking input that how was the experience
                                customer_view=input(f"\n----How was your experience me/ms_{CustomerName}('good' or 'anything you want(for no)'):->").strip().upper()
                                if customer_view=="GOOD":
                                        print("\n----We are very glad to serve you----\n----It was very nice experience working with you----")
                                        
                                else:
                                        print(f"\n----We are very sorry for the inconvenience mr/mrs_{CustomerName}----\n----We will try our best next time----")
                                        
                                print(f"\n---- mr/mrs_{CustomerName} your bill is generated in txt file----")
                                with open(CustomerName+"_Rent_Bill.txt", "w") as billfile:
                                 sale=random.randint(1,100)
                                 # creating a new text file for Customer Receipt and writing on it
                                 billfile.write("""\t=============================================================================================
        =                                   Ankit Rental Shop                                     =
        =                                                                                         =
        =                                       Rent Bill                                         =
        =                                                                                         =
        ===========================================================================================""")
                                 billfile.write(f"\n\n\tSale No: {sale}\t\t\t\t\t\t\t\t Date: {currentDate}\n")
                                 billfile.write(f"\n\t\t\t\tCustomer Name:->{CustomerName}")
                                 billfile.write(f"\n\t\t\t\tCustomer Address:->{CustomerAddress}")
                                 billfile.write(f"\n\t\t\t\tCustomer Number:->{CustomerNumber}")
                                 for i in range(0,len(forId)):
                                        billfile.write(f"\n\t\t\t\tFor Instrument:->{Dictionary_val[forId[i]]['Name']}")
                                        billfile.write(f"\n\t\t\t\tInstrument{i} Amount:->{forAmount[i]}")
                                        billfile.write(f"\n\t\t\t\tInstrument{i} Name:->{Dictionary_val[forId[i]]['Name']}")
                                 billfile.write(f"\n\t\t\t\tNumber of Instrument:->{len(forId)}")
                                 billfile.write(f"\n\t\t\t\tYour total cost is {Rent_Cost}")
                                 billfile.write("""\n\t\t\t\t=======================================
                                 =                                   =
                                 =         Thankyou for renting!!    =
                                 =                                   =
                               =========================================   """)
                                 billfile.write("""\n\t\t\t\t=======================================
                                 =                                   =
                                 =         Please visit again!!      =
                                 =                                   =
                               =========================================   """)
                                print("\n----Please collect your bill----")

                                print("\n----Please visit again----")
                                inlooprent=False          
                        elif choose=="TWO":
                                Delivery_charge=100
                                customer_view2=input(f"\n----How was your experience me/ms_{CustomerName}('good' or 'anything you want(for no)'):->").strip().upper()
                                if customer_view2=="GOOD":
                                        print("\n----We are very glad to serve you----\n----It was very nice experince working with you----")
                                      
                                else:
                                        print(f"\n----We are very sorry for the inconvenience mr/mrs_{CustomerName}----\n----We will try our best next time----")
                                print(f"\n---- mr/mrs_{CustomerName} your bill is generated in txt file----")
                                with open(CustomerName+"_Rent_Bill.txt", "w") as billfile:
                                 sale=random.randint(1,100)
                                 # creating a new text file for Customer Receipt and writing on it
                                 billfile.write("""\t=============================================================================================
        =                                   Ankit Rental Shop                                     =
        =                                                                                         =
        =                                       Rent Bill                                         =
        =                                                                                         =
        ===========================================================================================""")
                                 billfile.write(f"\n\n\tSale No: {sale}\t\t\t\t\t\t\t\t Date: {currentDate}\n")
                                 billfile.write(f"\n\t\t\t\tCustomer Name:->{CustomerName}")
                                 billfile.write(f"\n\t\t\t\tCustomer Address:->{CustomerAddress}")
                                 billfile.write(f"\n\t\t\t\tCustomer Number:->{CustomerNumber}")
                                 for i in range(0,len(forId)):
                                        billfile.write(f"\n\t\t\t\tFor Instrument:->{Dictionary_val[forId[i]]['Name']}")
                                        billfile.write(f"\n\t\t\t\tInstrument{i} Amount:->{forAmount[i]}")
                                        billfile.write(f"\n\t\t\t\tInstrument{i} Name:->{Dictionary_val[forId[i]]['Name']}")
                                 billfile.write(f"\n\t\t\t\tNumber of Instrument:->{len(forId)}")
                                 billfile.write(f"\n\t\t\t\tYour total cost is {Rent_Cost+Delivery_charge}")
                                 billfile.write("""\n\t\t\t\t=======================================
                                 =                                   =
                                 =         Thankyou for renting!!    =
                                 =                                   =
                               =========================================   """)
                                 billfile.write("""\n\t\t\t\t=======================================
                                 =                                   =
                                 =         Please visit again!!      =
                                 =                                   =
                               =========================================   """)
                                print("\n----Please collect your bill----")

                                print("\n----Please visit again----")
                                inlooprent=False          
                        else:
                                print("\nPlease select between one or two")
                                inlooprent=True

       else:
                print("\n\n----Cancelled----!!!!")
                print("\n\n ----hence you have cancelled the process you have\n to come to our shop for the instruments----")
                print("\n\n ----we can't deliver it without your details----")
                print("\n---- sir/mam your bill is generated in txt file----")                
                with open("sir_mam_Rent_Bill.txt", "w") as billfile:
                        sale=random.randint(1,100)
                        # creating a new text file for Customer Receipt and writing on it
                        billfile.write("""\t=============================================================================================
=                                   Ankit Rental Shop                                     =
=                                                                                         =
=                                       Rent Bill                                         =
=                                                                                         =
===========================================================================================""")
                        billfile.write(f"\n\n\tSale No: {sale}\t\t\t\t\t\t\t\t Date: {currentDate}\n")
                        billfile.write(f"\n\t\t\t\tCustomer Name:->Null")
                        billfile.write(f"\n\t\t\t\tCustomer Address:->Null")
                        billfile.write(f"\n\t\t\t\tCustomer Number:->Null")
                        for i in range(0,len(forId)):
                                billfile.write(f"\n\t\t\t\tFor Instrument:->{Dictionary_val[forId[i]]['Name']}")
                                billfile.write(f"\n\t\t\t\tInstrument{i} Amount:->{forAmount[i]}")
                                billfile.write(f"\n\t\t\t\tInstrument{i} Name:->{Dictionary_val[forId[i]]['Name']}")
                                billfile.write(f"\n\t\t\t\tYour total cost is {Rent_Cost}")
                        billfile.write(f"\n\t\t\t\tNumber of Instrument:->{len(forId)}")
                        billfile.write("""\n\t\t\t\t=======================================
                         =                                   =
                         =         Thankyou for renting!!    =
                         =                                   =
                       =========================================   """)
                        billfile.write("""\n\t\t\t\t=======================================
                         =                                   =
                         =         Please visit again!!      =
                         =                                   =
                       =========================================   """)        
                print("\n----We will be waiting for you sir/mam----")   