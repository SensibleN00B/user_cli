from input_handler import InputHandler
from user_repository import UserRepository
from user_service import UserService, IUserService


def run_cli(user_service: IUserService) -> None:
    command_mapper = {
        "create_user": user_service.create_user,
        "read_user": user_service.read_user,
        "update_user": user_service.update_user,
        "delete_user": user_service.delete_user,
    }

    command_mapper["help"] = lambda: user_service.print_help(command_mapper)

    while True:
        command_input = InputHandler.handle_input("Enter the command: ", str)

        if action := command_mapper.get(command_input):
            action()
        elif command_input == "exit":
            break
        else:
            print(f"Unknown command: {command_input}")


if __name__ == '__main__':
    user_repository = UserRepository()
    user_service = UserService(repository=user_repository)
    run_cli(user_service=user_service)
