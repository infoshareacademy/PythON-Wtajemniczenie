from document_system.ui import ui_from_settings


def run_example() -> None:
    ui = ui_from_settings()
    ui.header_text = "Okno programu"
    ui.add_button("OK")
    ui.add_button("Anuluj")
    ui.render()


if __name__ == "__main__":
    run_example()
