def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Juan", "lastname": "Ramírez"}

    super_list = [
        {"firstname": "Juan", "lastname": "Ramírez"},
        {"firstname": "Miguel", "lastname": "García"},
        {"firstname": "Sofía", "lastname": "González"},
        {"firstname": "Sara", "lastname": "Pérez"},
        {"firstname": "Laura", "lastname": "Martínez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f"{key} --> {value}")

    for i in super_list:
        print(f"{i['firstname']} {i['lastname']}")

if __name__ == "__main__":
    run()