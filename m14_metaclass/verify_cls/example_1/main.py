from example_system import mail_sender
from example_system.emails import WelcomeEmail, RegistrationEmail
from example_system.emails_init_check import WelcomeEmailInit, RegistrationEmailInit


def run_example() -> None:
    print("Welcome and activation emails...")
    welcome_email = WelcomeEmail(
        first_name="Jan", last_name="Kowalski", signature="Pozdrawiam, Mikołaj Lewandowski"
    )
    registration_email = RegistrationEmail(username="janek", activation_url="...")

    # welcome_email = WelcomeEmailInit(
    #     first_name="Jan", last_name="Kowalski", signature="Pozdrawiam, Mikołaj Lewandowski"
    # )
    # registration_email = RegistrationEmailInit(username="janek", activation_url="...")

    jan_email = "jan-kowalski@..."
    mail_sender.send_email("mailing@pyjazz.pl", jan_email, welcome_email)
    mail_sender.send_email("mailing@pyjazz.pl", jan_email, registration_email)


if __name__ == "__main__":
    run_example()
