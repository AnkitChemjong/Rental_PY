from Display_Instrument import Details_to_dictionary,Display_Details
from Rent_Instrument import rentProcess,billProcess
from Return_Instrument import returnProcess,fineProcess
# function for all the activity for the project 
def Combined():
    finalloop=True
    print("""\t=============================================================================================
        =                                                                                         =
        =                                  Ankit Rental Shop                                      =
        =                                                                                         =
        ===========================================================================================""")
    print("""\t=============================================================================================
        =       Welcome to our Rental shop, You can rent Different Instrument from hare!!         =
        =              Our shop charges our Customer on basis of 5 Days.                          =      
        =       You have to return the Instrument in time but, if due to some problem             =
        =           you can take extra 5 days but after that you will be fined 100$!!             =
        ===========================================================================================""")
    Confirmation=input("Just enter OK for further!!!:->")
    while (finalloop):
        print("""\t\t================================================================
                =           You Have Following Four Choices!!!!              =
                =              1) 1 For Display Details!                     =      
                =              2) 2 For Renting Instrument!!                 =
                =              3) 3 For Returning Instrument!!!              =
                =              4) 4 For Exit From Program!!!!                =
                ==============================================================""")
        try:
            fori=int(input("Enter your choice:->"))
            if fori==1:
                # calling Details_to_dictionary from Display_Instrument
                call=Details_to_dictionary()
                # calling Display_Details from Display_Instrument
                Display_Details(call)
            elif fori==2:
                # calling rentProcess fuction from Rent_Instrument
                rentProcess()
                # calling billProcess function from Rent_Instrument
                billProcess()
            elif fori==3:
                is_bill=input("Do you have bill?('YES' or anything you want(for no)):->").upper().strip()
                if is_bill=="YES":
                    # calling returnprocess from Return_Instrument
                    returnProcess()
                    rented=input("Do you rent or not?('YES' or anything you want(for no)):->").upper().strip()
                    if rented=="YES":
                      #calling fineProcess from Return_Instrument 
                      fineProcess()
                    else:
                        print("\n....Sorry for the inconvenience sir/mam....")
                else:
                    print("\n----First get the bill by renting something----")
            elif fori==4:
                print("\n----exited----")
                finalloop=False
                break
            else:
                print("\n---INVALID choice ----")
            print("\n----What do you want to do?")
            new_loop=True
            while new_loop:
                print("""===============================================
=         You have following Two choices!!!!    =
=              1) 1 For Run Again!              =      
=                                               =
=              2) 2 Don't Run!!                 =
=================================================""")
                try:
                    last_run=int(input("\n>>>>:->"))
                    if(last_run==1):
                        new_loop=False
                        finalloop=True
                    else:
                        new_loop=False
                        finalloop=False
                        print("\n----exited----")

                except ValueError:
                    print("\nPlease selec3t the valid choice!!!!!")

        except ValueError:
            print("\nPlease select the valid choice!!!!!")
            finalloop=True
# calling Combined function
Combined()