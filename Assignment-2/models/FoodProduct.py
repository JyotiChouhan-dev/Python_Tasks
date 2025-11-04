from models.Product import Product

class FoodProduct(Product):
    def __init__(self, name, stock, price, location, tags, expiry_date):
        super().__init__(name, stock, price, location, tags)
        self.expiry_date = expiry_date

    def describe(self):
        base_description = super().describe()
        return f"{base_description}, Expiry Date: {self.expiry_date}"