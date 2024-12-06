from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer
from typing import List


class Gym:

    def __init__(self) -> None:
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def __add_object(object, object_collection: list) -> None:
        if object not in object_collection:
            object_collection.append(object)

    @staticmethod
    def __find_object(object_collection, subscription):
        return next((obj for obj in object_collection
                     if obj.id == subscription.customer_id), None)

    def add_customer(self, customer: Customer) -> None:
        self.__add_object(customer, self.customers)

    def add_trainer(self, trainer: Trainer) -> None:
        self.__add_object(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment) -> None:
        self.__add_object(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        self.__add_object(plan, self.plans)

    def add_subscription(self, subscription: Subscription) -> None:
        self.__add_object(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int) -> str:
        s = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = self.__find_object(self.customers, s)
        trainer = self.__find_object(self.trainers, s)
        equipment = self.__find_object(self.equipment, s)
        plan = self.__find_object(self.plans, s)
        info_subscription = [s, customer, trainer, equipment, plan]
        return '\n'.join([x.__repr__() for x in info_subscription])
