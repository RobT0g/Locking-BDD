from dataclasses import dataclass, asdict
from tree import *
import random
import math
from gene import *

class Creature:
    baseline_number_of_aleles:int = 500
    baseline_alele_val:int = 5

    max_random_aleles:int = 100
    max_alele_gain = 40
    max_alele_loss = 40

    def __init__(self):
        self.total_aleles = self.baseline_number_of_aleles
        self.genes = gene_blueprint.copy()

    def generate_random_creature() -> 'Creature':
        new_creature = Creature()
        new_creature.total_aleles = Creature.baseline_number_of_aleles + random.randint(0, new_creature.max_random_aleles)
        new_creature.genes = generate_random_gene(new_creature.total_aleles, new_creature.baseline_alele_val)
        return new_creature
    
    def create_imperfect_copy(self) -> 'Creature':
        new_creature = Creature()
        new_creature.genes = self.genes.copy()

        # Gain and lose aleles
        alele_gain = random.randint(0, self.max_alele_gain)
        alele_loss = random.randint(0, self.max_alele_loss)

        if self.total_aleles < new_creature.baseline_number_of_aleles:
            alele_loss = 0

        new_creature.total_aleles = self.total_aleles + alele_gain - alele_loss
        
        # Increasing Aleles
        for i in range(alele_gain):
            attr_changed = random.randint(0, len(gene_fields)-1)
            new_creature.genes[gene_fields[attr_changed]] += 1 if alele_gain > 0 else -1
        
        # Lowering Aleles
        for i in range(alele_loss):
            attr_changed = random.randint(0, len(gene_fields)-1)

            # Making sure alele can't be lower than 1
            while new_creature.genes[gene_fields[attr_changed]] <= 0:
                attr_changed = random.randint(0, len(gene_fields)-1) 

            new_creature.genes[gene_fields[attr_changed]] += 1 if alele_gain > 0 else -1


        return new_creature

    def __str__(self):
        creature_print = ''
        attr_size = 0
        value_size = 0

        for attr in self.genes:
            if len(attr) > attr_size:
                attr_size = len(attr)

            if len(str(self.genes[attr])) > value_size:
                value_size = len(str(self.genes[attr]))

        for attr in self.genes:
            creature_print += f'{attr+" "*(attr_size-len(attr))} - {str(self.genes[attr])+" "*(value_size-len(str(self.genes[attr])))}\n'

        return creature_print


if __name__ == '__main__':
    sample_creature:Creature = Creature.generate_random_creature()
    print(sample_creature)
    for attr, val in sample_creature.genes.items():
        print(f'{attr} -> {val}')

    print('\n--------\n')
    new_creature:Creature = sample_creature.create_imperfect_copy()
    for attr, val in new_creature.genes.items():
        print(f'{attr} \t -> {val}')

