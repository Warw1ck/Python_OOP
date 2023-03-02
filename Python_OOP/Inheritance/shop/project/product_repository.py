from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
            return product
        except StopIteration:
            return

    def remove(self, product_name):
        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
            self.products.remove(product)
        except StopIteration:
            return

    def __repr__(self):
        return '\n'.join([f"{product.name}: {product.quantity}"for product in self.products])
