from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route
from project.user import User

from typing import List


class ManagingApp:

    VALID_TYPE_VEHICLES = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = next((u for u in self.users if
                     driving_license_number == u.driving_license_number), None)
        if user:
            return f"{driving_license_number} has already been registered to " \
                   f"our platform."
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under " \
               f"DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str,
                       license_plate_number: str):

        if vehicle_type not in self.VALID_TYPE_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        vehicle = next((v for v in self.vehicles if
                        v.license_plate_number == license_plate_number), None)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."
        new_vehicle = self.VALID_TYPE_VEHICLES[vehicle_type](brand, model,
                                                             license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with " \
               f"LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = next((r for r in self.routes if r.start_point == start_point and
                      r.end_point == end_point), None)

        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added" \
                       f" to our platform."
            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added" \
                       f" to our platform."
            route.is_locked = True
        new_route = Route(start_point, end_point, length, route_id=len(self.routes)+1)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and " \
               f"available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int,  is_accident_happened: bool):

        user = [u for u in self.users if
                driving_license_number == u.driving_license_number][0]
        vehicle = [v for v in self.vehicles if
                   license_plate_number == v.license_plate_number][0]
        route = [r for r in self.routes if route_id == r.route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! " \
                   f"This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicle = [v for v in self.vehicles if v.is_damaged]
        damaged_vehicle = sorted(damaged_vehicle, key=lambda v: (v.brand, v.model))

        if len(damaged_vehicle) > count:
            damaged_vehicle = damaged_vehicle[:count]

        for v in damaged_vehicle:
            v.is_damaged = False
            v.recharge()

        return f"{len(damaged_vehicle)} vehicles were successfully repaired!"

    def users_report(self):
        result = "*** E-Drive-Rent ***\n"
        ordered_users = sorted(self.users, key=lambda u: -u.rating)
        users_info = '\n'.join([str(u) for u in ordered_users])
        return result + users_info
