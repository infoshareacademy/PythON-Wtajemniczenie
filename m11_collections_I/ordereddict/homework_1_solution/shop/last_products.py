from collections import OrderedDict


class LastProducts:

    def __init__(self, max_number_of_products: int = 3) -> None:
        self.max_number_of_products = max_number_of_products
        self.products: OrderedDict[str, str] = OrderedDict()

    def add_watched_product(self, product_name: str, product_category: str) -> None:
        if product_name in self.products:
            self.products.move_to_end(product_name)
        else:
            self.products[product_name] = product_category
        if len(self.products) > self.max_number_of_products:
            self.products.popitem(last=False)

    def print_last_products_in_order(self) -> None:
        for product, category in reversed(self.products.items()):
            print(product, category)


