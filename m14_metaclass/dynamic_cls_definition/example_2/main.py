from example_system.email_sender import email_sender_provider
from example_system.message import Message


def run_example() -> None:
    email_content = "Hej! Co słychać?"
    message = Message(
        from_address="mikolaj@pyjazz.pl", to_address="help@pyjazz.pl", content=email_content
    )
    sender_cls = email_sender_provider()
    sender = sender_cls()
    sender.send_message(message)


if __name__ == "__main__":
    run_example()
