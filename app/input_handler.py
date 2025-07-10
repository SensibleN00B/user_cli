from typing import Any


class InputHandler:
    @staticmethod
    def handle_input(prompt: str, data_type: type = str, make_capital: bool = False) -> Any:
        while True:
            try:
                # if data_type == str and make_capital:
                #     return data_type(input(prompt).capitalize())
                return data_type(input(prompt))
            except ValueError:
                print(f"Invalid input. Try again. Input must be {data_type.__name__}.")



