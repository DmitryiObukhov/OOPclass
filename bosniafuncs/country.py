class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other_country):
        new_name = f"{self.name} & {other_country.name}"
        new_popul = self.population + other_country.population
        return Country(new_name, new_popul)
