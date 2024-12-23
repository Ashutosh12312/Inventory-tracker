# Function to add a product to inventory
def insert_item(inventory_list, product, amount, unit_price):
    """
    This function adds a new product along with its quantity and price to the inventory.
    After adding, it ensures the inventory is sorted alphabetically by product name.
    """
    inventory_list.append((product, amount, unit_price))
    inventory_list.sort(key=lambda item: item[0])  # Sort the list by product name after insertion
    return inventory_list


# Function to remove a product from the inventory
def remove_product(inventory_list, product):
    """
    Removes the specified product from the inventory list.
    If the product is not found, the list remains unchanged.
    """
    new_inventory = [item for item in inventory_list if item[0] != product]
    new_inventory.sort(key=lambda item: item[0])  # Keep inventory sorted after removal
    return new_inventory


# Function to calculate the total value of inventory
def calculate_inventory_value(inventory_list):
    """
    This function calculates the total monetary value of all products in the inventory,
    by multiplying the quantity by the unit price of each item.
    """
    total_value = 0
    for product, amount, unit_price in inventory_list:
        total_value += amount * unit_price
    return total_value


# Function to display inventory items and the total value
def display_current_inventory(inventory_list):
    """
    This function prints the current inventory details, including the product name, 
    quantity, and price. It also prints the total value of the inventory.
    """
    print("Inventory Report:")
    for product, amount, unit_price in inventory_list:
        print(f"Product: {product}, Quantity: {amount}, Unit Price: ${unit_price:.2f}")
    print(f"Total Inventory Value: ${calculate_inventory_value(inventory_list):.2f}")


# Main program logic
def start_inventory_program():
    """
    This is the main function where we define the initial stock of products and perform 
    various inventory operations such as adding, removing, and displaying items.
    """
    # Initial stock setup
    initial_stock = [
        ("Apples", 50, 0.5),
        ("Bananas", 30, 0.3),
        ("Oranges", 20, 0.7)
    ]
    initial_stock.sort(key=lambda item: item[0])  # Sort inventory alphabetically initially

    # Display initial inventory
    display_current_inventory(initial_stock)

    # Add a new product
    print("\nAdding 'Grapes' to the inventory...")
    updated_inventory = insert_item(initial_stock, "Grapes", 40, 1.2)
    display_current_inventory(updated_inventory)

    # Remove a product
    print("\nRemoving 'Bananas' from the inventory...")
    updated_inventory = remove_product(updated_inventory, "Bananas")
    display_current_inventory(updated_inventory)


if __name__ == "__main__":
    # Run the inventory program
    start_inventory_program()
