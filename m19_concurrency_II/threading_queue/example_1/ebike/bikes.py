import queue

from ebike.printer import print_text
from ebike.bikes_store import BikesStore

bikes_requests_queue: queue.Queue[str] = queue.Queue()


def rent_a_bike(renter_name: str) -> None:
    bikes_requests_queue.put(renter_name)


def bikes_manager() -> None:
    while True:
        renter_name = bikes_requests_queue.get()
        if BikesStore.NUMBER_OF_BIKES_AVAILABLE > 0:
            BikesStore.NUMBER_OF_BIKES_AVAILABLE -= 1
            print_text(f"{renter_name} just rented a bike!")
        else:
            print_text(f"There is no bike for {renter_name}")
        bikes_requests_queue.task_done()
