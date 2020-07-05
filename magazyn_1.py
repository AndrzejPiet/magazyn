import json

commands_list = ('exit', 'hello', 'show', 'add item') # lista poleceń dla użytkownika

def choice_console ():
    return commands_list #funkcja wykorzystujaca liste polecen
    
commands = choice_console()

print(f"The list of available commands : ","\n",  commands, "\n")
ignite = input ("What would you like to do  ? :")

items= [ 
    ("jablka", 100, "kg", 30),
    ("czeresnie", 20, "kg", 50) , 
    ("woda", 1000, "l", 1.2),
    ("lemoniada", 100, "l", 2)
       ]
with open('warehouse_items.txt', 'w') as store_file : # tworze liste do zapisywania danych produktów w json
     json.dump(items, store_file)
with open('warehouse_items.txt', 'r') as storefile: # wczytuję produkty z listy do nowej listy, ktora ma zapamietywac NOWE wpisy
     items=json.load(storefile)

def get_items():
    print("-"*54)
    print('| {:^15}| {:^9}| {:^6}|{:^15}|' .format("Name" , "Quantity", "Unit" , "Unit Price (PLN)"))
    print("-"*54)
    for i in items:
        print('|', i[0],' '* (13-len(i[0])),'| ', i[1], ' '*(6-len(str(i[1]))) \
          ,'| ', i[2],' '*(3-len(str(i[2]))),'|   ', i[3],' '*(10-len(str(i[3]))), '|' )
    print("-"*54)

new_item=()

def add_item():
    name= input (" Please input NAME of the product : ")
    quantity= input ("Please input QUANTITY of the product :  ")
    unit = input ("Please input UNIT of measure eg. l, kg, pcs :  ")
    price = input ("Please input PRICE in PLN (per unit) :  ")
    new_item= [name, quantity, unit, price]
    items.append(new_item)
    
     


while True :
    
    if ignite in commands :
        if ignite == "exit":
            print("Exiting ... Bye")
            break
        if ignite == 'show':
            get_items()
            print('End of the list \n')
            ignite = input ("Please chose What would you like to do ? :")
        if ignite == 'add item':
            add_item()
            with open('warehouse_items.txt', 'w') as store_file : # tworze liste do zapisywania danych produktów w json
                json.dump(items, store_file)
            ignite = input ("Please chose What would you like to do ? :")
        else :
            print("Command not working yet . ")
            ignite = input ("Please chose What would you like to do ? :") 
    else:
        print("Not valid command, choose from the list", commands)
        ignite = input ("What is your command ? : ") 