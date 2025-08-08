from dataclasses import dataclass
from typing import Dict


# 1. Define the custom exception as instructed.
#    The exercise specifies inheriting from Exception, which is fine for this purpose.
class ProductNotFoundException(Exception):
    """
    Raised when a product with the specified ID is not found.
    This exception takes a product_id.
    """

    def __init__(self, product_id):
        # We store the product_id for later access in the exception handler.
        self.product_id = product_id
        # We call the parent class constructor (Exception) with a clear message.
        super().__init__(f"Product with ID '{product_id}' not found.")


# dummy Product class
@dataclass
class Product:
    name: str


# 2. Create the Inventory class as instructed.
@dataclass
class Inventory:
    products: Dict[int, Product]

    # 3. Implement get_product method to raise the exception.
    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product by its ID.
        If the product is not found, raises a ProductNotFoundException.
        """
        if product_id not in self.products:
            # Here is where you raise the custom exception.
            # We create a new instance of our custom exception and pass the product_id.
            raise ProductNotFoundException(product_id)

        return self.products[product_id]


# --- Test code (as per the exercise instructions) ---

prod1 = Product("cat")
prod2 = Product("shoe")
prod3 = Product("horse")

products = {1: prod1, 2: prod2, 3: prod3}
inventory = Inventory(products)

print("Inventory created with products:", inventory.products)
print("=" * 40)

# 4. Test getting existing products
print("Testing an existing product (ID 1):")
try:
    product_one = inventory.get_product(1)
    print(f"Success: Found product '{product_one.name}'.")
except ProductNotFoundException as e:
    # This block should not be executed.
    print(f"Error (should not happen): {e}")

print("=" * 40)

# 4. Test getting non-existing products, handling the exception
print("Testing a non-existing product (ID 7):")
try:
    product_seven = inventory.get_product(7)
    # This line should not be reached if the exception is raised.
    print(f"Success: Found product '{product_seven.name}'.")
except ProductNotFoundException as e:
    # This is the correct place to catch and handle the exception.
    print(f"Caught the expected error: {e}")
    print(f"Details from the exception object: The ID was {e.product_id}")
except Exception as e:
    # This block is a good practice for catching any other unexpected errors.
    print(f"Caught an unexpected error: {e}")
