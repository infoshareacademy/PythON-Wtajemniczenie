from example_system import actions
from example_system.order import Order
from example_system.payment_service.mocky_client import MockyClient
from example_system.payment_service.remote_client import RemoteClient
from example_system.user import PaymentMethod, PaymentMethodType, User


def run_example() -> None:
    credit_card = PaymentMethod(
        payment_type=PaymentMethodType.CREDIT_CARD, global_identifier="ABC-ZYY"
    )
    transfer = PaymentMethod(payment_type=PaymentMethodType.E_TRANSFER, global_identifier="CCAD-33")
    mobile = PaymentMethod(payment_type=PaymentMethodType.MOBILE, global_identifier="45694fefef")

    user = User(name="Mikołaj", payment_methods=[credit_card, transfer, mobile])

    actions.pay_for_order(user, order=Order("Test-order"), client=RemoteClient())
    # actions.pay_for_order(user, order=Order("Test-order"), client=MockyClient())


if __name__ == "__main__":
    run_example()
