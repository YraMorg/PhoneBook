import json
import os

FILE = "phonebook.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

with open(FILE, "r") as f:
    contacts = json.load(f)

def save():
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    contacts.append({"name": name, "phone": phone})
    save()
    print("Contact added!")

def show_all():
    if not contacts:
        print("No contacts yet.")
        return
    for c in contacts:
        print(c["name"], "-", c["phone"])

def search():
    name = input("Name to search:")

    for c in contacts:
        if c["name"].lower() == name.lower():
            print("Found:", c["name"], "-", c["phone"])
            return

    print("Not found.")

while True:
    print("\nPhoneBook")
    print("1. Add contact")
    print("2. Show all")
    print("3. Search")
    print("4. Exit")

    choice = input("> ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_all()
    elif choice == "3":
        search()
    elif choice == "4":
        break
    else:
        print("Invalid choise")