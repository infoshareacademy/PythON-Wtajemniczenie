from typing import Protocol, ClassVar, Any, Optional


class Email(Protocol):
    TEMPLATE: ClassVar[str]
    context: dict[str, str]


class EmailMeta(type):
    def __new__(mcs, name: str, bases: tuple[type], class_dict: dict[str, Any]) -> Any:
        if not bases:
            return super().__new__(mcs, name, bases, class_dict)
        template: Optional[str] = class_dict.get("TEMPLATE", None)
        if not template:
            raise ValueError("Email class must provide path to the template")

        if not isinstance(template, str):
            raise ValueError("Path to email template must be a str instance")

        if not template.endswith(".html") and not template.endswith(".doc"):
            raise ValueError("Email template must be either html or doc")

        return super().__new__(mcs, name, bases, class_dict)


class AbstractEmail(metaclass=EmailMeta):
    pass


class WelcomeEmail(AbstractEmail):
    TEMPLATE: ClassVar[str] = "/statics/mail_templates/welcome.html"

    def __init__(self, first_name: str, last_name: str, signature: str) -> None:
        self.context = {
            "recipient_name": f"{first_name} {last_name}",
            "signature": signature,
        }


class RegistrationEmail(AbstractEmail):
    TEMPLATE: ClassVar[str] = "/statics/mail_templates/register.doc"

    def __init__(self, username: str, activation_url: str) -> None:
        self.context = {
            "username": username,
            "activation_url": activation_url,
        }
