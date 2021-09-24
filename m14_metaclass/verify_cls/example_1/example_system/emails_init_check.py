from typing import Protocol, ClassVar


class Email(Protocol):
    TEMPLATE: ClassVar[str]
    context: dict[str, str]


def _validate_email_template(email_obj: Email) -> None:
    try:
        template = email_obj.TEMPLATE
    except AttributeError:
        raise ValueError("Email class must provide path to the template")

    if not isinstance(template, str):
        raise ValueError("Path to mail template must be a str instance")

    if not template.endswith(".html") and not template.endswith(".doc"):
        raise ValueError("Email template must be either html or doc")



class WelcomeEmailInit:

    TEMPLATE: ClassVar[str] = "/statics/mail_templates/welcome.html"

    def __init__(self, first_name: str, last_name: str, signature: str) -> None:
        _validate_email_template(self)
        self.context = {
            "recipient_name": f"{first_name} {last_name}",
            "signature": signature,
        }


class RegistrationEmailInit:
    TEMPLATE: ClassVar[str] = "/statics/mail_templates/register.doc"

    def __init__(self, username: str, activation_url: str) -> None:
        _validate_email_template(self)
        self.context = {
            "username": username,
            "activation_url": activation_url,
        }
