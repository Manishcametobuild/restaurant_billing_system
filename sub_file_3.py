
def order_menu(restaurant, order):
    while True:
        print("\n" + "=" * 55)
        print("ORDER MENU")
        print("=" * 55)

        print("1. Show Menu")
        print("2. Add Item")
        print("3. View Order")
        print("4. Update Quantity")
        print("5. Remove Item")
        print("6. Search Menu")
        print("7. Generate Bill")
        print("8. Cancel Order")

        print("=" * 55)

        choice = input("Enter choice: ")

        if choice == "1":
            restaurant.show_menu()

        elif choice == "2":
            add_item(restaurant, order)

        elif choice == "3":
            order.show_order()

        elif choice == "4":
            update_item(order)

        elif choice == "5":
            remove_item(order)

        elif choice == "6":
            restaurant.search()

        elif choice == "7":
            if order.bill():
                restaurant.orders.append(order)
                return

        elif choice == "8":
            print("Order cancelled.")
            return

        else:
            print("Invalid choice.")