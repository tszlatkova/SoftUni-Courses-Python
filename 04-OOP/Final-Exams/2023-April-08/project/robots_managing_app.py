from typing import List
from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOTS_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def find_service(self, service_name):
        return next((s for s in self.services if s.name == service_name), None)

    def add_service(self, type: str, name: str):
        if type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")
        new_service = self.VALID_SERVICES[type](name)
        self.services.append(new_service)
        return f"{type} is successfully added."

    def add_robot(self, type: str, name: str, kind: str, price: float):
        if type not in self.VALID_ROBOTS_TYPES:
            raise Exception("Invalid robot type!")
        new_robot = self.VALID_ROBOTS_TYPES[type](name, kind, price)
        self.robots.append(new_robot)
        return f"{type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next((r for r in self.robots if r.name == robot_name), None)
        service = self.find_service(service_name)

        if isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."
        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.find_service(service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if not robot:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_service(service_name)
        number_of_robots_fed = 0
        for r in service.robots:
            r.eating()
            number_of_robots_fed += 1
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = self.find_service(service_name)
        total_price = 0
        for r in service.robots:
            total_price += r.price
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])
