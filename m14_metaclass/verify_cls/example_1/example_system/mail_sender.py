from typing import Any

from example_system.emails import Email


def send_email(src_address: str, dst_address: str, email: Email) -> None:
    print(f"Sending email from {src_address} to {dst_address}")
    template = _load_template(email.TEMPLATE)
    ...


def _load_template(template_path: str) -> Any:
    pass

