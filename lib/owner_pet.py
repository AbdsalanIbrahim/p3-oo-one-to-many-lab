class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Stores all instances of the Pet class

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type})"


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns all pets owned by this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Adds a pet to the owner if it's a valid Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception("Only pets of type Pet can be added")
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a list of the owner's pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)
