from tickets_ordering import actions


def run_example():
    tickets_number = int(input("Podaj liczbę biletów: "))
    actions.order_tickets(tickets_number)


if __name__ == "__main__":
    run_example()
