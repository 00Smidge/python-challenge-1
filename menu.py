
customer_request = [{
	"item name": "",
	"price": float,
	"quantity": int
}]

menu = {
  "Snacks": {
    "Cookie": .99,
    "Banana": .69,
    "Apple": .49,
    "Granola bar": 1.99
  },
  "Meals": {
    "Burrito": 4.49,
    "Teriyaki Chicken": 9.99,
    "Sushi": 7.49,
    "Pad Thai": 6.99,
    "Pizza": {
      "Cheese": 8.99,
      "Pepperoni": 10.99,
      "Vegetarian": 9.99
    },
    "Burger": {
      "Chicken": 7.49,
      "Beef": 8.49
    }
  },
  "Drinks": {
    "Soda": {
      "Small": 1.99,
      "Medium": 2.49,
      "Large": 2.99
    },
    "Tea": {
      "Green": 2.49,
      "Thai iced": 3.99,
      "Irish breakfast": 2.49
    },
    "Coffee": {
      "Espresso": 2.99,
      "Flat white": 2.99,
      "Iced": 3.49
    }
  },
  "Dessert": {
    "Chocolate lava cake": 10.99,
    "Cheesecake": {
      "New York": 4.99,
      "Strawberry": 6.49
    },
    "Australian Pavlova": 9.99,
    "Rice pudding": 4.99,
    "Fried banana": 4.49
  }
}



print("Welcome to the variety food truck.")

place_order = True

while place_order:
  print("From which menu would you like to order? ")
  category_id = 1
  menu_items = {}

  for key in menu.keys():
    print(f"{category_id}: {key}")
    menu_items[category_id] = key
    category_id += 1

  menu_category = input("Type menu number: ")
  if menu_category.isdigit():
    if int(menu_category) in menu_items.keys():
      menu_category_name = menu_items[int(menu_category)]
      print(f"You selected {menu_category_name}")
      menu_item_id = 1
      menu_items = {}
      print("-------|--------------------------|-------")
      for key, value in menu[menu_category_name].items():
        if type(value) is not dict:
          num_item_spaces = 24 - len(key)
          item_spaces = " " * num_item_spaces
          print(f"{menu_item_id}      | {key}{item_spaces} | ${value}")
          menu_items[menu_item_id] = {
            "Item name": key,
            "Price": value
          }
          menu_item_id += 1
        elif type(value) is dict:
          for k2, v2 in value.items():
            num_item_spaces = 24 - len(k2)
            item_spaces = " " * num_item_spaces
            print(f"{menu_item_id}      | {k2}{item_spaces} | ${v2}")
            menu_items[menu_item_id] = {
              "Item name": k2,
              "Price": v2
            }
            menu_item_id += 1
            print(f"What would you like to order from the {menu_category_name} menu? ")
            if int(menu_category) in menu_items.keys():
              #* place item in customer_order
              #* print order confirmation
              #* ask if customer would like to order more
                #if yes then return to top of loop else then print receipt

#               for k3, v3 in value2.items():
#                 num_item_spaces = 24 - len(key + k3) - 3
#                 item_spaces = " " * num_item_spaces
#                 print(f"{menu_item_id}      | {key} - {k3}{item_spaces} | ${v3}")
#                 menu_item_id += 1
#                 break;
#             num_item_spaces = 24 - len(key + key2) - 3
#             item_spaces = " " * num_item_spaces
#             print(f"{menu_item_id}      | {key} - {key2}{item_spaces} | ${value2}")
#             menu_items[menu_item_id] = {
#               "Item name": key + " - " + key2,
#               "Price": value2
#             }
#             menu_item_id += 1
#         else:
#           num_item_spaces = 24 - len(key)
#           item_spaces = " " * num_item_spaces
#           print(f"{menu_item_id}      | {key}{item_spaces} | ${value}")
#           menu_items[menu_item_id] = {
#             "Item name": key,
#             "Price": value
#           }
#           menu_item_id += 1
#     while True:
#         keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
# print("This is what we are preparing for you.\n")

# #print(order)

# print("Item name                 | Price  | Quantity")
# print("--------------------------|--------|----------")
