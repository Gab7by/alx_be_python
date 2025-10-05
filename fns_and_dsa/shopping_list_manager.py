def display_menu():
    print("\n=== Shopping List Manager ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to your shopping list.")
            else:
                print("⚠️ Item name cannot be empty.")

        elif choice == '2':
            # Remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' has been removed from your shopping list.")
            else:
                print(f"❌ '{item}' not found in your shopping list.")

        elif choice == '3':
            # View the current shopping list
            if shopping_list:
                print("\n🛒 Your Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("📝 Your shopping list is currently empty.")

        elif choice == '4':
            # Exit the program
            print("👋 Goodbye! Thanks for using the Shopping List Manager.")
            break

        else:
            print("⚠️ Invalid choice. Please try again (1-4).")

if __name__ == "__main__":
    main()
