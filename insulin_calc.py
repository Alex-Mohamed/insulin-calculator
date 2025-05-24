# This program calculates how much insulin an individual needs, 
# along with how much needs to be ordered, based on user input.

# Stores brand information in the form (name, form, concentration, mL per box)
insulin_list = [("lantus", "pen", 100, 15.0), ("lantus", "vial", 100, 10.0),
                ("basaglar", "pen", 100, 15.0), ("levemir", "pen", 100, 15.0),
                ("levemir", "vial", 100, 10.0), ("toujeo", "pen", 300, 4.5),
                ("toujeo", "max pen", 300, 6.0), 
                
                ("humalog", "pen", 100, 15.0), ("humalog", "pen", 200, 6.0), 
                ("humalog", "vial", 100, 10.0), ("lyumjev", "pen", 100, 15.0),
                ("lyumjev", "pen", 200, 6.0), ("lyumjev", "vial", 100, 10.0),
                ("admelog", "pen", 100, 15.0), ("admelog", "vial", 100, 10.0),
                ("novolog", "pen", 100, 15.0), ("novolog", "vial", 100, 10.0),
                ("fiasp", "pen", 100, 15.0), ("fiasp", "vial", 100, 10.0),
                ("apidra", "pen", 100, 15.0), ("apidra", "vial", 100, 10.0),
                
                ("u500", "vial", 500, 20.0), ("u500", "pen", 500, 6.0),
                
                ("tresiba", "pen", 100, 15.0), ("tresiba", "pen", 200, 9.0),
                ("tresiba", "vial", 100, 10.0),
                
                ("semglee", "pen", 100, 15.0), ("semglee", "vial", 100, 10.0)]

print("DIRECTIONS: Enter the data as requested below. Type 'stop' to end the program when " \
      "prompted for the brand of insulin.\n")

# The infinite loop below only ends when 'stop' is entered for 'brand'
while True:
# Gathers user input needed for calculations
    user_insulin_info = None
    while user_insulin_info == None: # Ensures valid input is provided
        brand = input("\nEnter the insulin brand (ex: Lantus): ").lower()
        if brand == 'stop': exit()
        form = input("Enter 'pen', 'max pen', or 'vial' for the insulin form desired: ").lower()
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