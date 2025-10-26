from CustomerOrder import CustomerOrder as co
from Product import Product as Product

### initialize some orders
co1 = co('Alice', 'Laptop', 1, 50.00, 'Electronics')
co2 = co('Alice', 'Smartphone', 2, 80.00, 'Electronics')
co3 = co('Alice', 'Desk Chair', 1, 150.00, 'Furniture')
co4 = co('Alice', 'Headphones', 1, 200.00, 'Electronics')
co5 = co('Bob', 'Monitor', 1, 24.00, 'Electronics')
co6 = co('Bob', 'Keyboard', 1, 22.00, 'Electronics')
co7 = co('Charlie', 'Mouse', 1, 15.00, 'Electronics')
co8 = co('David', 'Laptop', 3, 50.00, 'Electronics')
co9 = co('John', 'Laptop', 3, 50.00, 'Electronics')
co10 = co('Alice', 'shirt', 3, 50.00, 'Clothing')
co11 = co('Alice', 'jeans', 2, 80.00, 'Clothing')
co12 = co('Charlie', 'jacket', 1, 120.00, 'Clothing')

#### initialize some products
prd1 = Product('Laptop', 1200.00, 'Electronics')
prd2 = Product('Smartphone', 800.00, 'Electronics')
prd3 = Product('Desk Chair', 150.00, 'Furniture')
prd4 = Product('Headphones', 200.00, 'Electronics')
prd5 = Product('Monitor', 300.00, 'Electronics')
prd6 = Product('shirt', 50.00, 'Clothing')
prd7 = Product('jeans', 80.00, 'Clothing')
prd8 = Product('jacket', 120.00, 'Clothing')
prd9 = Product('sneakers', 90.00, 'Footwear')
prd10 =Product('boots', 150.00, 'Footwear')

productSet = {prd1, prd2, prd3, prd4, prd5, prd6, prd7, prd8, prd9, prd10}

customer_orders = [co1, co2, co3, co4, co5, co6, co7, co8, co9, co10, co11, co12]


customer_order_history = {}
product_classification = {}

def create_new_order():
    customer_name = input("Enter customer name: ")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    category = input("Enter category: ")
    new_order = co(customer_name, product_name, quantity, price, category)
    customer_orders.append(new_order)
    print(f"Order created for {customer_name}: {product_name}, Quantity: {quantity}, Price: {price}, Category: {category}")

def display_orders_by_customer_name(customer_name):
    found  = False
    for order in customer_orders:
        if order.customer_name.lower() == customer_name.lower():
            found = True
            print(f"  Product : {order.product_name}")
            print(f"  Quantity: {order.quantity}")
            print(f"  Price   : {order.price}")
            print(f"  Category: {order.category}")
            print("  " + "-" * 36)
    if not found:
        print("  No orders found for this customer.")
    print("=" * 40 + "\n")

def display_all_orders():
    for order in customer_orders:
        customer_order_history[order.customer_name] = [co for co in customer_orders if co.customer_name == order.customer_name]

    print("\n========== All Orders by Customer ==========")
    for customer, orders in customer_order_history.items():
        print(f"\nCustomer: {customer}")
        print("-" * 40)
        for order in orders:
            print(f"  Product: {order.product_name}")
            print(f"  Quantity: {order.quantity}")
            print(f"  Price: {order.price}")
            print(f"  Category: {order.category}")
            print("  " + "-" * 36)
    print("============================================\n")

def classify_product_categories():
    print("************* Classify Product Categories **************** \n")
    product_by_category = {}
    for product in productSet:
        if product.category not in product_by_category:
            product_by_category[product.category] = []
        product_by_category[product.category].append(product)

    # Display grouped products
    for category, products in product_by_category.items():
        print(f"Category: {category}")
        for product in products:
            print(f"  - {product.name}")

def analyze_customer_orders():
    customer_totals = {}
    customer_names = {order.customer_name for order in customer_orders}
    for order in customer_orders:
            customer_totals[order.customer_name] = customer_totals.get(order.customer_name, 0) + order.price
    print("*" * 10 + " Customer Order Analysis " + "*" * 10)
    counter = 0
    for key, value in customer_totals.items():
        counter= counter + 1
        if value > 100:
           cls = 'High value customer'
        elif 50 <= value <= 100:
            cls =  'moderate buyer'
        else:
            cls = 'Lower buyer'
        print(f" #{counter} - {key} is {cls} of order value >> {value:.2f}")

    #customer_totals[key] = {'total': value, 'classification': cls}
    #print(customer_totals)
    #print("*" *  40)
    #print("customer_names" , customer_names)

def generate_business_insights():

    products_total_revenue =  {}
    """ extract unique product names using set comprehension """
    unique_product_set = {order.product_name for order in customer_orders}
    for order in customer_orders:
        products_total_revenue[order.product_name] = products_total_revenue.get(order.product_name, 0) + order.price

    print(" Total revenue per product : ", products_total_revenue)
    print("=" * 40 + "\n")
    print("Extract unique product names using set")
    print("=" * 40 + "\n")
    counter = 0
    for product in unique_product_set:
        counter = counter + 1
        print(f" #{counter} : {product}")

    electronics_order = [order for order in customer_orders if 'Electronics' in order.category]

    print("*" +"*" * 10 + " Electronics Orders " + "*" * 10)
    for eorder in electronics_order:
        print(f" {eorder.customer_name}  Product: {eorder.product_name}, Category: {eorder.category}, Price: {eorder.price}")

    """ Sorted """
    customer_names = {order.customer_name for order in customer_orders}
    customer_totals = {}
    for order in customer_orders:
        customer_totals[order.customer_name] = customer_totals.get(order.customer_name, 0) + order.price


    sorted_customers_=  sorted(customer_totals.items(), key= by_total, reverse=True)

    print_sorted = lambda sorted_list: [print(f" Customer: {customer[0]}  Total Spending: {customer[1]}") for customer in sorted_list]

    print("=" * 40)
    print(" Top 3 customers by total spending ")
    print("=" * 40 + "\n")
    print_sorted(sorted_customers_[0:3])


def summarize_customer_orders():
    analyze_customer_orders()
    categorized_order = [co for co in customer_orders if co.category == 'Clothing' or co.category == 'Electronics']

    unique_product_set = {order.product_name for order in categorized_order}
    unique_product_set = sorted(unique_product_set)
    classifed_orders = {}
    print("************* Customer who bought clothing and electronics **************** \n")
    for co in categorized_order:
        classifed_orders[co.category] = [order for order in categorized_order if order.category == co.category]
    for category, orders in classifed_orders.items():
        print(f"\nCustomer: {category}")
        print("-" * 40)
        for order in orders:
            print(f"  Product: {order.product_name}")
            print(f"  Quantity: {order.quantity}")
            print(f"  Price: {order.price}")
            print(f"  Category: {order.category}")
            print("  " + "-" * 36)

    print("*" * 10 + " Unique Products " + "*" * 10)
    counter = 0
    for product in unique_product_set:
        counter = counter + 1
        print(f" #{counter} : {product}")

def by_total(item):
    return item[1]


option = ''
while option != "x" or option != "X":
    print("\n")
    print("\n========== Main Menu ==========")
    print("Option X  - Exit")
    print("Option S  - Create/Store new order")
    print("Option C  - Classify product categories")
    print("Option A  - Analyze total spending per customer")
    print("Option G  - Generate a summary report of orders")
    print("Option O  - Organize orders by customer")
    print("Option D  - Display orders by customer")
    print("Option P -  Print all orders")
    print("================================\n")

    option = input("Enter your choice: ").lower()
    if option == "x" :
        print("Thank you for using our application")
        break
    elif option == "s":
        create_new_order()
    elif option == "d":
        cname = input("Enter customer name: ")
        display_orders_by_customer_name(cname)
    elif option == "p":
        display_all_orders()
    elif option == "c":
        classify_product_categories()
    elif option == "a":
        analyze_customer_orders()
    elif option == "g":
        generate_business_insights()
    elif option == "o":
        summarize_customer_orders()



