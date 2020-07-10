from termcolor import colored


class Item():
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return \
            f"""
                name: \"{self.name}\",
                description: \"{self.description}\",
            """

    def on_take(self):
        print(
            f"""
                You have picked {self.name}
            """
        )

    def on_drop(self):
        print(
            f"""
                You have dropped {self.name}
            """
        )