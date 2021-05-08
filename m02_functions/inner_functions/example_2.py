def get_emails_to_be_notified(prefix):
    def generate_email(address):
        return f"{prefix}-{address}@{domain}"

    domain = "new-movie-example-domain.com.pl"

    # Inner function jest widoczna w tym zakresie
    admin_email = generate_email("admin")
    info_email = generate_email("info")
    contact_email = generate_email("contact")
    return [admin_email, info_email, contact_email]


def run_example():
    emails = get_emails_to_be_notified("notify")
    print(emails)

    # Brak dostępu do funkcji
    # admin = generate_email("admin", "some-other-example-domain.com.pl")


if __name__ == "__main__":
    run_example()
