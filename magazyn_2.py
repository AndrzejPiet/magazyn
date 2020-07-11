import json


def choice_console ():
    commands_list = ('exit', 'hello', 'show', 'add item','sell') # lista poleceń dla użytkownika
    print(f"The list of available commands : ","\n",  commands_list, "\n")
    return commands_list

    
with open('warehouse_items.txt', 'r') as storefile: # wczytuję produkty z listy do nowej listy, ktora ma zapamietywac NOWE wpisy
     items=json.load(storefile)

products = {
    "jablka": [100, "kg", 30],
    "czeresnie": [20, "kg", 50] , 
    "woda" : [1000, "l", 1.2],
    "lemoniada" : [100, "l", 2],
    "Proszek" : [20, "kg", 4.5]
       }

def get_items():
    print("-"*54)
    print('| {:^15}| {:^9}| {:^6}|{:^15}|' .format("Name" , "Quantity", "Unit" , "Unit Price (PLN)"))
    print("-"*54)
    for key, values in products.items():
        print('|', key,' '* (13-len(key)),'| ', values[0], ' '*(6-len(str(values[0]))) 
        ,'| ', values[1],' '*(3-len(str(values[1]))),'|   ', values[2],' '*(10-len(str(values[2]))), '|' )
    print("-"*54)


def add_item():
    new_key = input(" Please input NAME of the product : ")
    quantity= int(input ("Please input QUANTITY of the product :  "))
    unit = input ("Please input UNIT of measure eg. l, kg, pcs :  ")
    price = int( input ("Please input PRICE in PLN (per unit) :  "))
    new_value = [quantity, unit, price]
    products[new_key]= new_value
    
    
def sell_item():
    get_items()
    name_key = input(" Please input NAME of the product you want to sell : ") 
    for k, v  in products.items():
        if k == name_key:
            print (k, " current quantity : ", v[0], "", v[1])
            sell_quantity = int(input ("Insert quantity to sell :"))
            new_values = [v[0]- sell_quantity, v[1], v[2]]
            print(k, "we sold :", sell_quantity, v[1])
            products[name_key]=new_values
            print("Current status of warehouse :")
            get_items()
    



while True :
    with open('warehouse_items.txt', 'w') as store_file : # tworze liste do zapisywania danych produktów w json
     json.dump(products, store_file)
    

    commands=choice_console()
    ignite = input ("What would you like to do  ? :")
    if ignite in commands :
        if ignite == "exit":
            print("Exiting ... Bye")
            break
        if ignite == 'show':
            get_items()
            print('End of the list \n')
            
        if ignite == 'add item':
            add_item()
            print("Current item status is :")
            get_items()
       
        if ignite == 'sell':
            sell_item()
            
        
    else:
        print("Not valid command, choose from the list", commands)
         