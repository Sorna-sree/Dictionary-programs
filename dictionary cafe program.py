menu = {
    "items1":
        {
            "name":"vadai",
            "cost":10
            
        },
    "item2":
        {
            "name":"tea",
            "cost":15
        
        },
    "item3":
        {
            "name":"corn",
            "cost":20
        
        }

}
transactions = 10 #total 10 transaction
amount = 0
total_amount = 0
  
while(transactions > 0):
    for key in menu.keys():
        order = int(input( "how many " + str((menu[key]["name"])) + " you want to buy = ") )
        amount += (menu[key]["cost"] * order)
    total_amount += amount #calculate the total amount
    print("customer buys:  " + str(amount) +  "Rs") #print the one transaction amount
    amount = 0
    transactions -= 1
print("Total sales:  " + str(total_amount) + " rs") #total sales 
