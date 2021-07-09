from example_system.order import Order
from example_system.payment_service.client import PaymentDTO, PaymentClient
from example_system.user import User, PaymentMethodType


def pay_for_order(user: User, order: Order, client: PaymentClient) -> None:
    amount_to_be_paid = order.total_amount()
    payment_method = user.default_payment_method

    payment_id_prefix = _payment_identifier_prefix(payment_method.payment_type)
    payment_dto = PaymentDTO(
        identifier=f"{payment_id_prefix}-{payment_method.global_identifier}",
        amount=amount_to_be_paid,
    )
    result = client.pay(payment_dto)

    if result.success:
        process_successful_payment(result.context_info)
    else:
        process_failed_payment(result.context_info)


def _payment_identifier_prefix(payment_method_type: PaymentMethodType) -> str:
    if payment_method_type is PaymentMethodType.CREDIT_CARD:
        return "C"
    if payment_method_type is PaymentMethodType.MOBILE:
        return "M"
    if payment_method_type is PaymentMethodType.E_TRANSFER:
        return "T"
    raise ValueError("Not allowed payment method type!")


def process_successful_payment(payment_info: str) -> None:
    pass


def process_failed_payment(payment_info: str) -> None:
    pass
