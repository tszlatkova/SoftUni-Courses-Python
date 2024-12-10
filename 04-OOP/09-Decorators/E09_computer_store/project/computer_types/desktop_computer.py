from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    @property
    def available_processors(self):
        return {"AMD Ryzen 9 5950X": 500,
                "Intel Core i9-11900H": 600,
                "Apple M1 Pro": 1800}

    @property
    def max_ram(self) -> int:
        return 128

    def __str__(self):
        return "desktop computer"
