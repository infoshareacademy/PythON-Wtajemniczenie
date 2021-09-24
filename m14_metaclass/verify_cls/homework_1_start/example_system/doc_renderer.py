from example_system.documents import Document


def render_document(document: Document) -> None:
    print(f"Rendering document with template from {document.TEMPLATE_PATH}...")
