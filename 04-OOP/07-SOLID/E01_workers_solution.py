# You are provided with a code on which you have to apply the DIP (Dependency Inversion
# Principle) so that when adding new worker classes, the Manager class will work properly.
from abc import ABC, abstractmethod


class BaseWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(BaseWorker):

    @staticmethod
    def work():
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), \
            '`worker` must be of type {}'.format(BaseWorker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(BaseWorker):

    @staticmethod
    def work():
        print("I work very hard!!!")


# Test code/after

worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
