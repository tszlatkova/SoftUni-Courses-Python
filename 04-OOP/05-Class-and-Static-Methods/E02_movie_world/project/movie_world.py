from project.customer import Customer
from project.dvd import DVD
from typing import List


class MovieWorld:

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        c = next((c for c in self.customers if c.id == customer_id), None)  # Customer
        d = next((d for d in self.dvds if d.id == dvd_id), None)  # DVD

        if d.is_rented:
            if d in c.rented_dvds:
                return f"{c.name} has already rented {d.name}"
            return "DVD is already rented"
        if c.age < d.age_restriction:
            return f"{c.name} should be at least {d.age_restriction} to rent this movie"
        d.is_rented = True
        c.rented_dvds.append(d)
        return f"{c.name} has successfully rented {d.name}"

    def return_dvd(self, customer_id, dvd_id) -> str:
        c = next((c for c in self.customers if c.id == customer_id), None)
        d = next((d for d in c.rented_dvds if d.id == dvd_id), None)
        if d is None:
            return f"{c.name} does not have that DVD"
        d.is_rented = False
        c.rented_dvds.remove(d)
        return f"{c.name} has successfully returned {d.name}"

    def __repr__(self) -> str:
        customers_data = '\n'.join([c.__repr__() for c in self.customers])
        dvds_data = '\n'.join([d.__repr__() for d in self.dvds])
        return '\n'.join([customers_data, dvds_data])
