from dataclasses import dataclass, asdict
from tree import *
import random
import math
from alele_list import *

class Creature:
    baseline_number_of_aleles:int = 50
    baseline_alele_val:int = 5
    max_random_aleles:int = 10

    max_alele_loss = 4
    max_alele_gain = 4
    max_alele_change = 2
    number_of_aleles:int
    alele:Alele_List

    def __init__(self):
        self.number_of_aleles = self.baseline_number_of_aleles
        self.alele = Alele_List()

    def generate_random_creature() -> 'Creature':
        new_creature = Creature()
        new_creature.number_of_aleles = Creature.baseline_number_of_aleles + random.randint(0, new_creature.max_random_aleles)
        new_creature.alele = generate_random_alele(new_creature.number_of_aleles, new_creature.baseline_alele_val)
        return new_creature
    
    def create_imperfect_copy(self) -> 'Creature':
        attributes = list(vars(self.alele).items())
        number_of_attr = len(attributes)
        new_creature = Creature()

        # Copy aleles
        for ind in range(new_creature.alele.get_number_of_aleles()):
            new_creature.alele.set_alele_by_index(ind, self.alele.get_alele_by_index(ind), False)

        # Gain or lose aleles
        alele_gain = random.randint(-self.max_alele_loss, self.max_alele_gain)
        if self.number_of_aleles + alele_gain < new_creature.baseline_number_of_aleles:
            alele_gain = new_creature.baseline_number_of_aleles - self.number_of_aleles

        new_creature.number_of_aleles = self.number_of_aleles + alele_gain
        for i in range(abs(alele_gain)):
            attr_changed = random.randint(0, number_of_attr-1)
            new_creature.alele.set_alele_by_index(attr_changed, 1 if alele_gain > 0 else -1, True)

        # Change aleles
        alele_change = random.randint(0, self.max_alele_change)
        for i in range(alele_change):
            swap = [random.randint(0, number_of_attr-1) for j in range(2)]

            new_creature.alele.set_alele_by_index(swap[0], 1, True)
            new_creature.alele.set_alele_by_index(swap[1], -1, True)

        return new_creature

    def __str__(self):
        creature_print = ''
        
        attributes = self.alele.get_list_of_aleles() 
        attr_size = 0
        value_size = 0

        for attr in attributes:
            if len(attr) > attr_size:
                attr_size = len(attr)

            value = getattr(self.alele, attr)
            if len(str(value)) > value_size:
                value_size = len(str(value))

        for attr in attributes:
            value = getattr(self.alele, attr)
            creature_print += f'{attr+" "*(attr_size-len(attr))} - {str(value)+" "*(value_size-len(str(value)))}\n'

        return creature_print


if __name__ == '__main__':
    sample_creature:Creature = Creature.generate_random_creature()
    print(sample_creature)
    for attr, val in vars(sample_creature.alele).items():
        print(f'{attr} -> {val}')

    print('\n--------\n')
    new_creature:Creature = sample_creature.create_imperfect_copy()
    for attr, val in vars(new_creature.alele).items():
        print(f'{attr} \t -> {getattr(sample_creature.alele, attr)} \t{val}')
