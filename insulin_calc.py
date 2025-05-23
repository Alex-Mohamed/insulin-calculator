# This program calculates how much insulin an individual needs, 
# along with how much needs to be ordered, based on user input.

# Stores brand information in the form (name, form, concentration, mL per box)
insulin_list = [("Lantis", "pen", 100, 15.0), ("Lantis", "vial", 100, 10.0),
                ("Basaglar", "pen", 100, 15.0), ("Levemir", "pen", 100, 15.0),
                ("Levemir", "vial", 100, 10.0), ("Toujeo", "pen", 300, 4.5),
                ("Toujeo", "max pen", 300, 6.0), 
                
                ("Humalog", "pen", 100, 15.0), ("Humalog", "pen", 200, 6.0), 
                ("Humalog", "vial", 100, 10.0), ("Lyumjev", "pen", 100, 15.0),
                ("Lyumjev", "pen", 200, 6.0), ("Lyumjev", "vial", 100, 10.0),
                ("Admelog", "pen", 100, 15.0), ("Admelog", "vial", 100, 10.0),
                ("NovoLog", "pen", 100, 15.0), ("NovoLog", "vial", 100, 10.0),
                ("Flasp", "pen", 100, 15.0), ("Flasp", "vial", 100, 10.0),
                ("Apidra", "pen", 100, 15.0), ("Apidra", "vial", 100, 10.0),
                
                ("Humulin R", "vial", 500, 20.0), ("Humulin R", "pen", 500, 6.0),
                
                ("Tresiba", "pen", 100, 15.0), ("Tresiba", "pen", 200, 9.0),
                ("Tresiba", "vial", 100, 10.0),
                
                ("Semglee", "pen", 100, 15.0), ("Semglee", "vial", 100, 10.0)]

# Gathers user input needed for calculations
user_insulin_info = None
while user_insulin_info == None: # Ensures valid input is provided
    brand = input("Enter the insulin brand (ex: Lantis): ")
    form = input("Enter 'pen', 'max pen', or 'vial' for the insulin form desired: ")
    conc = int(input("Enter the desired concentration in mL (ex: 100): "))
    num_days = int(input("Enter '30' or '90' for desired per-day supply: "))
    units_per_day = int(input('Enter the units per day needed: '))

    # Finds and stores the tuple with the information needed
    for item in insulin_list:
        if item[0] == brand and item[1] == form and item[2] == conc:
            user_insulin_info = item
            break
    if user_insulin_info == None: # Checks for invalid input
        print("No information found based on user input. Please input valid data.")

# Calculates amount of insulin needed (prints to user)
insulin_amount = (units_per_day * num_days) / user_insulin_info[2]
print(f"\nThe amount of insulin needed is {insulin_amount} mL")

# Determines the amount of insulin to order based on mL per box (prints to user)
found = False
mult_counter = 1
while not found:
    if insulin_amount <= (user_insulin_info[3] * mult_counter):
        found = True
        order_amount = user_insulin_info[3] * mult_counter
    else:
        mult_counter += 1
print(f"The amount of insulin that needs to be ordered is {order_amount} mL")