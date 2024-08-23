# Menu dictionary
menu = {
  "Snacks": {"Cookie": 0.99, "Banana": 0.69, "Apple": 0.49, "Granola bar": 1.99},
    "Meals": {
      "Burrito": 4.49,
      "Teriyaki Chicken": 9.99,
      "Sushi": 7.49,
      "Pad Thai": 6.99,
      "Pizza": {"Cheese": 8.99, "Pepperoni": 10.99, "Vegetarian": 9.99},
      "Burger": {"Chicken": 7.49, "Beef": 8.49},
    },
    "Drinks": {
      "Soda": {"Small": 1.99, "Medium": 2.49, "Large": 2.99},
      "Tea": {"Green": 2.49, "Thai iced": 3.99, "Irish breakfast": 2.49},
      "Coffee": {"Espresso": 2.99, "Flat white": 2.99, "Iced": 3.49},
    },
    "Dessert": {
      "Chocolate lava cake": 10.99,
      "Cheesecake": {"New York": 4.99, "Strawberry": 6.49},
      "Australian Pavlova": 9.99,
      "Rice pudding": 4.99,
      "Fried banana": 4.49,
    },
}

print("Welcome to the variety food truck.")


customer_order = []
place_order = True
while place_order:
  print("From which menu would you like to order? ")
  menu_category_id = 1
  menu_items = {}
  
  for key in menu.keys():
    print(f"{menu_category_id}: {key}")
    menu_items[menu_category_id] = key
    menu_category_id += 1

  menu_category = input("Type menu number: ")

  if menu_category.isdigit():
    if int(menu_category) in menu_items.keys():
      
      menu_category_name = menu_items[int(menu_category)]
      print(f"You selected {menu_category_name}")
      menu_item_id = 1
      menu_items = {}
      print("Item # | Item name                | Price")
      print("-------|--------------------------|-------")
      
      for key, value in menu[menu_category_name].items():
        if type(value) is dict:
          
          for key2, value2 in value.items():
            calc_white_spaces = 24 - len(key + key2) - 3
            add_spaces = " " * calc_white_spaces
            print(f"{menu_item_id}      | {key} - {key2}{add_spaces} | ${value2}")
            menu_items[menu_item_id] = {
              "Item name": key + " - " + key2,
              "Price": value2,
            }
            menu_item_id += 1
            
        else:
          calc_white_spaces = 24 - len(key)
          add_spaces = " " * calc_white_spaces
          print(f"{menu_item_id}      | {key}{add_spaces} | ${value}")
          menu_items[menu_item_id] = {"Item name": key, "Price": value}
          menu_item_id += 1
          
      menu_selection = input(f"\nWhat would you like to order from {menu_category_name}? ")
      
      if not menu_selection.isdigit(): print('ERROR! Input was not iterable. Please try entering a numerical value. ')  # noqa: E701
      menu_selection = int(menu_selection)
      
      if menu_selection in menu_items.keys():
        quantity = input(f'How many {menu_items[menu_selection]['Item name']}s would you like? ') or '1'
        if not quantity.isdigit(): 
          print('Error: your input is not iterable, your quantity has be defaulted to 1')  # noqa: E701
          quantity = 1
        quantity = int(quantity)
        
        customer_order.append({
          "Item name": menu_items[menu_selection]['Item name'],
          "Price": menu_items[menu_selection]['Price'],
          "Quantity": quantity
        })
                
        print('\nCurrent Order')
        print("Item # | Item name                | Price | Quantity")
        print("-------|--------------------------|-------|---------")

        for index, item in enumerate(customer_order, start = 1):
          calc_white_space = 24 - len(item['Item name'])
          add_spaces = " " * calc_white_space
          print(f'{index}      | {item['Item name']}{add_spaces} | ${item['Price']} | {item['Quantity']}')
        
      else: 
        print(f'Error. Your selection of {menu_selection} what not in the {menu_category_name} menu. Please try selecting from the provided list. ')
          
    else:
      print(f"{menu_category} was not a menu option.")
          
  else:
      print("You didn't select a number.")
      
  keep_ordering = str(input("Would you like to keep ordering? (Y)es or (N)o ")).upper()
  match keep_ordering:
    case 'Y':
      continue
    case 'N':
      print('Thank you for shopping with Food Truck Food Co')
      place_order = False
      break
    case _:
      print('ERROR!! Unable to interpret input. Please use y or n')
      keep_ordering = str(input("Would you like to keep ordering? (Y)es or (N)o ")).upper()
      continue

print("This is what we are preparing for you.\n")
print("Item # | Item name                | Price | Quantity")
print("-------|--------------------------|-------|---------")

for index, item in enumerate(customer_order, start = 1):
  calc_white_space = 24 - len(item['Item name'])
  add_spaces = " " * calc_white_space
  print(f'{index}      | {item['Item name']}{add_spaces} | ${item['Price']} | {item['Quantity']}')
  
total = sum([item['Price'] * int(item['Quantity']) for item in customer_order])
print(f'Your total today is: ${total:.2f}')