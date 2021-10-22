def anonymize_phone_number(phone_number: str) -> str:
    public_digits_num = 6
    phone_number = phone_number.replace("-", "")
    public_digits = phone_number[:public_digits_num]
    number_of_private_digits = len(phone_number) - public_digits_num
    private_digits = "-" * number_of_private_digits
    return f"{public_digits}{private_digits}"


def test_anonymize_phone_number_replace_digits_after_6_with_hyphens():
    # Given (setup)
    phone_number = "123456789"
    # When (do what we test)
    anonymized_phone_number = anonymize_phone_number(phone_number)
    # Then (check what state is required)
    assert anonymized_phone_number == "123456---"


# def test_anonymize_phone_number_replace_digits_after_6_with_hyphens():
#     assert anonymize_phone_number("123456789")


def test_anonymize_phone_number_removes_hyphens_before_anonymization():
    phone_number_with_hyphens = "123-456-789"
    anonymized_phone_number = anonymize_phone_number(phone_number_with_hyphens)
    assert anonymized_phone_number == "123456---"


def test_anonymize_very_long_phone_number():
    very_long_phone_number = "123-456-789123456789"
    anonymized_phone_number = anonymize_phone_number(very_long_phone_number)
    assert anonymized_phone_number == "123456---"
