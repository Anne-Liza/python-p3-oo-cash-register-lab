class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.transactions = []  # Track transaction amounts to support voiding
    
    def add_item(self, title, price, quantity=1):
        """Add items to the register with the given title, price, and quantity."""
        if isinstance(price, (int, float)) and isinstance(quantity, int):
            # Add the item and its cost to the total
            self.total += price * quantity
            # Add item to the list of items, considering quantity
            for _ in range(quantity):
                self.items.append(title)
            # Record the transaction amount
            self.transactions.append(price * quantity)
        else:
            raise ValueError("Price must be a number and quantity must be an integer")
    
    def apply_discount(self):
        """Apply discount to the total and print a success message."""
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        """Void the last transaction."""
        if self.transactions:
            last_transaction = self.transactions.pop()
            self.total -= last_transaction
            # Remove the last item from the items list
            # To find and remove the last added item based on the last transaction
            for item in reversed(self.items):
                if last_transaction >= self.transactions[-1] if self.transactions else 0:
                    self.items.remove(item)
                    break
