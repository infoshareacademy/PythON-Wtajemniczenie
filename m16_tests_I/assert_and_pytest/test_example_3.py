def anonymize_phone_number(phone_number: str) -> str:
    public_digits_num = 6
    phone_number = phone_number.replace("-", "")
    public_digits = phone_number[:public_digits_num]
    number_of_private_digits = len(phone_number) - public_digits_num
    private_digits = "-" * number_of_private_digits
    return f"{public_digits}{private_digits}"


def test_anonymize_phone_number_replace_digits_after_6_with_hyphens():
    # Nie najlepsze dane testowe
    phone_number = "111111111"
    anonymized_phone_number = anonymize_phone_number(phone_number)
    assert anonymized_phone_number == "1111111---"

