from tabulate import tabulate
# Function to add details in dictionary 
def Details_to_dictionary():
    Instruments_dictionary={}
    # text file is opened and readed
    with open('Details.txt', 'r') as details:
        for line in details:
           detail=line.strip().split(",")
           ID=len(Instruments_dictionary)+1
           Instruments_dictionary[ID]={
               "Name":detail[0],
               "Color":detail[1],
               "Brand":detail[2],
               "Size":detail[3],
               "Price":detail[4],
               "Amount":detail[5]
           }
        return Instruments_dictionary

# function to display the dictionary in tabuate format
def Display_Details(data):
    data_list = []
    for ID, item in data.items():
        row = [ID, item["Name"], item["Color"], item["Brand"], item["Size"], item["Price"], item["Amount"]]
        data_list.append(row)
   
    Headers=["ID","Name", "Color", "Brand", "Size", "Price", "Amount"]
    table =tabulate(data_list,headers=Headers,tablefmt='grid')
    print(table)