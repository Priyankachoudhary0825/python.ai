#Railway ticket booking system
print("Welcome to CodeRail Railway Booking System ")

# Input details
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Show class options
print("\nChoose travel class:")
print("1. First Class - ₹1500")
print("2. Second Class - ₹1000")
print("3. Sleeper Class - ₹500")

choice = int(input("Enter choice (1/2/3): "))

# Set base price
if choice == 1:
    travel_class = "First Class"
    price = 1500
elif choice == 2:
    travel_class = "Second Class"
    price = 1000
elif choice == 3:
    travel_class = "Sleeper Class"
    price = 500
else:
    print("Invalid choice! Defaulting to Sleeper Class.")
    travel_class = "Sleeper Class"
    price = 500

# Age conditions
if age < 5:
    price = 0
elif age >= 60:
    price = price * 0.8   # 20% discount

# Meal option
meal_choice = input("Do you want to add a meal? (yes/no): ").lower()

if meal_choice == "yes":
    meal_added = "Yes"
    price += 200
else:
    meal_added = "No"

# Output 
print("\n------ Ticket Summary ------")
print("Passenger Name:", name)
print("Age:", age)
print("Class:", travel_class)
print("Meal Added:", meal_added)
print("Final Price: ₹", float(price))
print("Enjoy your journey! ")




# Burger king
print(" Welcome to Burger King\n")

# Display Menu
print("Menu:")
print("1. Whopper Burger ₹150")
print("2. Crispy Veg ₹100")
print("3. Chicken Wings ₹120")

# Prices
price1 = 150
price2 = 100
price3 = 120

# User choice
choice = int(input("Enter the item number (1/2/3): "))
quantity = int(input("Enter quantity: "))

# Calculate total based on item
if choice == 1:
    item_name = "Whopper Burger"
    total = price1 * quantity
elif choice == 2:
    item_name = "Crispy Veg"
    total = price2 * quantity
elif choice == 3:
    item_name = "Chicken Wings"
    total = price3 * quantity
else:
    print("Invalid choice!")
    exit()

print("\nOriginal Price: ₹", total)

# Coupon section
coupon_option = input("Do you have a coupon code? (yes/no): ").lower()
discount = 0

if coupon_option == "yes":
    code = input("Enter your coupon code: ").upper()
    if code == "KING50":
        discount = total * 0.5
        print("Applying 50% discount...")
    elif code == "BK20":
        discount = 20
        print("Applying ₹20 discount...")
    elif code == "NOCOUPON":
        discount = 0
        print("No discount applied.")
    else:
        print("Invalid coupon code. No discount applied.")

# Final calculation
final_price = total - discount

print("\n--Bill Summary--")
print("Quantity:", quantity)
print("Item:", item_name)
print("Original Price: ₹", total)
print("Discount Applied: ₹", discount)
print("Final Price: ₹", final_price)
print("Thanks for ordering at Burger King!")
