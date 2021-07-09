from datetime import datetime

from example_system.payment_service.client import PaymentDTO, TransactionResult


class RemoteClient:
    def pay(self, payment_data: PaymentDTO) -> TransactionResult:
        secret_key = ...
        request_payload = {
            "client_key": secret_key,
            "identifier": payment_data.identifier,
            "amount": payment_data.amount,
            "transaction_init_datetime": datetime.now().isoformat(),
        }
        # Send payload
        # Handle errors
        # Parse results
        success = True
        context_data = ""
        return TransactionResult(success, context_data)
