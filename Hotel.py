import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create SQLite database connection
conn = sqlite3.connect('restaurant.db')
c = conn.cursor()

# Create Menu table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS Menu (
                item_id INTEGER PRIMARY KEY,
                item_name TEXT NOT NULL,
                item_price REAL NOT NULL
            )''')
conn.commit()

# Create Orders table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS Orders (
                order_id INTEGER PRIMARY KEY,
                customer_name TEXT NOT NULL,
                item_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (item_id) REFERENCES Menu(item_id)
            )''')
conn.commit()

# Function to add a menu item
def add_item():
    item_name = item_name_entry.get()
    item_price = float(item_price_entry.get())

    c.execute("INSERT INTO Menu (item_name, item_price) VALUES (?, ?)", (item_name, item_price))
    conn.commit()
    messagebox.showinfo("Success", "Item added successfully")

# Function to view menu
def view_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")

    menu_label = tk.Label(menu_window, text="Menu", font=("Arial", 18))
    menu_label.pack()

    menu_items = c.execute("SELECT * FROM Menu").fetchall()
    for item in menu_items:
        item_label = tk.Label(menu_window, text=f"{item[0]}. {item[1]} - ${item[2]}")
        item_label.pack()

# Function to place an order
def place_order():
    customer_name = customer_name_entry.get()
    item_id = item_id_entry.get()
    quantity = int(quantity_entry.get())

    c.execute("INSERT INTO Orders (customer_name, item_id, quantity) VALUES (?, ?, ?)", (customer_name, item_id, quantity))
    conn.commit()
    messagebox.showinfo("Success", "Order placed successfully")

# Tkinter setup
root = tk.Tk()
root.title("Restaurant Management System")

# Add Item Section
add_item_label = tk.Label(root, text="Add Item")
add_item_label.grid(row=0, column=0, columnspan=2, pady=10)

item_name_label = tk.Label(root, text="Item Name:")
item_name_label.grid(row=1, column=0, sticky="e")
item_name_entry = tk.Entry(root)
item_name_entry.grid(row=1, column=1)

item_price_label = tk.Label(root, text="Item Price:")
item_price_label.grid(row=2, column=0, sticky="e")
item_price_entry = tk.Entry(root)
item_price_entry.grid(row=2, column=1)

add_item_button = tk.Button(root, text="Add Item", command=add_item)
add_item_button.grid(row=3, column=0, columnspan=2, pady=10)

# View Menu Section
view_menu_button = tk.Button(root, text="View Menu", command=view_menu)
view_menu_button.grid(row=4, column=0, columnspan=2, pady=10)

# Place Order Section
place_order_label = tk.Label(root, text="Place Order")
place_order_label.grid(row=5, column=0, columnspan=2, pady=10)

customer_name_label = tk.Label(root, text="Customer Name:")
customer_name_label.grid(row=6, column=0, sticky="e")
customer_name_entry = tk.Entry(root)
customer_name_entry.grid(row=6, column=1)

item_id_label = tk.Label(root, text="Item ID:")
item_id_label.grid(row=7, column=0, sticky="e")
item_id_entry = tk.Entry(root)
item_id_entry.grid(row=7, column=1)

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=8, column=0, sticky="e")
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=8, column=1)

place_order_button = tk.Button(root, text="Place Order", command=place_order)
place_order_button.grid(row=9, column=0, columnspan=2, pady=10)

# Start GUI
root.mainloop()

# Close database connection
conn.close()
