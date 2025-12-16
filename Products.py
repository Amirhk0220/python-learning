import csv
import os

FILENAME = "products.csv"
FIELDS = ["product", "price", "count"]
#This is comment for testing git hub

def init_file():
    file_empty = not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0
    if file_empty:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def add_product():
    product = input("what is the product: ")
    while True:
        price = input("Product price: ")
        if price.isdigit():
            price = int(price)
            break
        else:
            print("❌ price must be a number!")
    while True:
        count = input("count of product: ")
        if count.isdigit():
            count = int(count)
            break
        else:
            print("❌ count must be a number!")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({"product": product, "price": price, "count": count})
        print("✔ The product is added!\n")


def show_product():
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        print("\n--- Show all products ---")
        empty = True
        for row in reader:
            print(row)
            empty = False
        if empty:
            print("There are no products.")
    print()


def find_product():
    key_word = input("Product to search for: ")
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        found_any_data = False
        found_target = False
        for row in reader:
            found_any_data = True
            if key_word.lower() == row["product"].lower():
                print(f"✔ The product '{key_word}' was found.")
                found_target = True
                break
    if not found_any_data:
        print("❌ There are no products to search")
        return
    if not found_target:
        print(f"❌ There is no {key_word} to search")


def delete_product():
    delete = input("what product you want to delete: ").strip()
    products = []
    deleted = False
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if delete.lower() == row["product"].strip().lower():
                deleted = True
                continue
            products.append(row)
    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(products)

    if deleted:
        print(f"✔ The product '{delete}' was deleted.")

    else:
        print(f"❌ The product '{delete}' was not found.")


def total_inventory_value():
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)

        total_value = 0
        has_data = False

        for row in reader:
            has_data = True
            price = int(row["price"])
            count = int(row["count"])
            total_value += price * count

        if has_data:
            print(f"\nTotal inventory value: {total_value}\n")
        else:
            print("There are no products.")
def menu():
    init_file()
    while True:
        print("===== Product Management System =====")
        print("1. Add product")
        print("2. Show all product")
        print("3. Search product")
        print("4. Delete product")
        print("5. Total inventory value")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            show_product()
        elif choice == "3":
            find_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            total_inventory_value()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.\n")



menu()
