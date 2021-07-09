import json
from example_system.payment_service.client import PaymentDTO, TransactionResult


class MockyClient:
    def pay(self, payment_data: PaymentDTO) -> TransactionResult:
        mocky_info = {
            "success": True,
            "transaction-id": "JPFWJAP38ejdsr3Zfef3",
            "additional-data": ""
        }
        return TransactionResult(success=True, context_info=json.dumps(mocky_info))
