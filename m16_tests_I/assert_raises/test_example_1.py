import pytest


def anonymize_phone_number(phone_number: str) -> str:
    public_digits_num = 6
    phone_number = phone_number.replace("-", "")
    if len(phone_number) <= public_digits_num:
        raise ValueError(f"Nothing to anonymize - number is too short. Min len is {public_digits_num + 1}")
    public_digits = phone_number[:public_digits_num]
    number_of_private_digits = len(phone_number) - public_digits_num
    private_digits = "-" * number_of_private_digits
    return f"{public_digits}{private_digits}"

#
# def test_anonymize_phone_number_raises_value_error_when_number_is_too_short():
#     too_short_number = "123456"
#
#     with pytest.raises(ValueError):
#         anonymize_phone_number(too_short_number)
#
#
# def test_anonymize_phone_number_raises_value_error_when_number_with_hyphens_is_too_short():
#     too_short_number = "1-2-3-4-5-6"
#
#     with pytest.raises(ValueError):
#         anonymize_phone_number(too_short_number)



def test_anonymize_phone_number_raises_value_error_when_number_is_too_short():
    too_short_number = "123456"

    with pytest.raises(ValueError) as error:
        anonymize_phone_number(too_short_number)
    assert str(error.value) == "Nothing to anonymize - number is too short. Min len is 7"


def test_anonymize_phone_number_raises_value_error_when_number_with_hyphens_is_too_short():
    too_short_number = "1-2-3-4-5-6"

    with pytest.raises(ValueError):
        anonymize_phone_number(too_short_number)
