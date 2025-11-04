import numpy as np

class StatsService:
    def __init__(self, inventory):
        # inventory should be a dict {product_name: Product}
        self.inventory = inventory

    def average_price(self):
        prices = [p.price for p in self.inventory.values()]
        return np.mean(prices) if prices else 0

    def most_expensive_item(self):
        prices = [(p.name, p.price) for p in self.inventory.values() if p.price is not None]
        return max(prices, key=lambda x: x[1]) if prices else None

    def total_stock_count(self):
        stocks = [p.stock for p in self.inventory.values()]
        return np.sum(stocks)

    def total_value_per_product(self):
        return {p.name: p.stock * p.price for p in self.inventory.values()}

    def tag_based_stats(self, tag):
        tagged = [p for p in self.inventory.values() if tag in p.tags]
        if not tagged:
            return None
        avg_price = np.mean([p.price for p in tagged])
        total_value = np.sum([p.price * p.stock for p in tagged])
        return avg_price, total_value
