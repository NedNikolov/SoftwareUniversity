from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    __CAKE_PORTION = 200

    def __init__(self, name, price):
        super().__init__(name, self.__CAKE_PORTION, price)
