# Function to check if the order can be fulfilled
def check_order(inventory, order, budget):
    total_cost = 0
    purchase_details = {}
    status = "Fulfilled"
    
    # Sort items based on price (prioritize cheaper items first)
    sorted_order = sorted(order.items(), key=lambda x: inventory[x[0]]['price'])
    
    for item, requested_qty in sorted_order:
        # Check if item exists in inventory
        if item not in inventory:
            status = "Partially Fulfilled"
            continue
        
        available_qty = inventory[item]['quantity']
        price = inventory[item]['price']

        # If requested more than available
        if requested_qty > available_qty:
            requested_qty = available_qty
            status = "Partially Fulfilled"
        
        cost = requested_qty * price
        
        # Check if adding the item exceeds the budget
        if total_cost + cost > budget:
            # Try to buy as much as possible within remaining budget
            max_affordable_qty = (budget - total_cost) // price
            if max_affordable_qty > 0:
                cost = max_affordable_qty * price
                requested_qty = max_affordable_qty
                status = "Partially Fulfilled"
            else:
                status = "Partially Fulfilled"
                continue

        total_cost += cost
        purchase_details[item] = {'bought': requested_qty, 'cost': cost}

    if not purchase_details:
        status = "Impossible"

    return purchase_details, total_cost, status

# Taking input for inventory
inventory = {}
num_products = int(input("Enter number of products in the inventory: "))
for _ in range(num_products):
    product_name = input("Enter product name: ")
    quantity = int(input(f"Enter quantity of {product_name}: "))
    price = float(input(f"Enter price per unit of {product_name}: "))
    inventory[product_name] = {'quantity': quantity, 'price': price}

# Taking input for customer order
order = {}
num_orders = int(input("Enter number of items in the order: "))
for _ in range(num_orders):
    item_name = input("Enter item name for order: ")
    qty = int(input(f"Enter quantity of {item_name}: "))
    order[item_name] = qty

# Taking input for the customer's budget
budget = float(input("Enter the customer's budget: "))

# Run the function
purchased, total_spent, result_status = check_order(inventory, order, budget)

# Print the result
print("\nOrder Summary:")
for item, details in purchased.items():
    print(f"{item}: Bought {details['bought']} units for Rs.{details['cost']}")

print("Total Spent:", total_spent)
print("Order Status:", result_status)
