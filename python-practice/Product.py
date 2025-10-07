class Product:
    def __init__(self, name, price,category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}"