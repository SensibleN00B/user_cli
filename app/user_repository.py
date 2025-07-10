import fileinput
from abc import ABC, abstractmethod

from user_model import User


class IUserRepository(ABC):
    @abstractmethod
    def write_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user(self, surname: str) -> User:
        pass

    @abstractmethod
    def change_user(self, surname: str, user: User) -> None:
        pass

    @abstractmethod
    def remove_user(self, surname: str) -> None:
        pass


class UserRepository(IUserRepository):

    @staticmethod
    def check_surname_in_line(surname: str, line: str) -> bool:
        return surname.capitalize() == line.split("|")[1]

    def __init__(self, file_name: str = "users.txt") -> None:
        self.file_name = file_name

    def write_user(self, user: User) -> None:
        with open(self.file_name, "a") as file:
            file.write(user.to_row())

    def get_user(self, surname: str) -> User | None:
        with open(self.file_name, "r") as file:
            for line in file:
                if self.check_surname_in_line(surname=surname, line=line):
                    name, surname, age = line.split("|")
                    return User(name=name, surname=surname, age=int(age))
        return None

    def change_user(self, surname: str, new_user: User) -> bool:
        updated = False

        for line in fileinput.input(self.file_name, inplace=True):
            if self.check_surname_in_line(surname=surname, line=line):
                print(new_user.to_row(), end="")
                updated = True
            else:
                print(line, end="")

        return updated

    def remove_user(self, surname: str) -> bool:
        deleted = False

        for line in fileinput.input(self.file_name, inplace=True):
            if self.check_surname_in_line(surname=surname, line=line):
                print("", end="")
                deleted = True
            else:
                print(line, end="")

        return deleted
