from project.drink.drink import Drink


class Tea(Drink):
    __TEA_PRICE = 2.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.__TEA_PRICE, brand)

