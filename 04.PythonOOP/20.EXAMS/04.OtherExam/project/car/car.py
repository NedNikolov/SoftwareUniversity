from abc import ABC, abstractmethod


class Car(ABC):
    _min_speed_limit = 0
    _max_speed_limit = 0

    @abstractmethod
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return

    @speed_limit.setter
    def speed_limit(self, value):
        if not self._min_speed_limit <= value <= self._max_speed_limit:
            raise ValueError(
                f"Invalid speed limit! Must be between {self._min_speed_limit} and {self._max_speed_limit}!")
        self.speed_limit = value

    def is_taken(self, boole=False):
        pass
