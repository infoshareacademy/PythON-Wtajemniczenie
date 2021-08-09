from queue_system.customers_queue import CustomersQueue


def run_example() -> None:
    customers_queue = CustomersQueue()
    customers_queue.queue_customer("Jan")
    customers_queue.queue_customer("Alicja")
    customers_queue.queue_customer("Paweł")
    customers_queue.queue_customer("Karolina")

    print(customers_queue)
    print(customers_queue.deque_next_customer())

    print(customers_queue)
    customers_queue.queue_vip_customer("Aleksander")
    customers_queue.queue_customer("Jakub")
    print(customers_queue)

    print(customers_queue.deque_next_customer())
    print(customers_queue.deque_next_customer())
    print(customers_queue.deque_next_customer())
    print(customers_queue)


if __name__ == "__main__":
    run_example()
