import numpy as np
import sub_file_1,sub_file_2,sub_file_3

def main():
    restaurant = Restaurant()

    while True:
        print("\n")
        print("=" * 60)
        print("PYTHON FOOD CORNER".center(60))
        print("=" * 60)

        print("1. Show Menu")
        print("2. New Order")
        print("3. Search Menu")
        print("4. Sales Analytics")
        print("5. Exit")

        print("=" * 60)

        choice = input("Enter choice: ")

        if choice == "1":
            restaurant.show_menu()

        elif choice == "2":
            print("\nNew Order")
            customer = get_customer()
            order = Order(customer)
            order_menu(restaurant, order)

        elif choice == "3":
            restaurant.search()

        elif choice == "4":
            analytics(restaurant)

        elif choice == "5":
            print("\nThank you for using Python Food Corner.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
