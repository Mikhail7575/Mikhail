# 1. Создать класс Animal: name, species
# 2. Создать подкласс Mammal: warm_blood = True; display_info и Bird: can_fly = True; display_info
# 3. Создать класс Zoo: animals = []; add_animal, show_all_animals

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info_(self):
        print(f"{self.name} - {self.species}")


class Mammal(Animal):
    def __init__(self, name, species):
	    super().__init__(name, species)
        self.warm_blood = warm_blood    
    
	def display_info_(self):
        print(f"{self.name} - {self.species} warm_blood = True")
         
class Zoo(animal):
     def __init__(self, name, species):
		super().__init__(name, species)		 