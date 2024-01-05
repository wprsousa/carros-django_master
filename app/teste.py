class FoodDeliverySystem:
    order_id = 0
    orders_log = {}

    def __init__(self):
        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery": 350,
            "Soda": 30,
            "Wine": 500,
        }
        self.bill_amount = 0
        self.order_id = 0

    def display_menu(self):
        """
        Return the menu details in the following format:
        Burger  |  150
        Pizza   |  250
        Pasta   |  200
        Salad   |  120
        Beverages  |  130
        Noodles  |  150
        Sushi   |  270
        Bakery  |  350
        """
        menu_str = ""
        for key, value in self.menu.items():
            menu_str += f"{key.ljust(12)} | {value}\n"

        return menu_str

    def place_order(self, customer_name, order_items):
        """
        Return orders log after order placed by a customer with status as "Placed", otherwise return "order placement failed"
        Format:
        orders_log = {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Placed}}
        """
        if not order_items:
            return "Order placement failed. No items in the order."

        # Generate a unique order_id
        order_id = self.order_id
        self.order_id += 1

        # Create a new entry in the orders log
        self.orders_log[order_id] = {
            "customer_name": customer_name,
            "order_items": order_items,
            "status": "Placed",
        }

        # Return the updated orders log
        return self.orders_log

    def pickup_order(self, order_id):
        """
        status: Picked Up
        Return the changed status of the order: {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Picked Up"}}
        """
        if order_id in self.orders_log:
            self.orders_log[order_id]["status"] = "Picked Up"
            return self.orders_log
        else:
            return f"Order pickup failed. Order with ID {order_id} not found."

    def deliver_order(self, order_id):
        """
        status: Delivered
        Return the delivery status of order (delivered or not delivered)
        """
        return None

    def modify_order(self, order_id, new_items):
        """
        Return the modified order with items available in menu only if the order is not picked up:
        {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity", new_items}, status = "Placed"}}
        """
        return None

    def generate_bill(self, order_id):
        """
        if the sum of all items > 1000
        Amount = Sum of all items placed + 10% of total sum
        if sum of all items < 1000
        Amount = Sum of all items placed + 5% of total sum
        Return the total bill amount
        """
        return None

    def cancel_order(self, order_id):
        """
        Cancel order items for the customer if the order is not Picked Up and remove order details from orders log
        Return the order logs. For example, if you have 3 orders, but the third order is cancelled, you need remove this from the orders log and just return the first two orders:
        {1: {"customer_name":"clientA", "order_items":{"Burger":1,"Pasta":2},"status":"Delivered"}, 2: {"customer_name":"clientB", "order_items":{"Salad":2,"Sushi":4, "Beverages":6, "Bakery":2},"status":"Placed"}}
        """
        return None


menu = FoodDeliverySystem()


customer_name = "Mary Smith"
order_items = {"Burger": 2, "Pizza": 1, "Salad": 1}
order_result = menu.place_order(customer_name, order_items)

customer_name2 = "Mary Smithhhh"
order_items2 = {"Burger": 2, "Pizza": 1, "Salad": 1}
order_result2 = menu.place_order(customer_name2, order_items2)

customer_name3 = "Mary Poppins"
order_items3 = {"Burger": 2, "Pizza": 1, "Salad": 1}
order_result3 = menu.place_order(customer_name3, order_items3)
# print("Order placed:", order_result3)

order_id_to_pickup = 1
pickup_result = menu.pickup_order(order_id_to_pickup)
print("Order picked up:", pickup_result)