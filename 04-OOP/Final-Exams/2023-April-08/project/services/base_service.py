from abc import ABC, abstractmethod
from project.robots.base_robot import BaseRobot
from typing import List


class BaseService(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots: List[BaseRobot] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    @property
    @abstractmethod
    def service_type(self) -> str:
        pass

    def details(self):
        result = f"{self.name} {self.service_type} Service:\n"
        robots_names = [r.name for r in self.robots]
        result_robots = f"Robots: " \
                        f"{' '.join(robots_names) if len(self.robots) > 0 else 'none'}"
        return result + result_robots
