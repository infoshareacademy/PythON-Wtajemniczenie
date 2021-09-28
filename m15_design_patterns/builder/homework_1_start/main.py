from document_system.complex_form import ComplexForm, FormType


def run_example() -> None:
    only_personal_data_ue_form = ComplexForm(
        personal_section_heading="Please provide personal details",
        email_input=True,
        phone_input=False,
        details_section=False,
        details_section_heading=None,
        form_type=FormType.UE,
    )
    print(20 * "-")
    print(only_personal_data_ue_form.render())
    print(20 * "-")

    usa_form_with_details = ComplexForm(
        personal_section_heading="Personal details",
        email_input=False,
        phone_input=True,
        details_section=True,
        details_section_heading="Details information",
        form_type=FormType.USA,
    )
    print(usa_form_with_details.render())
    print(20 * "-")


if __name__ == "__main__":
    run_example()
