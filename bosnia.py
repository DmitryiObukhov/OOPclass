from bosniafuncs.country import Country
from bosniafuncs.magic import Country2

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.name + ' population is ', end='')
print(bosnia_herzegovina.population)

# magic method
bosnia = Country2('Bosnia', 10_000_000)
herzegovina = Country2('Herzegovina', 5_000_000)
bosnia_herzegovina2 = bosnia + herzegovina
print(bosnia_herzegovina2.name + ' population is ', end='')
print(bosnia_herzegovina2.population)
