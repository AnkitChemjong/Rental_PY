from Display_Instrument import Display_Details, Details_to_dictionary
import datetime
import random
Date= datetime.datetime.now()
currentDate = Date.strftime("%d-%m-%Y")
# returnProcess function for return process
def returnProcess():
    global cusrenting
    global Customername
    global Customeraddress
    global Customernumber
    global instrumentamount
    global instrumentid
    global instrumentday
    global forIds
    forIds=[]
    global forAmounts
    forAmounts=[]
    global fine_price
    fine_price=0
    Dictionary_value_rtn=Details_to_dictionary()
    orloop=True
    while (orloop):
        newloop=True
        while(newloop):
            print("\n----WELCOME TO OUR SHOP (ANKIT RENTAL SHOP) SIR/MAM----")
            # taking customer name as input
            print("\n----What is your Full Name sir/mam?----")
            Customername=input("\n=>>>>").upper().strip()
            if Customername=="":
                newloop=True
                print("\nPlease sir/mam enter your name in String")
            else:
                newloop=False
        while(newloop==False):
            # taking input of address of customer
            print(f"\n----What is your Address mr/mrs_{Customername}----")
            Customeraddress=input("\n=>>>>").upper().strip()
            if Customeraddress=="":
                newloop=True
                print(f"\nPlease mr/mrs_{Customername} enter your Address in String")
            else:
                newloop=True
        while(newloop):
            # taking number of customers
            print(f"\n----What is your Number mr/mrs_{Customername}?----")
            try:
                Customernumber=int(input("\n=>>>>"))
                if Customernumber<0:
                    newloop=True
                    print(f"\n----Please mr/mrs_{Customername}  enter your valid number----")
                else:
                    newloop=False
            except ValueError:
                print(f"\n----please mr/mrs_{Customername} enter your number as integer----")
        rnloop=True
        while(rnloop):
            print("\n----WE OFFER A VARIETY OF INSTRUMENTS FOR YOUR CHOICE----")
            # called functions of Display_Instruments() to display details
            Call= Details_to_dictionary()
            Display_Details(Call)
            user_confirmation_instrument_return = input(f"\n----Do you want to return Instroument of our shop? (Enter 'yes' or 'not' mr/mrs_{Customername}):->").upper().strip()
            if user_confirmation_instrument_return=="YES":
                print("\n----Processing----")
                inrloop=True
                while(inrloop):
                    try:
                        # taking input of instrument id
                        print(f"\n----Please mr/mrs_{Customername} select the instrumentid of the Instrument that you want to return----")
                        instrumentid=int(input("\n=>>>>"))
                        if instrumentid in Dictionary_value_rtn.keys():
                            inrloop=False
                            forIds.append(instrumentid)           
                        else:   
                            print(f"\n----Please mr/mrs_{Customername} enter a valid instrumentid of the Instruments!----")
                    except ValueError:
                        print(f"\n----Please mr/mrs_{Customername} enter instrumentid as Integer----")
                while(inrloop==False):
                    try:
                        # taking instrument amount from user
                        print(f"\n----Please mr/mrs_{Customername} enter the Amount of Instrument that you want ot Return----")
                        instrumentamount=int(input("\n=>>>>"))
                        if instrumentamount <=0:
                            print(f"\n----Please mr/mrs_{Customername} select the instrumentamount positive and greater than zero----")
                        else:
                            Dictionary_value_rtn[instrumentid]["Amount"]=int(Dictionary_value_rtn[instrumentid]["Amount"])+instrumentamount
                            with open("Details.txt", "w") as file:
                              for id, details in Dictionary_value_rtn.items():
                                file.write(f"{details['Name']},{details['Color']},{details['Brand']},{details['Size']},{details['Price']},{details['Amount']}\n")
                                inrloop=True
                            file.close()
                            forAmounts.append(instrumentamount)                                    
                    except ValueError:
                        print(f"\n----Please mr/mrs_{Customername} enter Amount as Integer----")
                while(inrloop):
                    try:
                        # taking input from user of total days registered for renting
                        print(f"\n----Please mr/mrs_{Customername} enter the total day you registered while renting----")
                        cusrenting=int(input("\n=>>>>"))
                        if cusrenting<=0:
                            print(f"\n----Please mr/mrs_{Customername} enter the valid day you registered while renting----")                  
                        else:   
                            inrloop=False
                    except ValueError:
                        print(f"\n----Please mr/mrs_{Customername} enter renting time as Integer----")

                while(inrloop==False):
                    # taking input from customer of total days he keeps the instruments
                    print(f"\n----Pleae mr/mrs_{Customername} enter the total days you keep the instrument for---- ")
                    try: 
                        instrumentday=int(input("\n=>>>>"))
                        if instrumentday<=0:
                            print(f"\n----Please mr/mrs_{Customername} enter a valid time for instrumentday----")
                        elif instrumentday>(cusrenting+5):
                            print("\n----Hence, you don't return the instrument whithin 5 days late then of your renting time----\n----So you have to pay the extra fine 100 dollars for each extra days----")
                            price=int((instrumentday-(cusrenting+5))*100)
                            fine_price+=price
                            customer_comfirm=input(f"\n----Is it ok with you mr/mrs_{Customername} or you want to check again( Enter 'yes' or 'no'):->").upper().strip()
                            if customer_comfirm=="YES":
                                inrloop=False
                            else:
                                inrloop=True
                        else:
                            inrloop=True             
                    except ValueError:
                        print(f"\n----Pleae mr/mrs_{Customername} enter integer as day for the instrumentday----")
            else:
                print(f"\n----Thankyou for your kind Information mr/mrs_{Customername}----")
                rnloop=False
            user_confirmation_instrument_returns = input(f"\n----Do you want to return more Instroument of our shop? (Enter 'yes' or anything you want(for not) mr/mrs_{Customername}):->").upper().strip()
            if user_confirmation_instrument_returns=="YES":
                 rnloop=True
            else:
                rnloop=False
        orloop=False
# Function for fine process 
def fineProcess():
    dictionary_values=Details_to_dictionary()
    customerrent=cusrenting
    instday=instrumentday
    final_fine=fine_price
    cusname=Customername
    cusaddress=Customeraddress
    cusnumber=Customernumber
    choiceloop=True
    while(choiceloop):
        print(f"\n----mr/mrs_{cusname} you have two ways to return the Instruments----")
        print("\n1).Visit our shop with the instrument----")
        print("\n2).Our workers will visit your house and get the Instruments(cost $100 extra charge)----")
        choices=input("Type 'one' or 'two':->").strip().upper()
        if choices=="ONE":
            customer_view=input(f"\n----How was your experience me/ms_{cusname}('good' or anything you want):->").strip().upper()
            if customer_view=="GOOD":
                print("\n----We are very glad to serve you----\n----It was very nice experince working with you----")
                
            else:
                print(f"\n----We are very sorry for the inconvenience mr/mrs_{cusname}----\n----We will try our best next time----")
            print(f"\n---- mr/mrs_{cusname} your bill is generated in txt file----")
            with open(cusname+"_Return_Bill.txt", "w") as billfiles:
                sales=random.randint(1,100)
                # creating a new text file for Customer Receipt and writing on it
                billfiles.write("""\t=============================================================================================
    =                                   Ankit Rental Shop                                     =
    =                                                                                         =
    =                                       Rent Bill                                         =
    =                                                                                         =
    ===========================================================================================""")
                billfiles.write(f"\n\n\tSale No: {sales}\t\t\t\t\t\t\t\t Date: {currentDate}\n")
                billfiles.write(f"\n\t\t\t\tCustomer Name:->{cusname}")
                billfiles.write(f"\n\t\t\t\tCustomer Address:->{cusaddress}")
                billfiles.write(f"\n\t\t\t\tCustomer Number:->{cusnumber}")
                for i in range(0,len(forIds)):
                    billfiles.write(f"\n\t\t\t\tFor Instrument:->{dictionary_values[forIds[i]]['Name']}")
                    billfiles.write(f"\n\t\t\t\tInstrument{i} Amount:->{forAmounts[i]}")
                    billfiles.write(f"\n\t\t\t\tInstrument{i} Name:->{dictionary_values[forIds[i]]['Name']}")
                billfiles.write(f"\n\t\t\t\tTotal Rent day:->{instday}")
                billfiles.write(f"\n\t\t\t\tNumber of Instrument:->{len(forIds)}")
                billfiles.write(f"\n\t\t\t\tTotal fine day:->{instday-customerrent}")
                billfiles.write(f"\n\t\t\t\tTotal fine:->${final_fine}")

                billfiles.write("""\n\t\t\t\t=======================================
                 =                                   =
                 =         Thankyou for returning!!  =
                 =                                   =
               =========================================   """)
                billfiles.write("""\n\t\t\t\t=======================================
                 =                                   =
                 =         Please visit again!!      =
                 =                                   =
               =========================================   """)
                print("\n----Please collect your bill----")
               
                print("\n----Please visit again----")
            choiceloop=False
        elif choices=="TWO":
            worker_cost=100
            # asking the customer how was your experience 
            customer_view=input(f"\n----How was your experience me/ms{cusname}('good' or anything you want):->").strip().upper()
            if customer_view=="GOOD":
                print("\n----We are very glad to serve you----\n----It was very nice experince working with you----")
                
            else:
                print(f"\n----We are very sorry for the inconvenience mr/mrs_{cusname}----\n----We will try our best next time----")
            print(f"\n---- mr/mrs_{cusname} your bill is generated in txt file----")
            # creating a new text file for Customer Receipt and writing on it
            with open(cusname+"_Return_Bill.txt", "w") as billfiles:
                sales=random.randint(1,100)
                billfiles.write("""\t=============================================================================================
    =                                   Ankit Rental Shop                                     =
    =                                                                                         =
    =                                       Rent Bill                                         =
    =                                                                                         =
    ===========================================================================================""")
                billfiles.write(f"\n\n\tSale No: {sales}\t\t\t\t\t\t\t\t Date: {currentDate}\n")
                billfiles.write(f"\n\t\t\t\tCustomer Name:->{cusname}")
                billfiles.write(f"\n\t\t\t\tCustomer Address:->{cusaddress}")
                billfiles.write(f"\n\t\t\t\tCustomer Number:->{cusnumber}")
                for i in range(0,len(forIds)):
                    billfiles.write(f"\n\t\t\t\tFor Instrument:->{dictionary_values[forIds[i]]['Name']}")
                    billfiles.write(f"\n\t\t\t\tInstrument{i} Amount:->{forAmounts[i]}")
                    billfiles.write(f"\n\t\t\t\tInstrument{i} Name:->{dictionary_values[forIds[i]]['Name']}")
                billfiles.write(f"\n\t\t\t\tTotal Rent day:->{instday}")
                billfiles.write(f"\n\t\t\t\tNumber of Instrument:->{len(forIds)}")
                billfiles.write(f"\n\t\t\t\tTotal fine day:->{instday-customerrent}")
                billfiles.write(f"\n\t\t\t\tTotal fine:->${final_fine+worker_cost}")

                billfiles.write("""\n\t\t\t\t=======================================
                 =                                   =
                 =         Thankyou for returning!!  =
                 =                                   =
               =========================================   """)
                billfiles.write("""\n\t\t\t\t=======================================
                 =                                   =
                 =         Please visit again!!      =
                 =                                   =
               =========================================   """)
                print("\n----Please collect your bill----") 

                print("\n----Please visit again----")
            choiceloop=False
        else:
            print("\n----Please choose between these two options----")
            choiceloop=True