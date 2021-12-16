from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        pass

    def create_driver(self, driver: Driver):
        for driver in self.drivers:
            if driver == driver.__name:
                raise Exception(f"Driver {driver.__name} is already created!")

        self.drivers.append(driver)
        return f"Driver {driver.__name} is created."

    def create_race(self, race: Race):
        for race in self.races:
            if race == race.__name:
                raise Exception(f"Race {race.__name} is already created!")

        self.races.append(race)

    def add_car_to_driver(self, driver_name: str, car_type: str):
        pass

    def add_driver_to_race(self, race_name: str, driver_name: str):
        pass

    def start_race(self, race_name: str):
        pass
