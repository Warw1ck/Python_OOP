class Shop:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def get_items_count(self):
        return len(self.products)





shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
