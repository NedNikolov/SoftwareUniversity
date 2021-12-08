class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget:
            return f"Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return f"Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__worker_capacity:
            return f"Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        worker_sum = sum([x.salary for x in self.workers])

        if worker_sum > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= worker_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals():
        pass

    def profit(amount):
        pass

    def animals_status():
        pass
