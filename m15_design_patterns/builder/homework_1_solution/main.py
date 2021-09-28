from document_system.form_builder import FormBuilder


def run_example() -> None:
    form_builder = FormBuilder()
    form_builder.build_basic_personal_section(heading="Please provide personal details")
    form_builder.build_email_section()
    form_builder.build_ue_regulatory_info()
    only_personal_data_ue_form = form_builder.get_form()
    print(20 * "-")
    print(only_personal_data_ue_form.render())
    print(20 * "-")

    form_builder.reset()
    form_builder.build_basic_personal_section(heading="Personal details")
    form_builder.build_phone_section()
    form_builder.build_details_section(heading="Details information")
    form_builder.build_usa_regulatory_info()
    usa_form_with_details = form_builder.get_form()
    print(usa_form_with_details.render())
    print(20 * "-")


if __name__ == "__main__":
    run_example()
