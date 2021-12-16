class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
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
        if len(self.workers) == self.__workers_capacity:
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

    def tend_animals(self):
        money_care_sum = sum([x.money_for_care for x in self.animals])

        if money_care_sum > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= money_care_sum
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals" + '\n'

        result += self.__get_animals_status_by_type('Lion')
        result += self.__get_animals_status_by_type('Tiger')
        result += self.__get_animals_status_by_type('Cheetah')

        return result.strip()

    def __get_animals_status_by_type(self, animal_type):
        animals = [str(x) for x in self.animals if x.__class__.__name__ == animal_type]
        result = f"----- {len(animals)} {animal_type}s:" + '\n'

        for animal in animals:
            result += animal
            result += '\n'

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers" + '\n'

        result += self.__get_worker_status_by_type('Keeper')
        result += self.__get_worker_status_by_type('Caretaker')
        result += self.__get_worker_status_by_type('Vet')

        return result.strip()

    def __get_worker_status_by_type(self, worker_type):
        workers = [str(x) for x in self.workers if x.__class__.__name__ == worker_type]
        result = f"----- {len(workers)} {worker_type}s:" + '\n'

        for worker in workers:
            result += worker
            result += '\n'

        return result




