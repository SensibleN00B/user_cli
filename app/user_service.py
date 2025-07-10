from abc import ABC, abstractmethod
from unittest.mock import Mock

from pydantic import ValidationError

from input_handler import InputHandler
from user_model import User
from user_repository import IUserRepository


class IUserService(ABC):
    @abstractmethod
    def create_user(self) -> None:
        pass

    @abstractmethod
    def read_user(self) -> None:
        pass

    @abstractmethod
    def update_user(self) -> None:
        pass

    @abstractmethod
    def delete_user(self) -> None:
        pass

    @staticmethod
    @abstractmethod
    def print_help(commands: dict) -> None:
        pass


class UserService(IUserService):
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    @staticmethod
    def print_help(commands: dict):
        print("Available commands:")
        for cmd in commands:
            print(f"- {cmd}")
        print("- exit")

    def create_user(self) -> None:
        name = InputHandler.handle_input("Enter the name: ", str)
        surname = InputHandler.handle_input("Enter the surname: ", str)
        age = InputHandler.handle_input("Enter the age: ", int)

        try:
            user = User(name=name, surname=surname, age=age)
        except ValidationError as e:
            print(e)
            return

        self.repository.write_user(user)

        print("User created successfully")

    def read_user(self) -> None:
        surname = InputHandler.handle_input("Enter the surname: ", str, True)
        user = self.repository.get_user(surname)

        if not user:
            print(f"User with surname {surname.capitalize()} not found")
            return

        print(user)

    def update_user(self) -> None:
        surname = InputHandler.handle_input("Enter the surname: ", str, True)
        user = self.repository.get_user(surname)

        if not user:
            print(f"User with surname {surname.capitalize()} not found")
            return

        new_name = InputHandler.handle_input("Enter the new name: ", str)
        new_surname = InputHandler.handle_input("Enter the new surname: ", str, True)
        new_age = InputHandler.handle_input("Enter the new age: ", int)

        try:
            new_user = User(name=new_name, surname=new_surname, age=new_age)
        except ValidationError as e:
            print(e)
            return

        result = self.repository.change_user(surname, new_user)

        if result:
            print(f"User with surname {new_user.surname} updated")
        else:
            print(f"User with surname {new_user.surname} not updated")

    def delete_user(self) -> None:
        surname = InputHandler.handle_input("Enter your surname: ", str, True)
        user = self.repository.get_user(surname)

        if not user:
            print(f"User with surname {surname.capitalize()} not found")
            return

        result = self.repository.remove_user(surname)

        if result:
            print(f"User with surname {surname.capitalize()} deleted")
        else:
            print(f"User with surname {surname.capitalize()} not deleted")
