class Country2:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = f"{self.name} & {other_country.name}"
        combined_population = self.population + other_country.population
        return Country2(combined_name, combined_population)
