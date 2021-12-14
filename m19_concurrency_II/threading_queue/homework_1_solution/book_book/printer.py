import queue

print_requests_queue: queue.Queue[str] = queue.Queue()


def print_text(text: str) -> None:
    print_requests_queue.put(text)


def printer_manager() -> None:
    while True:
        text = print_requests_queue.get()
        print(text)
        print_requests_queue.task_done()
