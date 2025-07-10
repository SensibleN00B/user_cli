from typing import Any


class InputHandler:
    @staticmethod
    def handle_input(prompt: str, data_type: type = str, make_capital: bool = False) -> Any:
        while True:
            try:
                # I wanted to implement this construction to immediately return the first name\last name in uppercase,
                # so that in the console when handling errors they would also be displayed in uppercase.
                # But doesn't this violate the Single Responsibility Principle?

                # if data_type == str and make_capital:
                #     return data_type(input(prompt).capitalize())
                return data_type(input(prompt))
            except ValueError:
                print(f"Invalid input. Try again. Input must be {data_type.__name__}.")



