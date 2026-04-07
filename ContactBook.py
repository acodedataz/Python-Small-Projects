import os
import time

Contact = {}

# Clear Screen Function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Pause Effect
def pause():
    time.sleep(1.5)

# Show Contacts
def show_contacts():
    if not Contact:
        print("\n📭 Contact Book is Empty!\n")
        return

    print("\n📒 Your Contact List:\n")
    print("Name\t\tPhone")
    print("-" * 25)

    for name in sorted(Contact):
        print(f"{name}\t\t{Contact[name]}")
    print()

# Add Contact
def add_contact():
    name = input("Enter Name: ").strip().title()

    if name in Contact:
        print("⚠️ Contact already exists!")
        return

    phone = input("Enter Phone Number: ").strip()

    if not phone.isdigit():
        print("❌ Invalid phone number!")
        return

    Contact[name] = phone
    print("✅ Contact Added Successfully!")

# Search Contact
def search_contact():
    name = input("Search Name: ").strip().title()

    if name in Contact:
        print(f"📞 {name} → {Contact[name]}")
    else:
        print("❌ Contact Not Found!")

# Edit Contact
def edit_contact():
    name = input("Enter Name to Edit: ").strip().title()

    if name in Contact:
        phone = input("Enter New Number: ").strip()

        if not phone.isdigit():
            print("❌ Invalid number!")
            return

        Contact[name] = phone
        print("✅ Contact Updated!")
    else:
        print("❌ Contact Not Found!")

# Delete Contact
def delete_contact():
    name = input("Enter Name to Delete: ").strip().title()

    if name in Contact:
        confirm = input("Are you sure? (y/n): ").lower()

        if confirm == "y":
            Contact.pop(name)
            print("🗑️ Contact Deleted!")
        else:
            print("❌ Cancelled!")
    else:
        print("❌ Contact Not Found!")

# Main App Loop
while True:
    clear()
    print("====== 📱 CONTACT BOOK APP ======\n")
    print("1. ➕ Add Contact")
    print("2. 🔍 Search Contact")
    print("3. 📋 Show All Contacts")
    print("4. ✏️ Edit Contact")
    print("5. 🗑️ Delete Contact")
    print("6. 🚪 Exit\n")

    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("❌ Please enter a valid number!")
        pause()
        continue

    clear()

    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        show_contacts()
    elif choice == 4:
        edit_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice!")

    pause()