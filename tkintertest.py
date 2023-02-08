import PySimpleGUI as pg

snacks = [    ("Kabab", 25),    ("Noodles", 40),    ("C-Biriyani", 75),    ("E-Biriyani", 50),    ("Pasta", 40),    ("puffs", 17)]

order = []

def show_menu():
    menu = "--- Snacks Menu ---\n"
    for i, snack in enumerate(snacks):
        menu += f"{i + 1}. {snack[0]}: ₹{snack[1]}\n"
    return menu

def take_order():
    while True:
        choice = pg.popup_get_text("Enter your choice (or 'q' to finish): ", title=show_menu())
        if choice == 'q':
            break
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(snacks):
                number = int(pg.popup_get_text("Enter the number of items: "))
                order.extend([snacks[choice]] * number)
            else:
                pg.popup("Invalid choice, please try again.")
        except ValueError:
            pg.popup("Invalid choice, please try again.")

def generate_bill():
    total = 0
    bill = "--- Your Order ---\n"
    order_count = {}
    for item in order:
        if item[0] not in order_count:
            order_count[item[0]] = 0
        order_count[item[0]] += 1
    for item, count in order_count.items():
        bill += f"{item}: ₹{snacks[next(i for i, x in enumerate(snacks) if x[0] == item)][1]} x {count} = ₹{count * snacks[next(i for i, x in enumerate(snacks) if x[0] == item)][1]}\n"
        total += count * snacks[next(i for i, x in enumerate(snacks) if x[0] == item)][1]
    bill += f"\nTotal: ₹{total}\n"
    bill += "------------"
    pg.popup(bill)

def additem():
    itemname = pg.popup_get_text("Enter the name: ")
    itemprice = int(pg.popup_get_text("Enter the price of the item: "))
    snacks.append((itemname, itemprice))
    pg.popup("Item added successfully!!!")

# Main program
while True:
    event, values = pg.Window("Menu", [[pg.Button("Show Menu"), pg.Button("Take Order"), pg.Button("Generate Bill"), pg.Button("Add Stock"), pg.Button("Exit")]]).read()
    if event == "Show Menu":
        pg.popup(show_menu())
    elif event == "Take Order":
        pg.popup(take_order())
    elif event == "Generate Bill":
        pg.popup(generate_bill())
    elif event == "Add Stock":
        pg.popup(additem())
    elif event == "Exit":
        exit()