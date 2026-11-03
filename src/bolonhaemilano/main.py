import sys
from menu import Menu


class Main:

    @staticmethod
    def main(args: list[str]) -> None:
        menu = Menu()
        menu.executar()


if __name__ == "__main__":
    Main.main(sys.argv[1:])