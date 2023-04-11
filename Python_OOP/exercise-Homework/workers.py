from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        ...


class Worker(BaseWorker):

    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if isinstance(worker, BaseWorker):
            self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(BaseWorker):

    def work(self):
        print("I work very hard!!!")



worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")