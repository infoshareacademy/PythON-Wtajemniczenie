from example_system.doc_renderer import render_document
from example_system.documents import SalesSummary, FinanceReport


def run_example() -> None:
    print("Documents!")
    finance_report = FinanceReport(data={})
    sales_summary = SalesSummary(top_text="Hello", some_data="...")

    render_document(finance_report)
    render_document(sales_summary)


if __name__ == "__main__":
    run_example()
