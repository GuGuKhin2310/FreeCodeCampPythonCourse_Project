class Planet:

    def __init__(self,name,planet_type,star):
        self.name = name
        self.planet_type = planet_type
        self.star = star

        if not all(isinstance(x, str) for x in [name, planet_type, star]):
            raise TypeError(f"name, planet type, and star must be strings")
        if not name or not planet_type or not star:
            raise ValueError(f"name, planet_type, and star must be non-empty strings")

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

planet_1 = Planet("Mercury","Terrestrial","Sun")
planet_2 = Planet("Jupiter","Gas Giant","Sun")
planet_3 = Planet("Neptune","Ice Giant","Sun")

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
print(planet_1)
print(planet_2)
print(planet_3)
