import os

database_file = "database.txt"
admin_file = "admin.txt"
text_color = '\033[0;35m'
reset_color = '\033[0m'
food=[] #This is the list of Food Item
price=[] #This is the list of Food Item Price
details=[] #This is the list of Food Item Details
addon_food=[] #List of add-on
addon_price=[] #List of add-on's price
customize_sauce=[] #List for Customize --> variables of sauce categories
sauceprice=[] #List for Customize --> sauce's price
customize_topping=[] #List for Customize --> variables of topping categories
toppingprice=[] #List for Customize --> toppings's price
customize_cheese=[] #List for Customize --> variables of cheese categories
cheeseprice=[] #List for Customize --> cheese's price 
Customer_name = []
addon_order = []
addon_amount = []
orders = []
normal_cost = []
addon_cost = []
sumaddon = []
customize_cost = []
pizza_cost = []
topping_costsadding=[]
topping_ordersadding=[]
cheese_ordersadding=[]
cheese_costsadding=[]
topping_cost = []
sauce_cost = []
cheese_cost = []
topping_orders = []
sauce_orders = []
cheese_orders = []
customize_amount = []
quantity = []
addon = []
total = []
name=""
username=[]
gmail=''
password=""
birth_day=''
phone=''
forgot=''
admin=[]
codes=[]
discounts=[]
users=[]

def reload():
    global name,password,gmail,phone,birth_day,forgot,username
    username.clear()
    f=open('database.txt')
    for i in f:
        variables=i.split(",")
        username.append(variables[0])
    f.close()
    f=open("database.txt","r")
    f=f.readlines()
    lineindex=1

    try:
        linecontainsname=1+username.index(name)
        for i in f:
            if lineindex == linecontainsname:
                variables=i.strip().split(',')
                password=variables[1]
                gmail=variables[2]
                phone=variables[3]
                birth_day=variables[4]
                forgot=variables[5]
            lineindex=lineindex+1
    
    except ValueError:
        name=""
        password=""
        gmail=""
        phone=""
        birth_day=""
        forgot=""

    admin.clear()
    f=open('admin.txt')
    for i in f:
       variables=i.strip().split(',')
       admin.append(variables[0])
    f.close()
       
    
    food.clear()    #clear the lists, to avoid the repeatation of variables in list
    price.clear()
    details.clear()
    f=open("menu.txt")
    for i in f:
        variables = i.strip().split(',') #split ',' textfile be like: foodname,foodprice,fooddetails
        food.append(variables[0])        #so split ',' the first variables means variables[0] will save in food list
        price.append(variables[1])       #split ',' the second variables means variables[1] will save in price list
        details.append(variables[2])     #split ',' the third variables means variables[2] will save in details list
    f.close()
    addon_food.clear()
    addon_price.clear()
    f=open("addon.txt")
    for i in f:
        a,b=i.split(",")
        addon_food.append(a)
        b=b.strip("\n")
        addon_price.append(b)
    f.close()
    customize_sauce.clear()
    sauceprice.clear()
    customize_topping.clear()
    toppingprice.clear()
    customize_cheese.clear()
    cheeseprice.clear()
    f=open("customize.txt")
    variables = f.read().split('\n')   #customize textfile be like: option1,price : option2,price : option3,price
    sauce_line=variables[0]             #second row: topping1,price : topping2,price : topping3,price
    topping_line=variables[1]           #so we split it using "\n" first so the first variables is for sauces second is topping third is cheese
    cheese_line=variables[2]            #then we split it using ":" for each lines then split again using "," first variables is option second is price
    for pair in sauce_line.split(":"):  
        a,b = pair.split(",",1)             #split(',',1) that '1' means split only 1 times
        customize_sauce.append(a.strip())
        sauceprice.append(b.strip())
    for pair in topping_line.split(":"):
        a,b = pair.split(",",1)
        customize_topping.append(a.strip())
        toppingprice.append(b.strip())
    for pair in cheese_line.split(":"):
        a,b = pair.split(",",1)
        customize_cheese.append(a.strip())
        cheeseprice.append(b.strip())
    f.close()
    #loyalty part reload
    users.clear()
    f=open('orders.txt')
    for i in f:
        variables=i.split('|',1)
        users.append(variables[0])#a,b,c(a)
    f.close()
    codes.clear()
    discounts.clear()
    f=open('promo_code.txt')
    for i in f:#i=textfile 
        a,b=i.split(' ')#
        codes.append(a)
        b=b.strip('-%\n')
        discounts.append(b)#put b into discount[]
    f.close()


def search(food,searchvalue):
    global NOTIFI
    NOTIFI="SEARCHING......"
    item=0
    clear_screen()
    maxlength=30
    for i in food:
        i=i.ljust(maxlength," ")
        if searchvalue in i:
            print(f'🟩 {i}RM{price[item]} {details[item]}')
            item=item+1
    if item==0:
        print("\033[1;1m!Does Not Exist!\nCANNOT FOUND!\033[0m")


# Function to clear the screen
def clear_screen():
    reload()
    os.system('cls' if os.name == 'nt' else 'clear') #for windows, cls is the command to clear screen, for linux or MacOS nt command used.
    global NOTIFI
    print(text_color+"------------------------------------------------------------------------"+reset_color)
    banner = '\033[1;34m'+"""
  _____ _                  _         _                 _           
 |  __ (_)                (_)       | |               (_)          
 | |__) | ___________ _ __ _  __ _  | |     __ _ _ __  _ ___  __ _ 
 |  ___/ |_  /_  / _ \ '__| |/ _` | | |    / _` | '_ \| / __|/ _` |
 | |   | |/ / / /  __/ |  | | (_| | | |___| (_| | |_) | \__ \ (_| |
 |_|   |_/___/___\___|_|  |_|\__,_| |______\__,_| .__/|_|___/\__,_|
                                                | |                
                                                |_|                                                                      
  """+'\033[0m'
    print(banner)
    print(text_color+"------------------------------------------------------------------------"+reset_color)
    print("\033[1;32m"+NOTIFI)
    print(text_color+"------------------------------------------------------------------------"+reset_color)


# Function to display the main screen
try:
    open('database.txt', 'r')
except FileNotFoundError:
    f = open('database.txt', 'a+')
    f.close()
    f=open("database.txt","w")
    f.write(
    'wongyisen,wys123,wys@gmail.com,0107894563,0517,10am\n'
    'tehliwei,tlw123,tlw@gmail.com,0123697455,0405,1am\n'
    'chaiziyang,czy123,czy@gmail.com,0167418523,1004,3pm\n'
    'michael,asdasdasd,michael@gmail.com,0123456789,0404,6pm\n')
    f.close()
try:
    open('admin.txt', 'r')
except FileNotFoundError:
    f = open('admin.txt', 'a+')
    f.close()
    f=open("admin.txt","w")
    f.write(
    'micheal,micheal123,michealmicheal\n'
    'liwei,liwei123,weiwei\n'
    'chai,chai1234,yangyang\n'
    'yisen,yisen123,xiaosen\n')
    f.close()
try:
    open('promo_code.txt', 'r')#try behind the program
except FileNotFoundError:#if no
    f=open('promo_code.txt','a+')#it will create a new textfile
    f.close()
    f=open("promo_code.txt","w")
    f.write(
    'newuser -12.0%\n'
    'olduser -15.0%\n'
    'happyfamily -3.0%\n'
    'thankyouteacher -30.0%\n'
    'iloveyou -17.0%\n')
    f.close()
try:
    open('menu.txt', 'r')
except FileNotFoundError:
    f = open('menu.txt', 'a+')
    f.close()
    f=open("menu.txt","w")
    f.write(
    "Hawaii,15.0,Combination of sweet pineapple and savory ham\n"
    "Aloha Chicken,15.0,Featuring tender chicken and sweetness of pineapple\n"
    "BBQ Chicken,15.0,Smoky barbecue sauce and grilled chicken\n"
    "Beef Pepperoni,15.0,Flavorful beef pepperoni slices\n"
    "Chicken Pepperoni,15.0,Traditional pepperoni pizza\n"
    "Vegie Fiesta,10.0,Vegetable-packed pizza nad have colorful toppings\n"
    "Vegie Galore,10.0,Vegetarian pizza loaded with fresh and vibrant vegetables\n"
    "Flaming Tuna,10.0,Spicy featuring succulent tuna\n"
    "Spiciy Sambal,10.0,Featuring a zesty sambal sauce and fiery blend of spices\n"
    "Smoky Beef,15.0,Showcasing the rich and smoky flavors of tender beef\n"
    "Smoky Chicken,15.0,Smoky grilled chicken as star ingredient\n"
    "Classic Chicken,10.0,Juicy chicken with classic pizza toppings\n"
    "Classic Beef,10.0,Savory ground beef complemented by classic toppings\n"
    "Spicy Sausage,12.0, Spicy sausage slices adding zesty flavor every bite\n"
    "Smoky Pepperoni Mushroom,15.0,Somky  pepperoni and earthy mushrooms\n"
    "Tropical Sambal Prawn,18.0,Succulent prawns and tropical twist\n"
    "Ultimate Hawaii,20.0,Combining ham pineapple and other delightful toppings\n"
    "Meatasaurus,20.0,Meat lover's dream variety of savory meats\n"
    "Super Cheese,15.0,Cheese lover's delight topped with a lot of cheese!\n"
    "Simply Cheesse,12.0,Combination of different cheese\n"
    "Seafood Delight,18.0,Packed with  medley of fresh flavorful seafood\n"
    )
    f.close()
try:
    open('addon.txt', 'r')
except FileNotFoundError:
    f = open('addon.txt', 'a+')
    f.close()
    f=open("addon.txt","w")
    f.write(
    "Mushroom Soup,6.0\n"
    "Garlic Bread,6.0\n"
    "Chicken Wing,12.0\n"
    "Onion Ring,10.0\n"
    "Chocolate Lava Cake,8.0\n"
    "Potato Wedges,10.0\n"
    "Pepsi(1.5L),6.0\n"
    "7 Up(1.5L),6.0\n"
    "Pepsi Black(1.5L),6.0\n"
    "Lipton Iced Tea,6.0\n"
    "Twister Orange,10.0\n"
    "Pepsi(Can),3.0\n"
    "Lipton Iced Tea(Can),4.0\n"
    "Mineral Water,2.0\n"
    )
    f.close()
try:
    open('customize.txt', 'r')
except FileNotFoundError:
    f = open('customize.txt', 'a+')
    f.close()
    f=open("customize.txt","w")
    f.write(
    "Barbecue,2.0:Tomato,1.0:Sambal,3.0:Chili,2.0:Mayo,2.0:Spicy tomato,2.0\n"
    "Pepperoni,3.0:Ham,3.0:Pineapple,2.0:Bacon,3.0:Beef Mince,3.0:Onion,1.0\n"
    "Mozza & Cheddar,2.5:Blue Cheese,3.0:Feta Cheese,3.0\n"
    )
    f.close()
try:
    open('orders.txt', 'r')
except FileNotFoundError:
    f = open('orders.txt', 'a+')

# Function to sign up a new user
def sign_up():
  global NOTIFI,name
  NOTIFI="Please Sign Up"
  clear_screen()
  name = input("Enter username: ")

  # Check if the username already exists
  if (name in username) or (name in admin):
    NOTIFI=("Username already exists.")
    choice = input(
      "1. Continue Sign Up\n2. Back to main screen\nEnter your option: ")

    if choice == "1":
      sign_up()
    elif choice == "2":
      main()
    else:
      NOTIFI="Invalid option. Returning to main screen."

  else:
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if len(password) < 6:
      NOTIFI="Password is too short. Minimum length is 6 characters."
      input("Press Enter to continue...")
    elif password == confirm_password:
      key = input("When you born? (Use when you forget your password)")
      # Save the new user to the database
      with open(database_file, "a") as file:
        file.write(f"{name},{password},-,-,-,{key}\n")

      NOTIFI=("User successfully signed up.")
      input("Press Enter to continue...")
    else:
      NOTIFI=("Passwords do not match.")
      clear_screen()
      input("Press Enter to continue...")
      main()

# Function to sign up a new admin account
def admin_signup():
  global NOTIFI
  NOTIFI="Please Sign Up"
  clear_screen()
  newUsername = input("Enter username: ")

  # Check if the username already exists
  if (newUsername in username) or (newUsername in admin):
    NOTIFI=("Username already exists.")
    clear_screen()
    choice = input(
      "1. Continue Sign Up\n2. Back to main screen\nEnter your option: ")

    if choice == "1":
      admin_signup()
    elif choice == "2":
      return
    else:
      NOTIFI="Invalid option. Returning to main screen."

  else:
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if len(password) < 6:
      NOTIFI="Password is too short. Minimum length is 6 characters."
      input("Press Enter to continue...")
    elif password == confirm_password:
      key = input("What is your Nickname? (Use when you forget your password)")
      # Save the new user to the database
      with open("admin.txt", "a") as file:
        file.write(f"{newUsername},{password},{key}\n")

      NOTIFI=("Admin successfully signed up.")
      input("Press Enter to continue...")
    else:
      NOTIFI=("Passwords do not match.")
      clear_screen()
      input("Press Enter to continue...")
      return

# Function to log in a user
def login():
  global NOTIFI,name
  NOTIFI=("Please Login")
  clear_screen()
  name = input("Enter username: ")
  
  password = input("Enter password: ")
  login_successful = False

  # Check if the username exists and password matches in the admin.txt file
  with open('admin.txt', 'r') as admin_file:
        for line in admin_file:
            stored_username,stored_password,_= line.strip().split(',')
            if name == stored_username and password == stored_password:
                input("Press Enter to continue...")
                login_successful = True
                admin_menu()
                main()
        admin_file.close()
  # Check if the username exists and password matches in the database.txt file
  with open('database.txt', 'r') as user_file:
    for line in user_file:
        stored_username,stored_password,_,_,_,_ = line.strip().split(',')
        if name == stored_username and password == stored_password:
            NOTIFI=(f"Successful login as User. Welcome {name}!")
            input("Press Enter to continue...")
            login_successful = True
            user_menu()
    user_file.close()
  if login_successful==False:
    NOTIFI=("Username or password is incorrect.")
    clear_screen()
    choice = input(
      "1. Continue Login\n2. Back to main screen\nEnter your option: ")

    if choice == "1":
      login()
    elif choice == "2":
      clear_screen()
    else:
      NOTIFI=("Invalid option. Returning to main screen.")


# Function to change password
def forgot_password():
  global NOTIFI,name,new_password,gmail,phone,birth_day,neededkey
  NOTIFI=("Please Enter your username")
  clear_screen()
  name = input("Enter username: ")
  if name in username: 
    with open('database.txt', 'r') as user_file:
        file=user_file.readlines()
        lineindex= 1
        linecontainsname= 1+username.index(name)
        user_file.close()
        for line in file:
            if lineindex == linecontainsname:
                variables=line.split(",")
                neededkey=(variables[5]).strip("\n")
            lineindex=lineindex+1
        key = input("When you born?(Answer as you register)")
        if key == neededkey:
            NOTIFI=("Please Enter your password")
            clear_screen()
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm new password: ")
            if len(new_password) < 6:
                NOTIFI=(
                "Password is too short. Minimum length is 6 characters.")
                input("Press Enter to continue...")
                clear_screen()
            elif new_password == confirm_password:
                    # Update the password in the appropriate file
                with open("database.txt", "r") as file:
                    lines = file.readlines()
                    file.close()
                with open("database.txt", "w") as file:
                    for line in lines:
                        stored_username,b,c,d,e,f = line.strip().split(",")
                        if name == stored_username:
                            file.write(f"{name},{new_password},{c},{d},{e},{f}\n")
                        else:
                            file.write(line)
                    file.close()
                NOTIFI=("Password successfully changed.")
                input("Press Enter to continue...")
                clear_screen()
            else:
                NOTIFI="Passwords do not match."
                input("Press Enter to continue...")
                clear_screen()
        
        else:
            NOTIFI="Incorrect KeyWord"
            
  elif name in admin: 
    with open('admin.txt', 'r') as admin_file:
        file=admin_file.readlines()
        lineindex= 1
        linecontainsname= 1+admin.index(name)
        admin_file.close()
        for line in file:
            if lineindex == linecontainsname:
                variables=line.split(",")
                neededkey=(variables[2]).strip("\n")
            lineindex=lineindex+1
        key = input("What is your nickname?(Answer as you register)")
        if key == neededkey:
            adminname=name
            NOTIFI=("Please Enter your password")
            clear_screen()
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm new password: ")
            if len(new_password) < 6:
                NOTIFI=(
                "Password is too short. Minimum length is 6 characters.")
                input("Press Enter to continue...")
                clear_screen()
            elif new_password == confirm_password:
                    # Update the password in the appropriate file
                with open("admin.txt", "r") as file:
                    lines = file.readlines()
                    file.close()
                with open("admin.txt", "w") as file:
                    for line in lines:
                        stored_username,b,c= line.strip().split(",")
                        if adminname == stored_username:
                            file.write(f"{adminname},{new_password},{c}\n")
                        else:
                            file.write(line)
                    file.close()
                NOTIFI=("Password successfully changed.")
                input("Press Enter to continue...")
                clear_screen()
            else:
                NOTIFI="Passwords do not match."
                input("Press Enter to continue...")
                clear_screen()
        
        else:
            NOTIFI="Incorrect KeyWord"
            
          
  else:
    NOTIFI=("Username does not exist.")
    clear_screen()
    choice = input(
      "1. Continue Forgot Password\n2. Back to main screen\nEnter your option: "
    )

    if choice == "1":
      forgot_password()
    elif choice == "2":
      return
    else:
      NOTIFI="Invalid option. Returning to main screen."


# Main program loop
def main():
    global NOTIFI
    NOTIFI=("Welcome to Pizzeria Lapisa")
    while True:
        clear_screen()
        print("1. Sign Up")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Enter your option: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            login()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            NOTIFI=(
            "Thank you for visiting Pizzeria Lapisa Terminal Shop.")
            input("Press Enter to continue...")
            clear_screen()
            break
        else:
            NOTIFI=("Invalid option. Returning to main screen.")

#chai part
def order():
  global name
  menu = open("menu.txt","r")
  food = []
  price = []
  global NOTIFI
  NOTIFI="ADD TO BOOKING CART"
  for i in menu:
        variables = i.strip().split(',')
        food.append(variables[0])
        price.append(variables[1])
        details.append(variables[2])
  option = input("(a)Normal Pizza | (b) Customize Pizza ")
  if option.lower() =="a":
    while True:
      
      print("-------------------------------------")
      print("Item                                    Price                Details")
      x = len(food)
      i=0
      maxlength=30
      for var in food:
        var_format = var.ljust(maxlength," ")
        if i < 9 :
           print(f"0{i+1}: {var_format}      RM{price[i]} {details[i]}")
           i= i + 1
        else:
          print(f"{i+1}: {var_format}      RM{price[i]} {details[i]}")
          i = i+1
      option = input("Do You want to order?(Y/N)")
      if option.upper() == "Y":
        num = int(input("Type the Index of food you want to Order(Only Numbers):"))
        if num > len(food):
              clear_screen()
              print("Item doesnt exist")
              continue
        elif num < len(food):    
              orders.append(food[num-1])
              print(f"{food[num-1]}      price=RM{price[num-1]} per pizza")
              amount = int(input("What is the amount of item you want to order:"))
              quantity.append(amount)
              sum = price[num-1] 
              pizza_cost.append(float(sum)*amount)
              x = 0
              for i in pizza_cost:
                x = x +float(i)
              normal_cost.append(x)
              next = input("Do you still want to order?(Y/N):")
              clear_screen()
              
              if next.upper() == "Y":
                  continue
              elif next.upper() == "N":
                  addon()
      
              else:
                  print("Not an option")
                  continue
      elif option.upper() == "N":
        clear_screen()
        user_menu()
      else:
        clear_screen()
        print("Not a valid input")
        continue
      break
  elif option.lower() == "b":
    customize()
  else:
    order()

def customize():
  global NOTIFI
  while True:
        NOTIFI="Customize Menu"
        clear_screen()
        print("\033[1;36mSauces Option:                   Price\033[0m")
        maxlength=30
        i=0
        for show in customize_sauce:
            show=show.ljust(maxlength," ")
            print(f'{i+1} {show}RM{sauceprice[i]}')
            i=i+1
        print("\033[1;36mToppings Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_topping:
            show=show.ljust(maxlength," ")
            print(f'{i+1} {show}RM{toppingprice[i]}')
            i=i+1
        print("\033[1;36mCheese Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_cheese:
            show=show.ljust(maxlength," ")
            print(f'{i+1} {show}RM{cheeseprice[i]}')
            i=i+1
        x = input("Do you want to Order?(Y/N)")
        if x.upper() == "N":
          user_menu()
        elif x.upper() == "Y":
          while True:
            clear_screen()
            print("\033[1;36mTopping Option:                Price\033[0m")
            maxlength=30
            i=0
            for show in customize_topping:
              show=show.ljust(maxlength," ")
              print(f'{i+1} {show}RM{toppingprice[i]}')
              i=i+1
            num = int(input("index of topping you want:"))
            if num > len(customize_topping):
              NOTIFI=("Item doesnt exist")
              continue
            else:
                topping_ordersadding.append(customize_topping[num-1])
                top = toppingprice[num-1]
                topping_costsadding.append(top)
                print(f"{customize_topping[num-1]}      {toppingprice[num-1]}")
                next = input("Do You Want to add other topping?(Y/N)")
                if next.upper() == "Y":  
                  continue
                elif next.upper() == "N":
                  x=0
                  for i in topping_costsadding:
                    x=x+float(i)
                  break
          topping_orders.append(('<').join(topping_ordersadding))
          topping_cost.append(('<').join(topping_costsadding))
          topping_costsadding.clear()
          topping_ordersadding.clear()
                  
          while True:
            clear_screen()
            print("\033[1;36mSauces Option:                Price\033[0m")
            maxlength=30
            i=0
            for show in customize_sauce:
              show=show.ljust(maxlength," ")
              print(f'{i+1} {show}RM{sauceprice[i]}')
              i=i+1
            nums = int(input("index of sauce you want:"))
            if nums > len(customize_sauce):
              NOTIFI=("Item doesnt exist")
              continue
            else:
              sauce_orders.append(customize_sauce[nums-1])
              sauce = sauceprice[nums-1]
              topping_cost.append(sauce)
              print(f"{customize_sauce[nums-1]}      {sauceprice[nums-1]}")
              input("Continue...")
              y=0
              for i in sauce_cost:
                y=y+float(i)
              break
          while True:
            clear_screen()
            print("\033[1;36mCheese Option:                Price\033[0m")
            maxlength=30
            i=0
            for show in customize_cheese:
              show=show.ljust(maxlength," ")
              print(f'{i+1} {show}RM{cheeseprice[i]}')
              i=i+1
            number = int(input("index of cheese you want:"))
            if number > len(customize_cheese):
              NOTIFI=("Item doesnt exist")    
              continue
            else:
              cheese_ordersadding.append(customize_cheese[number-1])
              cheese = cheeseprice[number-1]
              cheese_costsadding.append(cheese)
              print(f"{customize_cheese[number-1]}      {cheeseprice[number-1]}")
              next = input("Do You Want to add other cheese?(Y/N)")
              if next.upper() == "Y":
                continue
              elif next.upper() == "N":
                z=0
                for i in cheese_costsadding:
                    z=z+float(i)
                break
          cheese_orders.append(('<').join(cheese_ordersadding))
          cheese_cost.append(('<').join(cheese_costsadding))
          cheese_costsadding.clear()
          cheese_ordersadding.clear()
          amt = int(input("What is the amount of the pizza you want to order?(only integer)"))
          customize_amount.append(amt)
          sum = float((x+y+z)*amt)
          customize_cost.append(sum)
          addon() 
          break
                              
        else:
          NOTIFI=("Not an valid input")
          continue
        break
  
def addon():
  global NOTIFI,name
  while True:
      clear_screen()
      print("Item                                    Price")
      x = len(addon_food)
      i=0
      maxlength=20
      for var in addon_food:
        var_format = var.ljust(maxlength," ")
        if i < 9 :
           print(f"0{i+1}: {var_format}      RM{addon_price[i]}")
           i= i + 1
        else:
           print(f"{i+1}: {var_format}      RM{addon_price[i]}")
           i = i+1
      
          
      add = input("Do you have anything want to Add-on?(Y/N):")
      if add.upper() == "Y":      
          num = int(input("index:"))
          if num > len(addon_food):
            NOTIFI=("Item doesnt exist")
            clear_screen()
            continue
        
          else:    
            clear_screen()
            addon_order.append(addon_food[num-1])
            print(f"{addon_food[num-1]}      {addon_price[num-1]}")
            amount = int(input("What is the amount of item you want to order:"))
            addon_amount.append(amount)
            addprice = addon_price[num-1]
            addon_cost.append(float(addprice)*amount)
            x=0
            for i in addon_cost:
                x=x + float(i)
            sumaddon.append(x)
            next = input("Do you still want to Add-on?(Y/N):")
            clear_screen()
            if next.upper() == "Y":
              continue
            elif next.upper() == "N":
              clear_screen()
              user_menu()
              break
            else:
              NOTIFI=("Not an option")
              continue

      elif add.upper() == "N":
        user_menu()
        addon_order.append("NO add on")
        break
      else:
        NOTIFI=("Please choose a valid option")
      break
  
def booking_cart():
  global NOTIFI,name
  clear_screen()
  print("🟪\033[1;32mName\033[0;0m",name)
  while True:
    option = input("(a)View | (b)Delete | (c)Edit | (d)Payment | (e)Back:")
    if option.lower() == "a":
        if len(orders) != 0:
            for i in range(len(orders)):
                print("\n🟪 #"+ str(i+1) + "\033[1;32mNormal Pizza:\033[0;0m")
                print((orders[i]).replace(",","\033[1;32m||\033[0;0m"))
                print("\033[1;32mAmount:\033[0;0m", quantity[i])
        else:
            print("Didnt order for any Normal Pizza")
        
        if len(addon_order) != 0:
            for i in range(len(addon_order)):
                print("\n🟪 #"+ str(i+1) + "\033[1;32mAdd-On:\033[0;0m")
                print((addon_order[i]).replace(",","\033[1;32m||\033[0;0m"))
                print("\033[1;32mAmount:\033[0;0m",addon_amount[i])
        else:
            print("Didnt order for any Add-On")

        if len(topping_orders) != 0:
            for i in range(len(topping_orders)):
                print("\n🟪 #"+ str(i+1) + " \033[1;32mCustomize Pizza:\033[0;0m")
                print("\033[0;35mTopping:\033[0m")
                print((topping_orders[i]).replace("<","\033[1;32m||\033[0;0m"))
                print("\n\033[0;35mSauce:\033[0m")
                print((sauce_orders[i]).replace("<","\033[1;32m||\033[0;0m"))
                print("\n\033[0;35mCheese:\033[0m")
                print((cheese_orders[i]).replace("<","\033[1;32m||\033[0;0m"))
                print("\033[0;35mAmount:\033[0m",customize_amount[i])
        else:
            print("Didnt order for any Customize Pizza")
        continue
    elif option.lower() == "b":
        Choose = input("(a)Normal Pizza | (b)Add-On | (c)Customize Pizza | (d) Back:")
        if Choose.lower() == "a":
          if len(orders) != 0:
            while True:
                clear_screen()
                i=0
                maxlength=30
                for var in orders:
                    var_format = var.ljust(maxlength," ")
                    if i < 9 :
                        print(f"0{i+1}: {var_format}      Amount:{quantity[i]}")
                        i= i + 1
                    
                    else:
                        print(f"{i+1}: {var_format}      Amont:{quantity[i]}")
                        i = i+1 
                while True:
                    try:
                        delete = int(input("Input The Index of the order you want to delete(Type any letter to leave):"))                 
                        if delete > len(orders):
                            NOTIFI=("Item doesnt exist")
                            continue
                        else:   
                            orders.remove(orders[delete-1])
                            quantity.remove(quantity[delete-1])
                            normal_cost.remove(normal_cost[delete-1])
                            NOTIFI = "Remove Succesfully"
                            booking_cart() 
                            break  
                    except ValueError:
                        booking_cart()
                        break
                break
          else:
              clear_screen()
              print ("You didnt order for any Normal Pizza")
              continue
        elif Choose.lower() == "b":
          if len(addon_order) != 0:
            while True:
                clear_screen()
                i=0
                maxlength=20
                for var in addon_order:
                    var_format = var.ljust(maxlength," ")
                    if i < 9 :
                        print(f"0{i+1}: {var_format}      Amount:{addon_amount[i]}")
                        i= i + 1
                    else:
                        print(f"{i+1}: {var_format}      Amount:{addon_amount[i]}")
                        i = i+1    
                while True:
                    try:
                        deletes = int(input("Input The Index of the food you want to delete(type letter to leave):"))       
                        if deletes > len(addon_order):
                            NOTIFI=("Item doesnt exist")
                            continue
                        else:  
                            addon_order.remove(addon_order[deletes-1])
                            addon_amount.remove(addon_amount[deletes-1])
                            addon_cost.remove(addon_cost[delete-1])
                            NOTIFI = "Remove Succesfully"
                            booking_cart()
                            break
                    except ValueError:
                        booking_cart()
                        break
                break
          else:
              clear_screen()
              print ("You didnt order for any Add-On")  
              continue
        elif Choose.lower() == "c":
          if len(topping_orders) != 0:
            while True:
                clear_screen()
                for i in range(len(topping_orders)):
                    print("\n🟪 #"+ str(i+1) + " Customize Pizza:")
                    print("Topping:")
                    print((topping_orders[i]).replace("<","\033[1;32m||\033[0;0m"))
                    print("\nSauce:")
                    print((sauce_orders[i]).replace("<","\033[1;32m||\033[0;0m"))
                    print("\nCheese:")
                    print((cheese_orders[i]).replace("<","\033[1;32m||\033[0;0m"))
                    print("amount:",customize_amount[i])
            
                while True:
                    try:
                        deletes = int(input("Input The Index of the Food you want to delete(type letter to leave):"))       
                        if deletes > len(customize_amount):
                            NOTIFI=("Item doesnt exist")
                            continue
                        else:  
                            topping_orders.remove(topping_orders[deletes-1])
                            sauce_orders.remove(sauce_orders[deletes-1])
                            cheese_orders.remove(cheese_orders[deletes-1])
                            customize_amount.remove(customize_amount[deletes-1])
                            customize_cost.remove(customize_cost[deletes-1])
                            NOTIFI = "Remove Succesfully"
                            booking_cart()
                            break
                    except ValueError:
                        booking_cart()
                        break
                break
          else:
              clear_screen()
              print("You didnt order for any customize pizza")  
              continue        
        elif Choose.lower() == "d":
            booking_cart()
        else:
            print("Not an option")
            booking_cart()
                        
              
    elif option.lower() == "c":
        choose = input("(a)Normal Pizza | (b)Add-On | (c)Customize Pizza | (d) Back:")
        if choose.lower() == "a":
          if len(orders) != 0:
            while True:
                clear_screen()
                x = len(orders)
                i=0
                maxlength=30
                for var in orders:
                    var_format = var.ljust(maxlength," ")
                    if i < 9 :
                        print(f"0{i+1}: {var_format}      Amount:{quantity[i]}")
                        i= i + 1
                    else:
                        print(f"{i+1}: {var_format}      Amount:{quantity[i]}")
                        i = i+1 
                while True:
                    try:
                        edit = int(input("Input The Index of the Food to edit the amount(type any letter to leave):"))
                        if edit > len(orders):
                            clear_screen()
                            NOTIFI = "Value not Found"
                            continue
                        else:
                            new_input = int(input("Enter the new value: "))
                            if 0 <= edit < len(quantity)+1:
                                index = edit - 1
                                quantity[index] = new_input
                            NOTIFI = "Edit Succesfully"
                            booking_cart()
                            break
                
                    except ValueError:
                        booking_cart()
                        break
          else:
              clear_screen()
              print ("You didnt order for any Normal pizza")  
              continue           
        elif choose.lower() == "b":
          if len(addon_order) != 0:
            while True:
                clear_screen()
                x = len(addon_order)
                i=0
                maxlength=20
                for var in addon_order:
                    var_format = var.ljust(maxlength," ")
                    if i < 9 :
                        print(f"0{i+1}: {var_format}      Amount:{addon_amount[i]}")
                        i= i + 1
                    else:
                        print(f"{i+1}: {var_format}      Amount:{addon_amount[i]}")
                        i = i+1
                while True:
                    try:
                            edit = int(input("Input The Index of Add-On to edit the amount(type any letter to leave):"))
                            if edit > len(addon_order):
                                NOTIFI=("Item doesnt exist")
                                continue
                            else:
                                new_input = int(input("Enter the new value: "))
                                if 0 <= edit < len(addon_amount)+1:
                                    index = edit - 1
                                    addon_amount[index] = new_input
                                    NOTIFI = "Edit Succesfully"
                                    booking_cart()
                                    break
                    except ValueError :
                            booking_cart()
                            break
          else:
              clear_screen()
              print ("You didnt order for any Add_On pizza")  
              continue                   
        elif choose.lower() == "c":
          if len(topping_orders) != 0:
            while True:
                clear_screen()
                for i in range(len(topping_orders)):
                    print("\n#"+ str(i+1) + " Customize Pizza:")
                    print("Topping:")
                    print((topping_orders[i]).replace("<","\033[1;32m||\033[0;0m"))
                    print("\nSauce:")
                    print((sauce_orders[i]).replace("<","\033[1;32m||\033[0;0m"))
                    print("\nCheese:")
                    print((cheese_orders[i]).replace("<","\033[1;32m||\033[0;0m"))
                    print("\033[1;32mAmount:\033[0;0m",customize_amount[i])
                try:
                    edit = int(input("Input The Index of customize pizza to edit the amount(type any letter to leave):"))
        
                    if edit > len(topping_orders):
                        clear_screen()
                        NOTIFI=("Item doesnt exist")
                        continue
                    else:
                        new_input = int(input("Enter the new value: "))
                        if 0 <= edit < len(customize_amount)+1:
                            index = edit - 1
                            customize_amount[index] = new_input
                            NOTIFI = "Edit Succesfully"
                            booking_cart()
                            break
                except ValueError :
                    booking_cart()
                    break
          else:
              clear_screen()
              print ("You didnt order for any customize pizza")  
              continue           
        elif choose.lower() == "d":
            booking_cart()
            break
        else:
            NOTIFI=("Not an Option")
            booking_cart()
            break

    elif option.lower() == "d":
        payment()
        break
    elif option.lower() == "e":
        clear_screen()
        user_menu()
    else:
        NOTIFI=("Not an Option")
        booking_cart()
        break
    break

def payment():
  global total,NOTIFI
  x = 0 
  y = 0
  z = 0
  for num in normal_cost:
    if isinstance(num, float):
        x += num
  for num in customize_cost:
    if isinstance(num, float):
        y += num
  for num in sumaddon:
    if isinstance(num, float):
        z += num    
  sum = x+y+z
  total.append(sum)
  while True:
    print("🟪Cost of Normal Pizza: RM",x)
    print("🟪Cost of Customize Pizza: RM",y)
    print("🟪Cost of Add-on: RM",z)
    print("Total Cost of orders:   RM",sum)
    p = input("Do you have any promo code?(Y/N)")
    if p.upper() == "Y":
        promo = input("Enter the Promo Code you have:")
        pp=open("promo_code.txt")
        for i in pp:
            a,b=i.split(" ")
            codes.append(a)
            b=b.strip("-%\n")
            discounts.append(b)
            if promo in codes:
                code_index=codes.index(promo)
                discount=float(discounts[code_index])
                totals=sum-(sum * (discount/100))
                print('Total after discount (-',discount,'%): RM',format(totals,".2f"),sep='')
                break
            else:
                print("promo code does not exist")
        break
    elif p.upper() == "N":
        break
    else:
        print("Invalid Input")
        continue    
  pay = input("Do you want to pay for your order now?(Y/N)")
  if ((pay.upper() == "Y") and ((total[0])!=0)):
    x = 0
    y = 0 
    z = 0
    NOTIFI=("Pay Successful")
    with open("orders.txt","a") as file:
      ordersquanti=''
      if len(orders) != 0:
        for i in range(len(orders)):
            ordersquanti+=(str(orders[i])+">"+str(quantity[i])+':')
        ordersquanti=ordersquanti.rstrip(":")
      else:
        ordersquanti="-"


      if len(topping_orders) != 0:
        customizewithhisoption=""
        print(topping_orders,"\n",sauce_orders,"\n",cheese_orders,"\n",customize_amount)
        for i in range(len(topping_orders)):
            customizewithhisoption+=(str(topping_orders[i])+">"+str(sauce_orders[i])+">"+str(cheese_orders[i])+">"+str(customize_amount[i])+':')
        customizewithhisoption=customizewithhisoption.rstrip(":")
      else:
        customizewithhisoption="-"

      if len(addon_order) != 0:
        addsquanti=''
        for i in range(len(addon_order)):
            addsquanti+=(str(addon_order[i])+">"+str(addon_amount[i])+':')
        addsquanti=addsquanti.rstrip(":")
      else:
         addsquanti="-"

      file.write(name+"|"+ordersquanti+"|"+customizewithhisoption+"|"+addsquanti+"|"+str(total)+"\n")
    file.close()
    clear_bookingcart()
    user_menu()
  elif pay.upper() == "N":
    booking_cart()
  else:
    NOTIFI=("Not an valid input")
    booking_cart()

def user_menu():
  global name,NOTIFI
  while True:
    clear_screen()
    print(text_color + "(a)" + reset_color,"Search",text_color + "(b)" +       reset_color,"Order",text_color + "(c)" + reset_color,"Booking Cart",text_color + "(d)" + reset_color,"Profile",text_color + "(else)" + reset_color,"Logout")
    option = input("Type Your Option:")
    print("-" * 60)
    if option.lower() == "a":
        while True:
            searchvalue = input("Food Item Name You Want To Search(Type Q to leave): ")
            if searchvalue.upper() == "Q":
                clear_screen()
                user_menu()
                break
            else:
                search(food,searchvalue)
    elif option.lower() == "b":
        order()
        
    elif option.lower() == "c":
        booking_cart()
        
    elif option.lower() == "d":
        profile()
        
    else:
        NOTIFI=("LOGGED OUT")
        clear_bookingcart()
        break

def clear_bookingcart():
    topping_costsadding.clear()
    topping_ordersadding.clear()
    cheese_costsadding.clear()
    cheese_ordersadding.clear()
    topping_cost.clear()
    sauce_cost.clear()
    cheese_cost.clear()
    topping_orders.clear()
    sauce_orders.clear()
    cheese_orders.clear()
    customize_amount.clear()
    addon_order.clear()
    addon_amount.clear()
    total.clear()
    quantity.clear()
    pizza_cost.clear()
    orders.clear()
    normal_cost.clear()
    customize_cost.clear()
    addon_cost.clear()
    sumaddon.clear()



def profile():
    global NOTIFI,name,password,gmail,phone,birth_day,forgot
    while True:
        clear_screen()
        print("Name: "+name)
        print("\nGmail: "+gmail)
        print("\nPhone: "+phone)
        print("\nBirthday: "+birth_day+"\n")
        print("Promo code                 Percentage(%)")
        maxlength = 30
        i=0
        for show in codes:
          show=show.ljust(maxlength," ")
          print(f' {show}{discounts[i]}')
          i=i+1
        edit=input("'🛠 EDIT'/'🗑 DELETE'/else=🚪 QUIT:")
        if edit.upper() == 'EDIT':
            while True:
                clear_screen()        
                print("Name: "+name)
                print("\nGmail: "+gmail)
                print("\nPhone: "+phone)
                print("\nBirthday: "+birth_day+"\n")
                print("Which part you want to edit?")
                new=input("1.name\n2.password\n3.gmail\n4.phone\n5.birthday\nElse=exit\n\nEnter:")
                if new == '1':
                    confirmpassword=input("Password:")
                    if confirmpassword == password :
                        NOTIFI=('Change NAME')
                        clear_screen()
                        newname=input("Enter your new name:")
                        f = open('database.txt', 'r')
                        file = f.readlines()
                        lineindex = 1
                        editline = 1+username.index(name)
                        f.close()
                        f= open ('database.txt','w')
                        for line in file:
                            if lineindex != editline:
                                f.write(line)
                            else:
                                f.write(newname+','+password+','+gmail+','+phone+','+birth_day+','+forgot+"\n")
                            lineindex = lineindex+1
                            name = newname
                        NOTIFI=('✅ Edit Successful!!!✅')
                        f.close()
                    else :
                        NOTIFI=("Password Incorrect❌") 
                        break
                elif new== '2':
                    confirmpassword=input("Password:")
                    if confirmpassword == password :
                        NOTIFI=('Change PASSWORD')
                        clear_screen()
                        newpassword=input("Enter your new password:")
                        f = open('database.txt', 'r')
                        file = f.readlines()
                        lineindex = 1
                        editline = 1+username.index(name)
                        f.close()
                        f= open ('database.txt','w')
                        for line in file:
                            if lineindex != editline:
                                f.write(line)
                            else:
                                f.write(name+','+newpassword+','+gmail+','+phone+','+birth_day+','+forgot+"\n")
                            lineindex = lineindex+1
                            password=newpassword
                        NOTIFI=('✅ Edit Successful!!!✅')
                        f.close()
                    else :
                        NOTIFI=("Password Incorrect❌") 
                        break
                elif new== '3':
                    confirmpassword=input("Password:")
                    if confirmpassword == password :
                        NOTIFI=('Change GMAIL')
                        while True:
                            clear_screen()
                            newgmail=input("Enter your new gmail:")
                            if '@gmail.com'not in newgmail:
                                NOTIFI=('⚠️ Enter the gmail correctly!!!⚠️ e.g xxxx@gmail.com')
                            else:
                                f = open('database.txt', 'r')
                                file = f.readlines()
                                lineindex = 1
                                editline = 1+username.index(name)
                                f.close()
                                f= open ('database.txt','w')
                                for line in file:
                                    if lineindex != editline:
                                        f.write(line)
                                    else:
                                        f.write(name+','+password+','+newgmail+','+phone+','+birth_day+','+forgot+"\n")
                                    lineindex = lineindex+1
                                    gmail=newgmail
                                NOTIFI=('✅ Edit Successful!!!✅')
                                f.close()
                                break
                    else :
                        NOTIFI=("Password Incorrect❌") 
                        break
                elif new== '4':
                    confirmpassword=input("Password:")
                    if confirmpassword == password :
                        NOTIFI=('Change PHONE NUMBER')
                        while True:
                            clear_screen()
                            try:
                                newphone=int(input("Enter your new phone(0123456789):"))
                                newphone=str(newphone)
                                if len(newphone) != (9 or 10):
                                    NOTIFI=('⚠️ Length for phone no. is not enough or too much!!!⚠️')
                                    continue
                                else:
                                    break
                            except ValueError:
                                continue
                        f = open('database.txt', 'r')
                        file = f.readlines()
                        lineindex = 1
                        editline = 1+username.index(name)
                        f.close()
                        f= open ('database.txt','w')
                        for line in file:
                            if lineindex != editline:
                                f.write(line)
                            else:
                                f.write(name+','+password+','+gmail+',0'+newphone+','+birth_day+','+forgot+"\n")
                            lineindex = lineindex+1
                            phone=newphone
                        NOTIFI=('✅ Edit Successful!!!✅')
                        f.close()
                    else :
                        NOTIFI=("Password Incorrect❌") 
                        break
                elif new== '5':
                    confirmpassword=input("Password:")
                    if confirmpassword == password :
                        NOTIFI=('Change BIRTHDAY')
                        clear_screen()
                        birthday=int(input("Enter your birthday(e.g DDMMYYYY):"))
                        f = open('database.txt', 'r')
                        file = f.readlines()
                        lineindex = 1
                        editline = 1+username.index(name)
                        f.close()
                        f= open ('database.txt','w')
                        for line in file:
                            if lineindex != editline:
                                f.write(line)
                            else:
                                f.write(name+','+password+','+gmail+','+phone+','+str(birthday)+','+forgot+"\n")
                            lineindex = lineindex+1
                            birth_day=birthday
                        NOTIFI=('✅ Edit Successful!!!✅')
                        f.close()
                    else :
                        NOTIFI=("Password Incorrect❌") 
                        break
                else:
                    break
        elif edit.upper() == 'DELETE':
            while True:
                clear_screen()
                confirmpassword=input('Password: ')
                if confirmpassword == password :
                    print("Are you sure to DELETE your account?")
                    confirm=input("YES/NO :")
                    if confirm =="YES":
                        f = open('database.txt', 'r')
                        file = f.readlines()
                        lineindex = 1
                        deleteline = 1+username.index(name)
                        f.close()
                        f= open ('database.txt','w')
                        for line in file:
                            if lineindex != deleteline:
                                f.write(line)
                            lineindex = lineindex+1
                        NOTIFI=('✅ DELETE Successful!!!✅')
                        f.close()
                        main()
                    elif confirm.upper() =="NO":
                       return
                    else:
                       print('Invalid Option....')
                       input("Press Enter to continue...")
                       return
                else:
                    NOTIFI=("Password Incorrect❌") 
                    break          
        else:
            break

def admin_menu():
    global NOTIFI
    while True:
        NOTIFI="Admin Main Menu"
        clear_screen()
        print("\n\033[1;1mDo you want Go| 🟪 Promo Code 🟪 Check 🟪 Menu 🟪 Create Admin Account")
        print("Enter \n1=🟪 Promo Code \n2=🟪 Check \n3=🟪 Menu \n4=🟪 Create Admin Account\nElse=🟧 Exit")
        adminmenuask = input('\nEnter: \033[0m')
        if adminmenuask == "1":
            promo_code()
        elif adminmenuask == "2":
            check()
        elif adminmenuask == "3":
            adminmenu()
        elif adminmenuask == "4":
            admin_signup()
        else:
            break


#loyalty
def check():
    global NOTIFI
    while True:
      clear_screen()
      print("\n1= Check User's Information\n2= Check Orders\nelse=exit")
      ask=input('Enter')
      if ask == '1':
        check_user_info()
      elif ask =="2":
        check_orders()
      else:
        break
      
def check_user_info():
  global NOTIFI,name,gmail,phone,birth_day
  NOTIFI="Check User's Information"
  while True:
    clear_screen()
    print("Users:")
    for show in username:
       print(f' {show}')
    print('Enter the username to check his info \n"exit"=exit')
    checkname=input('Username (full name): ')
    if checkname in username:
      NOTIFI= "Checking "+checkname
      clear_screen()
      print(checkname,"\n")
      name = checkname
      reload()
      print("\nGmail: "+gmail)
      print("\nPhone: "+phone)
      print("\nBirthday: "+birth_day+"\n")
      input("\nEnter any things to leave...")
    elif checkname.lower()=="exit":
      break
    else:
      NOTIFI='User not found.'

def promo_code():
  global NOTIFI
  clear_screen()
  print("Codes:                     Points:")
  maxlength=30
  i=0
  for show in codes:
   show=show.ljust(maxlength," ")
   print(f' {show}{discounts[i]}')
   i=i+1
  print('Do you want to create or remove promo code?')
  createremove = input("Enter 'create'/'remove'/'else'=exit: ")
  if createremove.lower() == "create":
    clear_screen()
    print("Codes:                     Points:")
    maxlength=30
    i=0
    for show in codes:
      show=show.ljust(maxlength," ")
      print(f' {show}{discounts[i]}')
      i=i+1
    code_admin = str(input("Enter new promo code to be created:"))
    while True:
      while True:
        try:
          discount_admin_type = float(
            input("Set the percentage for discount: "))
          break
        except ValueError:
          print('Please Enter NUMBER!')
      if discount_admin_type > 100:
        NOTIFI = 'Discount cannot over 100%'
        break
      elif discount_admin_type <= 0:
        NOTIFI = 'Discount cannot leeser than 0%'
        break
      else:
        break
    discount_admin = str(discount_admin_type)
    while True:
      if '%' in discount_admin:
        break
      else:
        discount_admin = '-' + discount_admin + '%'
    if code_admin in codes:
      NOTIFI = ' ⚠️ This promo code already exists ⚠️ '
      promo_code()
    else:
      f = open('promo_code.txt', 'a')
      f.write(code_admin + ' ' + discount_admin + '\n')
      NOTIFI = 'Done!The promo code is created.✅'
      f.close()
      promo_code()
  if createremove.lower() == 'remove':
    clear_screen()
    for show in codes:
      print(f'🏷 {show}')
    coderemove = input('Enter the code that you want to remove: ')
    if coderemove in codes:
      f = open('promo_code.txt', 'r')
      file = f.readlines()
      lineindex = 1
      deleteline = 1 + codes.index(coderemove)
      f = open('promo_code.txt', 'w')
      for line in file:
        if lineindex != deleteline:
          f.write(line)
        lineindex = lineindex + 1
      NOTIFI = 'REMOVED!!'
      f.close()
      promo_code()
    else:
      NOTIFI = '❗️Promo code not found ❗️'
  else:
    return

#menu_admin part
#Admin Menu #ENTER
def adminmenu():
    global NOTIFI
    while True:
        NOTIFI="Admin Menu"
        clear_screen()
        print("\n\033[1;1mDo you want Go| 🟪 Food Item 🟪 Add-on 🟪 Customize |Menu?")
        print("Enter \n1=🟪 Food Item \n2=🟪 Add-on \n3=🟪 Customize \nElse=🟧 Exit")
        adminmenuask = input('\nEnter: \033[0m')
        if adminmenuask == "1":
            foodmenu_adminmenu()
        elif adminmenuask == "2":
            addon_adminmenu()
        elif adminmenuask == "3":
            customize_adminmenu()
        else:
            break

#Food Item part
def foodmenu_adminmenu():
    global NOTIFI
    while True:
        NOTIFI="Food Menu Admin"
        clear_screen()
        print("Item:                            Price:    Details:")
        maxlength=30
        i=0
        for show in food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{price[i]}    {details[i]}')
            i=i+1
        print("\033[1;1mDo you want 🟥 Delete 🟩 Create 🟦 Update Food Menu?")
        print("Enter \n1=🟥 Delete \n2=🟩 Create \n3=🟦 Edit \nElse=🟧 Exit")
        adminmenuask = input('\nEnter: \033[0m')
        if adminmenuask == "1":
            delete_adminmenu()
        elif adminmenuask == "2":
            create_adminmenu()
        elif adminmenuask == "3":
            update_adminmenu()
        else:
            break

def search(food,searchvalue):
    global NOTIFI
    NOTIFI="SEARCHING......"
    item=0
    clear_screen()
    maxlength=30
    for i in food:
        i=i.ljust(maxlength," ")
        if searchvalue in i:
            print(f'🟩 {i}RM{price[item]} {details[item]}')
            item=item+1
    if item==0:
        print("\033[1;1m!Does Not Exist!\nCANNOT FOUND!\033[0m")

def create_adminmenu():
    global NOTIFI
    while True:
        NOTIFI="Create Food Item"
        clear_screen()
        print("Item:                             Price:    Details:")
        maxlength=30
        i=0
        for show in food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{price[i]}    {details[i]}')
            i=i+1
        print("\n\033[1;1mEnter: \n1=🟩 Create \n2=🟨 Check Item Exist or Not (search by name)")
        ask=input('Enter "1" or "2" \nelse is Exit: \033[0m' )

        if ask == "1":
            createitem_adminmenu()
            break

        elif ask == "2":
            clear_screen()
            print("Item:                            Price:    Details:")
            maxlength=30
            i=0
            for show in food:
                show=show.ljust(maxlength," ")
                print(f'🟪 {show}RM{price[i]}    {details[i]}')
                i=i+1
            while True:
                print("\033[1;1mSearch by Food Item Name")
                print("\n 🟨 'Food Item Name'=search \n 🟧 'exit'=exit \n 🟩 'create'=create\033[0m")
                searchvalue = input("Enter: ")
                clear_screen()
                if searchvalue.lower() == "exit":
                    break
                elif searchvalue.lower() == "create":
                    createitem_adminmenu()
                    break
                else:
                    search(food, searchvalue)
        else:
            break

def createitem_adminmenu():
    global NOTIFI
    NOTIFI="Create Food Item"
    while True:
        clear_screen()
        print("Item:                            Price:    Details:")
        maxlength=30
        i=0
        for show in food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{price[i]}    {details[i]}')
            i=i+1
        print("\n\033[1;1m Create New Food Item")
        print('Type "exit"=exit (in Name:)')
        newfooditemname = input("Name: \033[0m")
        if newfooditemname.lower() == "exit":
            break
        elif len(newfooditemname) >= 30:
            NOTIFI="The Food Item Name is TOO LONG"
            continue
        elif newfooditemname in food:
            NOTIFI="This Food Item Already Exists"
            continue
        else:
            while True:
                try:
                    newfooditemprice= float(input("Price(RM): "))
                    newfooditemprice= str(newfooditemprice) #because float cannot concatenating with other string It will show TypeError
                    break
                except ValueError:
                    NOTIFI="Please Insert Number"
                    clear_screen()
                    print("Item:                            Price:    Details:")
                    maxlength=30
                    i=0
                    for show in food:
                        show=show.ljust(maxlength," ")
                        print(f'🟪 {show}RM{price[i]}    {details[i]}')
                        i=i+1
                    print("\nName: ",newfooditemname,sep="")
            while True:
                newfooditemdetail=input('Details(cannot contains ","):')
                if ',' in newfooditemdetail:
                    NOTIFI='Details cannot contains ","'
                    clear_screen()
                    print("Item:                            Price:    Details:")
                    maxlength=30
                    i=0
                    for show in food:
                        show=show.ljust(maxlength," ")
                        print(f'🟪 {show}RM{price[i]}    {details[i]}')
                        i=i+1
                    print("\\033[1;1mnNew Item Name: ",newfooditemname,"\nNew Item Price",newfooditemprice,"\033[1;1m",sep="")
                else:
                    break
            NOTIFI="New Food Item is Created"
            f=open('menu.txt','a')
            f.write(newfooditemname+','+newfooditemprice+','+newfooditemdetail+'\n')
            f.close()
            continue

def delete_adminmenu():
    global NOTIFI
    NOTIFI="Delete Food Item"
    clear_screen()
    print("Item:                            Price:    Details:")
    maxlength=30
    i=0
    for show in food:
        show=show.ljust(maxlength," ")
        print(f'🟪 {show}RM{price[i]}    {details[i]}')
        i=i+1
    while True:
        print("\n\033[1;1mSearch by Food Item Name")
        print(" 🟨 'Food Item Name'=search \n 🟧 'exit'=exit \n 🟥 'delete'=delete")
        searchvalue = input("Enter: \033[0m")
        clear_screen()
        if searchvalue.lower() == "exit":
            break
        elif searchvalue.lower() == "delete":
            deleteitem_adminmenu()
            break
        else:
            search(food, searchvalue)

def deleteitem_adminmenu():
    global NOTIFI
    NOTIFI="Delete Food Item"
    while True:
        clear_screen()
        print("Item:                            Price:    Details:")
        maxlength=30
        i=0
        for show in food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{price[i]}    {details[i]}')
            i=i+1
        print("\n\033[1;1mDelete Food Item \n(no need to insert 'pizza')\n(full name)")
        print("\n 🟥 'Name'=delete \n 🟧 'exit'=exit ")
        deleteitemname = input("Name: \033[0m")
        print('\033[1;1mYou Sure want to DELETE',deleteitemname,'?\033[0m')
        if deleteitemname in food:
            while True:
                confirm=input("yes/no:")
                if confirm.lower() =='yes':
                    break
                elif confirm.lower() =='no':
                    return
                else:
                    print('"yes"/"no"')
            NOTIFI=(deleteitemname+" pizza DELETED")
            f = open('menu.txt', 'r')
            file = f.readlines()
            lineindex = 1
            deleteline = 1+food.index(deleteitemname)
            f.close()
            f= open ('menu.txt','w')
            for line in file:
                if lineindex != deleteline:
                    f.write(line)
                lineindex = lineindex+1
            f.close()
        elif deleteitemname.lower() == 'exit':
            break
        else:
            NOTIFI='⚠️  Food Item Not Found ⚠️'

def update_adminmenu():
    global NOTIFI
    while True:
        NOTIFI="Update Food Menu"
        clear_screen()
        print("Item:                            Price:    Details:")
        maxlength=30
        i=0
        for show in food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{price[i]}    {details[i]}')
            i=i+1
    
        print("\n\033[1;1mEnter: \n1=🟦 Edit Food Item\n2=🟨 Check Food Item Exist or Not (search by name)")
        ask=input('Enter "1"\"2"\nelse is Exit: \033[0m' )

        if ask == "1":
            updateitem_adminmenu()
        elif ask == "2":
            clear_screen()
            print("Item:                            Price:    Details:")
            maxlength=30
            i=0
            for show in food:
                show=show.ljust(maxlength," ")
                print(f'🟪 {show}RM{price[i]}    {details[i]}')
                i=i+1
            while True:
                print("\033[1;1mSearch by Food Item Name")
                print("\n 🟨 'Food Item Name'=search \n 🟧 'exit'=exit \n 🟦 'edit'=Edit Food Menu")
                searchvalue = input("Enter: \033[0m")
                clear_screen()
                if searchvalue.lower() == "exit":
                    break
                elif searchvalue.lower() == "edit":
                    updateitem_adminmenu()
                    break
                else:
                    search(food, searchvalue)
        else:
            break

def updateitem_adminmenu():
    global NOTIFI
    NOTIFI="Update Food Item"
    while True:
        clear_screen()
        print("Item:                            Price:    Details:")
        maxlength=30
        i=0
        for show in food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{price[i]}    {details[i]}')
            i=i+1
        print("\n\033[1;1mEdit Food Item \n(no need to insert 'pizza')\n(full name)")
        print("\n 🟦 'Name'=edit \n 🟧 'exit'=exit ")
        edititemname = input("\nName: \033[0m")
        if edititemname in food:
            while True:
                try:
                    while True:
                        editnewname=input('New Name: ')
                        if editnewname in food:
                            NOTIFI="This Food Item Already Exists"
                            continue
                        elif len(editnewname) >= 30:
                            NOTIFI="The Food Item Name is TOO LONG"
                            continue
                        else:
                            break
                    edititemprice= float(input("Price(RM): "))
                    edititemprice= str(edititemprice)
                    break
                except ValueError:
                    NOTIFI="Please Insert Number"
                    clear_screen()
                    print("Item:                            Price:    Details:")
                    maxlength=30
                    i=0
                    for show in food:
                        show=show.ljust(maxlength," ")
                        print(f'🟪 {show}RM{price[i]}    {details[i]}')
                        i=i+1
                    print("\n\033[1;1mEDITING: ",edititemname," pizza\033[0m",sep="")
            while True:
                editfooditemdetail=input('\033[1;1mDetails(cannot contains ","):\033[0m')
                if ',' in editfooditemdetail:
                    NOTIFI='Details cannot contains ","'
                    clear_screen()
                    print("Item:                            Price:    Details:")
                    maxlength=30
                    i=0
                    for show in food:
                        show=show.ljust(maxlength," ")
                        print(f'🟪 {show}RM{price[i]}    {details[i]}')
                        i=i+1
                    print("\n\033[1;1mNew edit Name: ",editnewname,"\nNew edit Price\033[0m",edititemprice,sep="")
                else:
                    break
            NOTIFI=(edititemname+" pizza UPDATED")
            f = open('menu.txt', 'r')
            file = f.readlines()
            lineindex = 1
            editline = 1+food.index(edititemname)
            f.close()
            f= open ('menu.txt','w')
            for line in file:
                if lineindex != editline:
                    f.write(line)
                else:
                    f.write(editnewname+','+edititemprice+','+editfooditemdetail+'\n')
                lineindex = lineindex+1
            f.close()
        elif edititemname.lower() == 'exit':
            break
        else:
            NOTIFI='⚠️  Food Item Not Found ⚠️'

#Add-on part
def addon_adminmenu():
    global NOTIFI
    while True:
        NOTIFI="Add-on Menu"
        clear_screen()
        print("Add-on:                          Price:")
        maxlength=30
        i=0
        for show in addon_food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{addon_price[i]}')
            i=i+1
        print("\n\033[1;1mEnter: \n1=🟩 Create \n2=🟥 Delete\n3=🟦 Edit\nelse:🟧 Exit")
        ask=input('Enter "1"\"2"\"3"\nelse is Exit: \033[0m' )
        if ask == "1":
            createaddon_adminmenu()
        elif ask == "2":
            deleteaddon_adminmenu()
        elif ask=="3":
            updateaddon_adminmenu()
        else:
            break

def createaddon_adminmenu():
    global NOTIFI
    NOTIFI="Create Add-on"
    while True:
        clear_screen()
        print("Add-on:                          Price:")
        maxlength=30
        i=0
        for show in addon_food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{addon_price[i]}')
            i=i+1
        print("\n\033[1;1m Create New Add-on")
        print('Type "exit"=exit (in Name:)')
        newaddonname = input("Name: \033[0m")
        if newaddonname.lower() == "exit":
            break
        elif newaddonname in addon_food:
            NOTIFI="This Add-on Already Exists"
            continue
        elif len(newaddonname) >= 30:
            NOTIFI="The Add-on Name is TOO LONG"
            continue
        else:
            while True:
                try:
                    newaddonprice= float(input("Price(RM): "))
                    newaddonprice= str(newaddonprice)
                    break
                except ValueError:
                    NOTIFI="Please Insert Number"
                    clear_screen()
                    print("Add-on:                          Price:")
                    maxlength=30
                    i=0
                    for show in addon_food:
                        show=show.ljust(maxlength," ")
                        print(f'🟪 {show}RM{addon_price[i]}')
                        i=i+1
                    print("\nName: ",newaddonname,sep="")
            NOTIFI="New Add-on is Created"
            f=open('addon.txt','a')
            f.write(newaddonname+','+newaddonprice+'\n')
            f.close()
            continue

def deleteaddon_adminmenu():
    global NOTIFI
    NOTIFI="Delete Add-on"
    while True:
        clear_screen()
        print("Add-on:                          Price:")
        maxlength=30
        i=0
        for show in addon_food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{addon_price[i]}')
            i=i+1
        print("\n\033[1;1mDelete Add-on \n(full name)")
        print("\n 🟥 'Name'=delete \n 🟧 'exit'=exit ")
        deleteitemname = input("Name: \033[0m")
        if deleteitemname in addon_food:
            while True:
                confirm=input("yes/no:")
                if confirm.lower() =='yes':
                    break
                elif confirm.lower() =='no':
                    return
                else:
                    print('"yes"/"no"')
            NOTIFI=(deleteitemname+" Add-on DELETED")
            f = open('addon.txt', 'r')
            file = f.readlines()
            lineindex = 1
            deleteline = 1+addon_food.index(deleteitemname)
            f.close()
            f= open ('addon.txt','w')
            for line in file:
                if lineindex != deleteline:
                    f.write(line)
                lineindex = lineindex+1
            f.close()
        elif deleteitemname.lower() == 'exit':
            break
        else:
            NOTIFI='⚠️  Add-on Not Found ⚠️'

def updateaddon_adminmenu():
    global NOTIFI
    NOTIFI="Update Add-on"
    while True:
        clear_screen()
        print("Add-on:                          Price:")
        maxlength=30
        i=0
        for show in addon_food:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{addon_price[i]}')
            i=i+1
        print("\n\033[1;1mEdit Add-on \n(full name)")
        print("\n 🟦 'Name'=edit \n 🟧 'exit'=exit ")
        editaddonname = input("\nName: \033[0m")
        if editaddonname in addon_food:
            while True:
                try:
                    while True:
                        editnewname=input('New Name: ')
                        if len(editnewname) >= 30:
                            NOTIFI="The Add-on Name is TOO LONG"
                            continue
                        elif editnewname in addon_food:
                            NOTIFI="This Add-on Already Exists"
                            continue
                        else:
                            break
                    editaddonprice= float(input("Price(RM): "))
                    editaddonprice= str(editaddonprice)
                    break
                except ValueError:
                    NOTIFI="Please Insert Number"
                    clear_screen()
                    print("Add-on:                          Price:")
                    maxlength=30
                    i=0
                    for show in addon_food:
                        show=show.ljust(maxlength," ")
                        print(f'🟪 {show}RM{addon_price[i]}')
                        i=i+1
                    print("\n\033[1;1mEDITING: \033[0m",editaddonname,sep="")
            NOTIFI=(editaddonname+" UPDATED to "+editnewname)
            f = open('addon.txt', 'r')
            file = f.readlines()
            lineindex = 1
            editline = 1+addon_food.index(editaddonname)
            f.close()
            f= open ('addon.txt','w')
            for line in file:
                if lineindex != editline:
                    f.write(line)
                else:
                    f.write(editnewname+','+editaddonprice+'\n')
                lineindex = lineindex+1
            f.close()
        elif editaddonname.lower() == 'exit':
            break
        else:
            NOTIFI='⚠️  Add-on Not Found ⚠️'


#Customize part
def customize_adminmenu():
    global NOTIFI
    while True:
        NOTIFI="Customize Menu"
        clear_screen()
        print("\033[1;36mSauces Option:                   Price\033[0m")
        maxlength=30
        i=0
        for show in customize_sauce:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{sauceprice[i]}')
            i=i+1
        print("\033[1;36mToppings Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_topping:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{toppingprice[i]}')
            i=i+1
        print("\033[1;36mCheese Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_cheese:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{cheeseprice[i]}')
            i=i+1
        print("\n\033[1;1mEnter: \n1=🟩 Create \n2=🟥 Delete\n3=🟦 Edit\nelse:🟧 Exit")
        ask=input('Enter "1"\"2"\"3"\nelse is Exit: \033[0m' )
        if ask == "1":
            createcustom_adminmenu()
        elif ask == "2":
            deletecustom_adminmenu()
        elif ask=="3":
            updatecustom_adminmenu()
        else:
            break

def createcustom_adminmenu():
    global NOTIFI
    while True:
        NOTIFI="Create Option"
        clear_screen()
        print("\033[1;36mSauces Option:                   Price\033[0m")
        maxlength=30
        i=0
        for show in customize_sauce:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{sauceprice[i]}')
            i=i+1
        print("\033[1;36mToppings Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_topping:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{toppingprice[i]}')
            i=i+1
        print("\033[1;36mCheese Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_cheese:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{cheeseprice[i]}')
            i=i+1
        print("\n \033[1;1mCreate New Option For Customize")
        print("\nEnter: \n1=🟩 Sauce Option \n2=🟩 Toppings Option\n3=🟩 Cheese Option\nelse:🟧 Exit")
        ask=input("Enter:\033[0m")
        if ask == "1":
            NOTIFI='Sauce Option'
            while True:
                clear_screen()
                print("\033[1;36mSauces Option:                   Price\033[0m")
                maxlength=30
                i=0
                for show in customize_sauce:
                    show=show.ljust(maxlength," ")
                    print(f'🟪 {show}RM{sauceprice[i]}')
                    i=i+1
                print("\n\033[1;1m Create New Option For Customize")
                print('Type "exit"=exit (in Option:)')
                newoptionname = input("Option: \033[0m")
                if newoptionname.lower() == "exit":
                    break
                elif newoptionname in customize_sauce:
                    NOTIFI="This Option Already Exists"
                    continue
                else:
                    while True:
                        try:
                            newoptionprice= float(input("Price(RM): "))
                            newoptionprice= str(newoptionprice)
                            break
                        except ValueError:
                            NOTIFI="Please Insert Number"
                            clear_screen()
                            print("\033[1;36mSauces Option:                   Price\033[0m")
                            maxlength=30
                            i=0
                            for show in customize_sauce:
                                show=show.ljust(maxlength," ")
                                print(f'🟪 {show}RM{sauceprice[i]}')
                                i=i+1
                            print("\n\033[1;1mNew Sauce Name: \033[0m",newoptionname,sep="")
                    NOTIFI="New Sauce Option is Created"
                    f=open('customize.txt','r')
                    newwritein=f.readlines()
                    customize_sauce.append(newoptionname)
                    sauceprice.append(newoptionprice)
                    updatesauceline=":".join([f"{customize_sauce[index]},{sauceprice[index]}" for index in range(len(customize_sauce))])
                    newwritein[0]=updatesauceline+'\n'
                    f=open('customize.txt','w')
                    f.writelines(newwritein)
                    f.close()
                    continue
        elif ask == "2":
            NOTIFI='Toppings Option'
            while True:
                clear_screen()
                print("\033[1;36mToppings Option:                   Price\033[0m")
                maxlength=30
                i=0
                for show in customize_topping:
                    show=show.ljust(maxlength," ")
                    print(f'🟪 {show}RM{toppingprice[i]}')
                    i=i+1
                print("\n\033[1;1m Create New Option For Customize")
                print('Type "exit"=exit (in Option:)')
                newoptionname = input("Option: \033[0m")
                if newoptionname.lower() == "exit":
                    break
                elif newoptionname in customize_topping:
                    NOTIFI="This Option Already Exists"
                    continue
                else:
                    while True:
                        try:
                            newoptionprice= float(input("Price(RM): "))
                            newoptionprice= str(newoptionprice)
                            break
                        except ValueError:
                            NOTIFI="Please Insert Number"
                            clear_screen()
                            print("\033[1;36mToppings Option:                   Price\033[0m")
                            maxlength=30
                            i=0
                            for show in customize_topping:
                                show=show.ljust(maxlength," ")
                                print(f'🟪 {show}RM{toppingprice[i]}')
                                i=i+1
                            print("\n\033[1;1mNew Topping Name: \033[0m",newoptionname,sep="")
                    NOTIFI="New Topping Option is Created"
                    f=open('customize.txt','r')
                    newwritein=f.readlines()
                    customize_topping.append(newoptionname)
                    toppingprice.append(newoptionprice)
                    updatetoppingline=":".join([f"{customize_topping[index]},{toppingprice[index]}" for index in range(len(customize_topping))])
                    newwritein[1]=updatetoppingline+'\n'
                    f=open('customize.txt','w')
                    f.writelines(newwritein)
                    f.close()
                    continue
        elif ask == "3":
            NOTIFI='Cheese Option'
            while True:
                clear_screen()
                print("\033[1;36mCheese Option:                   Price\033[0m")
                maxlength=30
                i=0
                for show in customize_cheese:
                    show=show.ljust(maxlength," ")
                    print(f'🟪 {show}RM{cheeseprice[i]}')
                    i=i+1
                print("\n\033[1;1m Create New Option For Customize")
                print('Type "exit"=exit (in Option:)')
                newoptionname = input("Option: \033[0m")
                if newoptionname.lower() == "exit":
                    break
                elif newoptionname in customize_cheese:
                    NOTIFI="This Option Already Exists"
                    continue
                else:
                    while True:
                        try:
                            newoptionprice= float(input("Price(RM): "))
                            newoptionprice= str(newoptionprice)
                            break
                        except ValueError:
                            NOTIFI="Please Insert Number"
                            clear_screen()
                            print("\033[1;36mCheese Option:                   Price\033[0m")
                            maxlength=30
                            i=0
                            for show in customize_cheese:
                                show=show.ljust(maxlength," ")
                                print(f'🟪 {show}RM{cheeseprice[i]}')
                                i=i+1
                            print("\n\033[1;1mNew Cheese Name: \033[0m",newoptionname,sep="")
                    NOTIFI="New Cheese Option is Created"
                    f=open('customize.txt','r')
                    newwritein=f.readlines()
                    customize_cheese.append(newoptionname)
                    cheeseprice.append(newoptionprice)
                    updatecheeseline=":".join([f"{customize_cheese[index]},{cheeseprice[index]}" for index in range(len(customize_cheese))])
                    newwritein[2]=updatecheeseline+'\n'
                    f=open('customize.txt','w')
                    f.writelines(newwritein)
                    f.close()
                    continue
        else:
            break

def deletecustom_adminmenu():
    global NOTIFI
    while True:
        NOTIFI="Delete Option"
        clear_screen()
        print("\033[1;36mSauces Option:                   Price\033[0m")
        maxlength=30
        i=0
        for show in customize_sauce:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{sauceprice[i]}')
            i=i+1
        print("\033[1;36mToppings Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_topping:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{toppingprice[i]}')
            i=i+1
        print("\033[1;36mCheese Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_cheese:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{cheeseprice[i]}')
            i=i+1
        print("\n\033[1;1m Delete Option For Customize")
        print("\nEnter: \n1=🟥 Sauce Option \n2=🟥 Toppings Option\n3=🟥 Cheese Option\nelse:🟧 Exit")
        ask=input("Enter: \033[0m")
        if ask == '1':
            NOTIFI='Sauce Option'
            while True:
                clear_screen()
                print("\033[1;36mSauces Option:                   Price\033[0m")
                maxlength=30
                i=0
                for show in customize_sauce:
                    show=show.ljust(maxlength," ")
                    print(f'🟪 {show}RM{sauceprice[i]}')
                    i=i+1
                print("\n\033[1;1m Delete an Option For Customize")
                print('Type "exit"=exit (in Option:)')
                deleteoptionname = input("Option: \033[0m")
                if deleteoptionname.lower() == "exit":
                    break
                elif deleteoptionname in customize_sauce:
                    while True:
                        confirm=input("yes/no:")
                        if confirm.lower() =='yes':
                            break
                        elif confirm.lower() =='no':
                            return
                        else:
                            print('"yes"/"no"')
                    NOTIFI=(deleteoptionname+" This Option DELETED")
                    f = open('customize.txt', 'r')
                    deletewritein=f.readlines()
                    deleteindex=customize_sauce.index(deleteoptionname)
                    customize_sauce.pop(deleteindex)
                    sauceprice.pop(deleteindex)
                    updatesauceline=":".join([f"{customize_sauce[index]},{sauceprice[index]}" for index in range(len(customize_sauce))])
                    deletewritein[0]=updatesauceline+'\n'
                    f=open('customize.txt','w')
                    f.writelines(deletewritein)
                    f.close()
                    continue
                else:
                    NOTIFI='⚠️  Option Not Found ⚠️'
        elif ask == '2':
            NOTIFI='Toppings Option'
            while True:
                clear_screen()
                print("\033[1;36mTopping Option:                 Price\033[0m")
                maxlength=30
                i=0
                for show in customize_topping:
                    show=show.ljust(maxlength," ")
                    print(f'🟪 {show}RM{toppingprice[i]}')
                    i=i+1
                print("\n\033[1;1m Delete an Option For Customize")
                print('Type "exit"=exit (in Option:)')
                deleteoptionname = input("Option: \033[0m")
                if deleteoptionname.lower() == "exit":
                    break
                elif deleteoptionname in customize_topping:
                    while True:
                        confirm=input("yes/no:")
                        if confirm.lower() =='yes':
                            break
                        elif confirm.lower() =='no':
                            return
                        else:
                            print('"yes"/"no"')
                    NOTIFI=(deleteoptionname+" This Option DELETED")
                    f = open('customize.txt', 'r')
                    deletewritein=f.readlines()
                    deleteindex=customize_topping.index(deleteoptionname)
                    customize_topping.pop(deleteindex)
                    toppingprice.pop(deleteindex)
                    updatetoppingline=":".join([f"{customize_topping[index]},{toppingprice[index]}" for index in range(len(customize_topping))])
                    deletewritein[1]=updatetoppingline+'\n'
                    f=open('customize.txt','w')
                    f.writelines(deletewritein)
                    f.close()
                    continue
                else:
                    NOTIFI='⚠️  Option Not Found ⚠️'
        elif ask == '3':
            NOTIFI='Cheese Option'
            while True:
                clear_screen()
                print("\033[1;36mCheese Option:                   Price\033[0m")
                maxlength=30
                i=0
                for show in customize_cheese:
                    show=show.ljust(maxlength," ")
                    print(f'🟪 {show}RM{cheeseprice[i]}')
                    i=i+1
                print("\n\033[1;1m Delete an Option For Customize")
                print('Type "exit"=exit (in Option:)')
                deleteoptionname = input("Option: \033[0m")
                if deleteoptionname.lower() == "exit":
                    break
                elif deleteoptionname in customize_cheese:
                    while True:
                        confirm=input("yes/no:")
                        if confirm.lower() =='yes':
                            break
                        elif confirm.lower() =='no':
                            return
                        else:
                            print('"yes"/"no"')
                    NOTIFI=(deleteoptionname+" This Option DELETED")
                    f = open('customize.txt', 'r')
                    deletewritein=f.readlines()
                    deleteindex=customize_cheese.index(deleteoptionname)
                    customize_cheese.pop(deleteindex)
                    cheeseprice.pop(deleteindex)
                    updatecheeseline=":".join([f"{customize_cheese[index]},{cheeseprice[index]}" for index in range(len(customize_cheese))])
                    deletewritein[2]=updatecheeseline+'\n'
                    f=open('customize.txt','w')
                    f.writelines(deletewritein)
                    f.close()
                    continue
                else:
                    NOTIFI='⚠️  Option Not Found ⚠️'
        else:
            break

def check_orders():
   global NOTIFI
   NOTIFI="Check Orders"
   while True:
      clear_screen()
      for i in range(len(users)):
         if i < 9:
            print(f'0{i+1}: {users[i]}')
         else:
            print(f'{i+1}: {users[i]}')
      print('\nEnter the order index to check the order \n"exit"=exit')
      checkindex=input('Index: ')
      if checkindex.lower()=="exit":
        break
      elif int(checkindex) <= len(users):
        NOTIFI= ("Checking '"+checkindex+"' order")
        clear_screen()
        f=open("orders.txt","r")
        linecount=1
        for i in f:
           if int(checkindex) == linecount:
              variables=i.split('|')
              print(f'Name:{variables[0]}')
              variables_normalpizza=variables[1].split(':')
              print('\nNormal Pizza:Amount')
              for show in variables_normalpizza:
                 print(f'{(show).replace(">"," :")}')
              variables_custompizza=variables[2].split(':')
              print("\nCustomize Pizza")
              for amountcustom in range(len(variables_custompizza)):
                variables_customizestuff=(variables_custompizza[amountcustom]).split('>')
                print("\n\033[1;32m"+str(amountcustom+1)+':customize pizza:\033[0;0m')
                print(f'\033[1;33mTopping: \033[0;0m')
                print(str(variables_customizestuff[0]).replace("<","\033[1;32m||\033[0;0m"))
                print(f'\033[1;33mSauce: \033[0;0m')
                print(str(variables_customizestuff[1]).replace("<","\033[1;32m||\033[0;0m"))
                print(f'\033[1;33mCheese: \033[0;0m')
                print(str(variables_customizestuff[2]).replace("<","\033[1;32m||\033[0;0m"))
                print(f'\033[1;33mAmount: \033[0;0m'+(variables_customizestuff[3]).replace("<","\033[1;32m||\033[0;0m"))
              variables_addon=variables[3].split(':')
              print('\nNormal Pizza:Amount')
              for show in variables_addon:
                 print(f'{(show).replace(">"," :")}')
              print('\nTotal Price: '+variables[4])
           linecount=linecount+1
        input("Enter to quit...")
      else:
        NOTIFI='Invalid Input'


def updatecustom_adminmenu():
    global NOTIFI
    while True:
        NOTIFI="Update Option"
        clear_screen()
        print("\033[1;36mSauces Option:                   Price\033[0m")
        maxlength=30
        i=0
        for show in customize_sauce:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{sauceprice[i]}')
            i=i+1
        print("\033[1;36mToppings Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_topping:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{toppingprice[i]}')
            i=i+1
        print("\033[1;36mCheese Option:\033[0m")
        maxlength=30
        i=0
        for show in customize_cheese:
            show=show.ljust(maxlength," ")
            print(f'🟪 {show}RM{cheeseprice[i]}')
            i=i+1
        print("\n\033[1;1m Edit Option For Customize")
        print("\nEnter: \n1=🟦 Sauce Option \n2=🟦 Toppings Option\n3=🟦 Cheese Option\nelse:🟧 Exit")
        ask=input("Enter: \033[0m")
        if ask == '1':
            NOTIFI='Sauce Option'
            while True:
                clear_screen()
                print("\033[1;36mSauces Option:                   Price\033[0m")
                maxlength=30
                i=0
                for show in customize_sauce:
                    show=show.ljust(maxlength," ")
                    print(f'🟪 {show}RM{sauceprice[i]}')
                    i=i+1
                print("\n\033[1;1m Edit an Option For Customize")
                print('Type "exit"=exit (in Option:)')
                editoptionname = input("Option:\033[0m ")
                if editoptionname.lower() == "exit":
                    break
                elif editoptionname in customize_sauce:
                    while True:
                        editnewoptionname=input('New Option Name: ')
                        if editnewoptionname in customize_sauce:
                            continue
                        else:
                            break
                    while True:
                        try:
                            editoptionprice=float(input('New Option Price(RM): '))
                            editoptionprice=str(editoptionprice)
                            break
                        except ValueError:
                            NOTIFI="Please Insert Number!"
                            clear_screen()
                            print("\033[1;36mSauces Option:                   Price\033[0m")
                            maxlength=30
                            i=0
                            for show in customize_sauce:
                                show=show.ljust(maxlength," ")
                                print(f'🟪 {show}RM{sauceprice[i]}')
                                i=i+1
                            print('\nNow  Editting:',editoptionname,)
                            print('New name: '+editnewoptionname)
                    NOTIFI=(editoptionname+" This Option Changed To"+editnewoptionname)
                    f = open('customize.txt', 'r')
                    editwritein=f.readlines()
                    editindex=customize_sauce.index(editoptionname)
                    customize_sauce[editindex]=editnewoptionname
                    sauceprice[editindex]=editoptionprice
                    updatesauceline=":".join([f"{customize_sauce[index]},{sauceprice[index]}" for index in range(len(customize_sauce))])
                    editwritein[0]=updatesauceline+'\n'
                    f=open('customize.txt','w')
                    f.writelines(editwritein)
                    f.close()
                    continue
                else:
                    NOTIFI='⚠️  Option Not Found ⚠️'
        
        if ask == '2':
            NOTIFI='Toppings Option'
            while True:
                clear_screen()
                print("\033[1;36mTopping Option:                 Price\033[0m")
                maxlength=30
                i=0
                for show in customize_topping:
                    show=show.ljust(maxlength," ")
                    print(f'🟪 {show}RM{toppingprice[i]}')
                    i=i+1
                print("\n\033[1;1m Edit an Option For Customize")
                print('Type "exit"=exit (in Option:)')
                editoptionname = input("Option: \033[0m")
                if editoptionname.lower() == "exit":
                    break
                elif editoptionname in customize_topping:
                    while True:
                        editnewoptionname=input('New Option Name: ')
                        if editnewoptionname in customize_topping:
                            continue
                        else:
                            break
                    while True:
                        try:
                            editoptionprice=float(input('New Option Price(RM): '))
                            editoptionprice=str(editoptionprice)
                            break
                        except ValueError:
                            NOTIFI="Please Insert Number!"
                            clear_screen()
                            print("\033[1;36mTopping Option:                 Price\033[0m")
                            maxlength=30
                            i=0
                            for show in customize_topping:
                                show=show.ljust(maxlength," ")
                                print(f'🟪 {show}RM{toppingprice[i]}')
                                i=i+1
                            print('\nNow  Editting:',editoptionname,)
                            print('New name: '+editnewoptionname)
                    NOTIFI=(editoptionname+" This Option Changed To"+editnewoptionname)
                    f = open('customize.txt', 'r')
                    editwritein=f.readlines()
                    editindex=customize_topping.index(editoptionname)
                    customize_topping[editindex]=editnewoptionname
                    toppingprice[editindex]=editoptionprice
                    updatetoppingline=":".join([f"{customize_topping[index]},{toppingprice[index]}" for index in range(len(customize_topping))])
                    editwritein[1]=updatetoppingline+'\n'
                    f=open('customize.txt','w')
                    f.writelines(editwritein)
                    f.close()
                    continue
                else:
                    NOTIFI='⚠️  Option Not Found ⚠️'

        if ask == '3':
            NOTIFI='Cheese Option'
            while True:
                clear_screen()
                print("\033[1;36mCheese Option:                   Price\033[0m")
                maxlength=30
                i=0
                for show in customize_cheese:
                    show=show.ljust(maxlength," ")
                    print(f'🟪 {show}RM{cheeseprice[i]}')
                    i=i+1
                print("\n \033[1;1mEdit an Option For Customize")
                print('Type "exit"=exit (in Option:)')
                editoptionname = input("Option: \033[0m")
                if editoptionname.lower() == "exit":
                    break
                elif editoptionname in customize_cheese:
                    while True:
                        editnewoptionname=input('New Option Name: ')
                        if editnewoptionname in customize_cheese:
                            continue
                        else:
                            break
                    while True:
                        try:
                            editoptionprice=float(input('New Option Price(RM): '))
                            editoptionprice=str(editoptionprice)
                            break
                        except ValueError:
                            NOTIFI="Please Insert Number!"
                            clear_screen()
                            print("\033[1;36mCheese Option:                   Price\033[0m")
                            maxlength=30
                            i=0
                            for show in customize_cheese:
                                show=show.ljust(maxlength," ")
                                print(f'🟪 {show}RM{cheeseprice[i]}')
                                i=i+1
                            print('\nNow  Editting:',editoptionname,)
                            print('New name: '+editnewoptionname)
                    NOTIFI=(editoptionname+" This Option Changed To"+editnewoptionname)
                    f = open('customize.txt', 'r')
                    editwritein=f.readlines()
                    editindex=customize_cheese.index(editoptionname)
                    customize_cheese[editindex]=editnewoptionname
                    cheeseprice[editindex]=editoptionprice
                    updatecheeseline=":".join([f"{customize_cheese[index]},{cheeseprice[index]}" for index in range(len(customize_cheese))])
                    editwritein[2]=updatecheeseline+'\n'
                    f=open('customize.txt','w')
                    f.writelines(editwritein)
                    f.close()
                    continue
                else:
                    NOTIFI='⚠️  Option Not Found ⚠️'
        else:
            break


main()
