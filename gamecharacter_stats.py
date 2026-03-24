class GameCharacter:
    def __init__(self,name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self,value):
        if value < 0:
            value = 0
            self._health = value

        if value > 100:
            value = 100
            self._health = value
        
        if 0 <= value <= 100:
            self._health = value
    
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self,value):
        if value < 0:
            self._mana = 0
        
        if value > 50:
            self._mana = 50
        
        if 0 <= value <= 50:
            self._mana = value
    
    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self._level}!")
    
    def __str__(self):
        return(f"Name: {self.name}\nLevel: {self._level}\nHealth: {self.health}\nMana: {self.mana}\n")


hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up
