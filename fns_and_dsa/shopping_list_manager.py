def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            new_item = input("Enter item name: ")
            shopping_list.append(new_item)
            print(f"{new_item} added to the list!")

        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input("Enter item name to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} removed from the list!")
            else:
                print(f"Item '{item_to_remove}' not found in the list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
