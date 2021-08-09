from shop.last_products import LastProducts


def run_example() -> None:
    last_products = LastProducts()
    last_products.add_watched_product("Namiot", "Turystyka")
    last_products.add_watched_product("Buty do biegania", "Bieganie")
    last_products.add_watched_product("Pompka do roweru", "Rower")
    last_products.add_watched_product("Opona", "Rower")
    last_products.add_watched_product("Buty do biegania", "Bieganie")

    last_products.print_last_products_in_order()


if __name__ == '__main__':
    run_example()