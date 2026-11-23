



# =====================================
# E-COMMERCE PRODUCT MANAGEMENT SYSTEM
# =====================================

# STEP 1: Create the Product class

class Product:

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


# STEP 2: Create the ProductManager class

class ProductManager:

    def __init__(self):
        self.products = []


    # STEP 3: Add a new product

    def add_product(self, product_id, name, price):

        if type(product_id) != int or product_id <= 0:
            print("Invalid product ID!")
            return

        if not isinstance(name, str) or not name.strip():
            print("Invalid product name!")
            return

        if (not isinstance(price, (int, float))
                or isinstance(price, bool) or price < 0):
            print("Invalid product price!")
            return

        if self.binary_search(product_id) is not None:
            print("Product ID already exists!")
            return

        new_product = Product(product_id, name, price)

        self.products.append(new_product)

        self.products.sort(
            key=lambda product: product.product_id
        )

        print("Product added successfully!")


    # STEP 4: Implement Binary Search

    def binary_search(self, product_id):

        low = 0
        high = len(self.products) - 1

        while low <= high:

            mid = (low + high) // 2

            current_id = self.products[mid].product_id

            if current_id == product_id:
                return self.products[mid]

            elif current_id < product_id:
                low = mid + 1

            else:
                high = mid - 1

        return None


    # STEP 5: Update product price

    def update_price(self, product_id, new_price):

        if (not isinstance(new_price, (int, float))
                or isinstance(new_price, bool) or new_price < 0):
            print("Invalid price!")
            return

        product = self.binary_search(product_id)

        if product is not None:
            product.price = new_price
            print("Price updated successfully!")

        else:
            print("Product not found!")


    # STEP 6: Display all products

    def display_products(self):

        if len(self.products) == 0:
            print("No products available.")
            return

        print("\n===== AVAILABLE PRODUCTS =====")

        for product in self.products:

            print("Product ID:", product.product_id)
            print("Product Name:", product.name)
            print("Product Price:", product.price)
            print("------------------------------")


# STEP 7: Test the system

manager = ProductManager()

# Add products
manager.add_product(103, "Laptop", 2500)
manager.add_product(101, "Phone", 1200)
manager.add_product(105, "Keyboard", 150)
manager.add_product(102, "Mouse", 50)
manager.add_product(104, "Headphones", 200)

# Display all products
manager.display_products()

# Search for a product
print("\n===== SEARCH PRODUCT =====")

result = manager.binary_search(103)

if result is not None:
    print("Product found!")
    print("Name:", result.name)
    print("Price:", result.price)
else:
    print("Product not found!")

# Update product price
print("\n===== UPDATE PRICE =====")

manager.update_price(103, 2800)

# Display products after updating
manager.display_products()






    

