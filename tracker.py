import json

print("--- WELCOME FROM FINANCIAL TRACKER---")

name = input ("Enter your name:  ")

try:
   with open('ban.txt','r') as f:
     balance = json.load(f)
     print(balance)

except FileNotFoundError:
    
    print(f"{name} Enter your starting balance")
    balance = int(input(">   "))
    print(f"Your starting balance : ${balance} ")

except json.JSONDecodeError:
   print(f"{name}, ban.txt was corrupted or empty starting fresh.")
   balance = int(input("Enter your starting balance: "))
   print(f"Your starting balance: ${balance}")

try:
   with open("store.txt","r") as f:
     store = json.load(f)
     print(store)
except FileNotFoundError:
    store = []
except json.JSONDecodeError:
   print("store.txt was corrupted or empt starting fresh.")
   store = []
  
ex = 0
 
def add():
    global balance
    print(balance)
    a1 = int(input("Income>   "))
    print(f"income = {a1}")
    balance += a1
    print(f"New balance: {balance}")

def expense():
    global ex, store, balance
    for i in range(3):
      item = input("Enter item name:  ")
      
      a3 = int(input("Expense:  "))
      
      if a3 > balance:
          print("You don't have enough money!")
      else:
       
         balance -= a3
        
         ex += a3

         print(f"New balance: {balance}")
        
         with open("ban.txt", "w") as f:
           json.dump(balance, f, indent=4)

         a6 = input("Enter item type:  ")
      
         u = {
         "item" : item,
         "cost" : a3,
         "type" : a6
         }
 
         store.append(u)
      
         print(f"Your Store expense information> {store}")

      with open("store.txt", "w") as f:
        json.dump(store, f, indent=4)

def view():
     
     global balance
     print(balance)

def view_expense():
     global ex
     print(f"Total expense {ex}")
    
     
while True:
        print("===== FINANCE TRACKER =====")
        print('''
Add income
Add expense
View expenses
View categories
View balance
Exit
''')

        cho = input("Choose>     ")
      
        try: 
          if cho == "Add income":
           add()
          elif cho == "Add expenses":
           expense()
          elif cho == "View balance":
            view()
          elif cho == "View expenses":
            view_expense()
      
          elif cho == "Exit":
             break
    
        except ValueError:
           print("Enter a number!")

        
  



   

