import pymysql
var_conn = pymysql.connect(host="localhost", user="root", password="", database="milk_store5")
cursor = var_conn.cursor()

def start_ussdb():
    print("1. Login")
    print("2. Create account")
    print("3. Stop using Mukamira system")

    choice = input("Enter your choice: ")

    if choice == "1":
        global phone
        phone = input("Enter your phone number: ")
        if len(phone) == 10 and (phone.startswith("078") or phone.startswith("079")):
            pin = input("Enter your pin number: ")

            cursor.execute("SELECT * FROM user WHERE phone = %s AND pass = %s", (phone, pin))
            data = cursor.fetchall()
            for each_data in data:
                check = each_data[0]
            
            if check:
                home()
            else:
                print("Failed to login")
        else:
            print("fake phone number")
                
    elif choice == "2":
        # global phone
        phone = input("Enter phone number: ")
        if len(phone) == 10 and (phone.startswith("078") or phone.startswith("079")):
            fname = input("Enter your first name: ")
            lname = input("Enter your last name: ")
            pin = input("Enter your PIN number: ")

            email = input("Please enter your email address: ")
            check_email = 0
            for i in email:
                if i == "@":
                    check_email = 1

            if check_email == 1:
                cursor.execute("INSERT INTO user values (%s, %s, %s, %s, %s, %s)", ('', fname, lname, phone, pin, email))
                var_conn.commit()
                start_ussdb()
            else:
                print("Invalid email")
            

    elif choice == "3":
        quit()
    else:
        print("Invalid choice")

def home():
    print("1. Place an Order")
    print("2. View Order")
    print("3. Logout Order")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("1. Yoghut")
        print("2. Milk")
        print("3. Cheese")
        
        product_id = input("Enter product ID: ")
        if product_id == "1":
            cursor.execute("SELECT * FROM user WHERE phone = %s", (phone))
            data = cursor.fetchall()
            for i in data:
                user_id = i[0]
            
            unit_price = 5000
            quantity = int(input("Enter a quantity: "))
            total_price = unit_price * quantity
            cursor.execute("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)", ('', 2, product_id, quantity, total_price))
            var_conn.commit()
            print("Order created successfully")
        
        elif product_id == "2":
            print("1. 250ml")
            print("2. 1L")
            print("3. 3L")
            size = input("Enter size: ")

            cursor.execute("SELECT name FROM products WHERE id = %s", (product_id))
            data = cursor.fetchall()
            for i in data:
                product_name = i[0]

            print("Product name: ", product_name)
            if size == '1':
                print("Size: 250ml")
            elif size == "2":
                print("Size: 1L")
            elif size == "3":
                print("Size: 3L")


            unit_price = 200
            quantity = int(input("Enter a quantity: "))
            total_price = unit_price * quantity

            print("Quantity: ", quantity)
            print("Total: ", total_price)
            print("")

            print("1. Confirm order")
            print("2. Cancel order")
            con_cc = input("Enter your choice : ")
            if con_cc == "1":
                cursor.execute("SELECT * FROM user WHERE phone = %s", (phone))
                data = cursor.fetchall()
                for i in data:
                    user_id = i[0]
                cursor.execute("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)", ('', user_id, product_id, quantity, total_price))
                var_conn.commit()
                print("Order created successfully")
            else:
                print("Order creation cancelled")
                home()
    
        elif product_id == "3":
            cursor.execute("SELECT id FROM user WHERE phone = %s", (phone))
            data = cursor.fetchall()
            for i in data:
                user_id = i[0]
            
            unit_price = 3000
            quantity = int(input("Enter a quantity: "))
            total_price = unit_price * quantity
            cursor.execute("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)", ('', user_id, product_id, quantity, total_price))
            var_conn.commit()
            print("Order created successfully")
            
        else:
            print("Invalid input")

    elif choice == "2":
        cursor.execute("SELECT id FROM user WHERE phone = %s", (phone))
        data = cursor.fetchall()
        for i in data:
            user_id = i[0]
        cursor.execute("SELECT products.name, products.unit_price, orders.quantity, orders.total FROM products JOIN orders ON products.id = orders.product_id  WHERE orders.user_id = %s", (user_id))
        data = cursor.fetchall()
        for i in data:
            print("Product name: ", i[0])
            print("Unit price: ", i[1])
            print("Quantity: ", i[2])
            print("Total price ", i[3])
    elif choice == "3":
        start_ussdb()
    else:
        print("Invalid choice")
start_ussdb()