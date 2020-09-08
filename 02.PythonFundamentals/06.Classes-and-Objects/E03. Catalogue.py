class Calatogue:
    list = []

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        for prod in self.products:
            word = self.products[prod]
            if first_letter == chr(word[0]):
                list.append(word)
            return list

    def __repr__(self):
        print(f"Items in the {self.name} catalogue:\n")
        return f""