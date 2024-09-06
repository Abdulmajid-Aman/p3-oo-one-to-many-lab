class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = list()

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self._pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
        

    @pet_type.setter
    def pet_type(self, value):
        if value not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self._pet_type = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise Exception('Not a valid Instance')
        self._owner = value

class Owner:
    def __init__(self, name):
        self.name = name


    def pets(self):
        return [pet for pet in Pet.all if pet._owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception('Not a valid instance')
        pet._owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

# Create an Owner instance
owner = Owner("John")

# Create Pet instances with the owner
pet1 = Pet("Whiskers", "cat", owner)
pet2 = Pet("Jerry", "reptile", owner)

print(Pet.all)  # Output: [pet1, pet2]
print(owner.pets())  # Output: [pet1, pet2]