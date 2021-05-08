def outer_func(outer_var_1):
    def inner_func(inner_var_1):
        print("Dostęp do zmiennej lokalnej:", inner_var_1)
        print("Dostęp do zmiennej non-local (lokalna z kontekstu outer):", outer_var_1)
        print("Dostęp do zmiennej non-local (lokalna z kontekstu outer):", outer_var_2)
        nonlocal outer_var_3
        outer_var_3 = "CHANGED"
        print("Modyfikacja zmiennej z kontekstu outer:", outer_var_3)

    outer_var_2 = "|OUTER 2|"
    outer_var_3 = "|OUTER 3|"

    print("Na poziomie outer mamy: ", outer_var_1, outer_var_2, outer_var_3, sep="\n")
    inner_func("--inner-1--")
    print(
        "Po wywołaniu inner, na poziomie outer mamy: ",
        outer_var_1,
        outer_var_2,
        outer_var_3,
        sep="\n",
    )


def run_example():
    outer_func("|OUTER 1|")


if __name__ == "__main__":
    run_example()
