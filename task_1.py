from abc import abstractmethod, ABC
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter("%(message)s")

ch.setFormatter(formatter)

logger.addHandler(ch)

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, area):
        self.make = make
        self.model = model
        self.area = area

    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make, model, area):
        self.make = make
        self.model = model
        self.area = area

    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Мотор заведено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def __init__(self):
        self.area = "(US Spec)"

    def create_car(self, make, model):
        return Car(make, model, self.area)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.area)


class EUVehicleFactory(VehicleFactory):
    def __init__(self):
        self.area = "(EU Spec)"

    def create_car(self, make, model):
        return Car(make, model, self.area)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.area)


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()