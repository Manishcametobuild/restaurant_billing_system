class Item:
    def __init__(self, item_id, name, category, price, veg=True):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.veg = veg


class FoodItem(Item):
    def __init__(self, item_id, name, category, price, veg=True):
        super().__init__(item_id, name, category, price, veg)

    def show(self):
        food_type = "Veg" if self.veg else "Non-Veg"
        print(f"{self.item_id:<5}{self.name:<25}{self.category:<15}"
              f"₹{self.price:<10.2f}{food_type:<10}")


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Order:
    order_no = 1000

    def __init__(self, customer):
        Order.order_no += 1
        self.number = Order.order_no
        self.customer = customer
        self.items = {}

    def add_item(self, item, quantity):
        if item.item_id in self.items:
            self.items[item.item_id]["quantity"] += quantity
        else:
            self.items[item.item_id] = {
                "item": item,
                "quantity": quantity
            }

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False

    def update_item(self, item_id, quantity):
        if item_id in self.items:
            if quantity == 0:
                del self.items[item_id]
            else:
                self.items[item_id]["quantity"] = quantity
            return True
        return False

    def subtotal(self):
        total = 0

        for data in self.items.values():
            total += data["item"].price * data["quantity"]

        return total

    def discount(self):
        total = self.subtotal()

        if total >= 2000:
            rate = 15
        elif total >= 1000:
            rate = 10
        elif total >= 500:
            rate = 5
        else:
            rate = 0

        amount = total * rate / 100

        return rate, amount

    def gst(self):
        total = self.subtotal()
        discount_rate, discount_amount = self.discount()

        amount = total - discount_amount
        tax = amount * 5 / 100

        return tax

    def final_amount(self):
        total = self.subtotal()
        discount_rate, discount_amount = self.discount()
        tax = self.gst()

        return total - discount_amount + tax

    def show_order(self):
        if not self.items:
            print("\nOrder is empty.")
            return

        print("\n" + "=" * 75)
        print("CURRENT ORDER")
        print("=" * 75)

        print(f"{'ID':<5}{'Item':<25}{'Price':<12}{'Qty':<8}{'Total':<12}")
        print("-" * 75)

        for item_id, data in self.items.items():
            item = data["item"]
            quantity = data["quantity"]
            total = item.price * quantity

            print(
                f"{item.item_id:<5}"
                f"{item.name:<25}"
                f"₹{item.price:<10.2f}"
                f"{quantity:<8}"
                f"₹{total:<10.2f}"
            )

        print("-" * 75)
        print(f"{'Subtotal':>60} : ₹{self.subtotal():.2f}")
        print("=" * 75)

    def bill(self):
        if not self.items:
            print("\nCannot generate bill. Order is empty.")
            return False

        subtotal = self.subtotal()
        discount_rate, discount_amount = self.discount()
        tax = self.gst()
        final = self.final_amount()

        print("\n")
        print("=" * 70)
        print("PYTHON FOOD CORNER".center(70))
        print("RESTAURANT BILL".center(70))
        print("=" * 70)

        print(f"Order Number : {self.number}")
        print(f"Customer     : {self.customer.name}")
        print(f"Phone        : {self.customer.phone}")

        print("-" * 70)
        print(f"{'Item':<25}{'Qty':<8}{'Price':<12}{'Total':<15}")
        print("-" * 70)

        for data in self.items.values():
            item = data["item"]
            quantity = data["quantity"]
            total = item.price * quantity

            print(
                f"{item.name:<25}"
                f"{quantity:<8}"
                f"₹{item.price:<10.2f}"
                f"₹{total:<12.2f}"
            )

        print("-" * 70)

        print(f"{'Subtotal':<50} ₹{subtotal:.2f}")
        print(
            f"{'Discount (' + str(discount_rate) + '%)':<50}"
            f" -₹{discount_amount:.2f}"
        )
        print(f"{'GST (5%)':<50} ₹{tax:.2f}")

        print("-" * 70)
        print(f"{'Final Amount':<50} ₹{final:.2f}")
        print("=" * 70)
        print("Thank you for visiting!")
        print("=" * 70)

        return True


class Restaurant:
    def __init__(self):
        self.menu = {}
        self.orders = []
        self.create_menu()

    def create_menu(self):
        foods = [
            FoodItem(1, "Margherita Pizza", "Pizza", 249, True),
            FoodItem(2, "Farmhouse Pizza", "Pizza", 349, True),
            FoodItem(3, "Chicken Pizza", "Pizza", 399, False),
            FoodItem(4, "Veg Burger", "Burger", 149, True),
            FoodItem(5, "Chicken Burger", "Burger", 199, False),
            FoodItem(6, "French Fries", "Sides", 99, True),
            FoodItem(7, "Cheese Fries", "Sides", 129, True),
            FoodItem(8, "Veg Sandwich", "Sandwich", 129, True),
            FoodItem(9, "Chicken Sandwich", "Sandwich", 179, False),
            FoodItem(10, "Pasta Alfredo", "Pasta", 249, True),
            FoodItem(11, "Chicken Pasta", "Pasta", 299, False),
            FoodItem(12, "Cold Coffee", "Drinks", 119, True),
            FoodItem(13, "Fresh Lime", "Drinks", 79, True),
            FoodItem(14, "Coke", "Drinks", 60, True),
            FoodItem(15, "Chocolate Brownie", "Dessert", 149, True),
            FoodItem(16, "Ice Cream", "Dessert", 99, True)
        ]

        for food in foods:
            self.menu[food.item_id] = food

    def show_menu(self):
        print("\n" + "=" * 75)
        print("RESTAURANT MENU".center(75))
        print("=" * 75)

        print(
            f"{'ID':<5}"
            f"{'Item Name':<25}"
            f"{'Category':<15}"
            f"{'Price':<10}"
            f"{'Type':<10}"
        )

        print("-" * 75)

        for item in self.menu.values():
            item.show()

        print("=" * 75)

    def search(self):
        word = input("\nEnter item or category: ").lower()

        found = False

        print("\nSearch Results")
        print("-" * 75)

        for item in self.menu.values():
            if word in item.name.lower() or word in item.category.lower():
                item.show()
                found = True

        if not found:
            print("No item found.")

        print("-" * 75)


def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Enter a valid number.")


def get_quantity():
    while True:
        quantity = get_number("Enter quantity: ")

        if quantity > 0:
            return quantity

        print("Quantity must be greater than zero.")


def get_customer():
    while True:
        name = input("Enter customer name: ").strip()

        if len(name) >= 2:
            break

        print("Enter a valid name.")

    while True:
        phone = input("Enter phone number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            break

        print("Enter a valid 10-digit phone number.")

    return Customer(name, phone)


def add_item(restaurant, order):
    restaurant.show_menu()

    item_id = get_number("Enter item ID: ")

    if item_id not in restaurant.menu:
        print("Invalid item ID.")
        return

    quantity = get_quantity()

    item = restaurant.menu[item_id]

    order.add_item(item, quantity)

    print(f"{quantity} {item.name} added to order.")


def update_item(order):
    if not order.items:
        print("\nOrder is empty.")
        return

    order.show_order()

    item_id = get_number("Enter item ID: ")

    if item_id not in order.items:
        print("Item not found in order.")
        return

    quantity = get_number("Enter new quantity (0 to remove): ")

    if quantity < 0:
        print("Invalid quantity.")
        return

    order.update_item(item_id, quantity)

    if quantity == 0:
        print("Item removed.")
    else:
        print("Quantity updated.")


def remove_item(order):
    if not order.items:
        print("\nOrder is empty.")
        return

    order.show_order()

    item_id = get_number("Enter item ID: ")

    if order.remove_item(item_id):
        print("Item removed from order.")
    else:
        print("Item not found.")