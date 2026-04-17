from dataclasses import dataclass, asdict
from tree import *
import random

@dataclass
class Alele_List:
    HEALTH:int = 0
    ATTACK:int = 0
    DEFENSE:int = 0
    INTIMIDATION:int = 0
    
    PEACE:int = 0
    WAR:int = 0
    
    RETALIATION:int = 0
    FEAR:int = 0

    PURSUIT:int = 0
    SPEED:int = 0

    def increment_aleles(self, distribution:list[int], baseline_increment:int) -> None:
        for ind, key in enumerate(vars(self).keys()):
            setattr(self, key, distribution[ind]+baseline_increment)
    
    def get_number_of_aleles(self) -> int:
        return len(vars(self).items())
    
    def get_list_of_aleles(self) -> list[str]:
        return list(vars(self).keys())
    
    def get_alele_by_index(self, ind:int) -> int:
        return getattr(self, self.get_list_of_aleles()[ind])

    def set_alele_by_index(self, ind:int, value:int, increment:bool) -> None:
        alele_to_change = self.get_list_of_aleles()[ind]

        if increment:
            value = getattr(self, alele_to_change) + value

        setattr(self, alele_to_change, value)

def distribute_integer(total, n) -> list:
    cuts = sorted(random.sample(range(total + 1), n - 1))
    cuts = [0] + cuts + [total]
    
    return [cuts[i+1] - cuts[i] for i in range(n)]


def generate_random_alele(number_of_aleles:int, baseline_val:int) -> Alele_List:
    alele = Alele_List()

    number_of_attr = len(vars(alele).items())
    distribution = distribute_integer(number_of_aleles, number_of_attr)
    
    alele.increment_aleles(distribution, baseline_val)
    return alele

class Creature:
    baseline_number_of_aleles:int = 50
    baseline_alele_val:int = 5
    max_random_aleles:int = 10

    max_alele_loss = 4
    max_alele_gain = 4
    max_alele_change = 2

    number_of_aleles:int = 0
    alele:Alele_List=Alele_List()

    def __init__(self):
        pass

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

@dataclass
class Actions:
    engage = [(0, 'WAR', 2), (0, 'PEACE', -1), (0, 'INTIMIDATION', -1)]

    def get_attribute_total(self, creatures:list[Creature], attribute:str) -> int:
        result = 0
        try:
            attribute_cal = getattr(self, attribute)
            
            for cel in attribute_cal:
                result += getattr(creatures[cel[0]].alele, cel[1])*cel[2]

        except: print('INCORRECT ATTRIBUTE NAME')
        return result

class World:
    iterations:int = 20
    number_of_creatures = 100
    creatures:list[Creature] = [Creature.generate_random_creature() for i in range(number_of_creatures)]
    list_of_creatures:list[Creature] = creatures.copy()
    lineage:ItemTree = []
    action_manager:Actions = Actions()

    def __init__(self):
        self.lineage = ItemTree()
        self.lineage.set_root('BASE')

        for c in self.creatures:
            self.lineage.add_new_item(c, 'BASE')

    def calculate(self, creatures:list[Creature], attribute:str) -> int:
        return self.action_manager.get_attribute_total(creatures, attribute)

    def fight(self, creature_ids:list[int]) -> tuple[bool, int]:
        creatures = [self.creatures[i] for i in creature_ids]
        
        # Will they fight?
        engage_status = [i > 0 for i in [self.calculate(creatures, 'engage'), self.calculate([creatures[1], creatures[0]], 'engage')]]

        if all(engage_status):
            # Both want to fight
            pass

        elif any(engage_status):
            # Only one of them want to fight
            pass

        else:
            # Neither wants to fight
            pass


    def iterate(self):
        next_gen = []
        for i in range(0, self.number_of_creatures, 2):
            result = self.fight([i, i+1])

            if result[0]:
                winner = self.creatures[result[1]]
                next_gen.append(winner)
                
                new_creature = winner.create_imperfect_copy()
                next_gen.append(new_creature)
                self.list_of_creatures.append(new_creature)
                self.lineage.add_new_item(new_creature, winner)
            
            else:
                new_creatures = [self.creatures[i].create_imperfect_copy(), self.creatures[i+1].create_imperfect_copy()]

                for ind, c in enumerate(new_creatures):
                    next_gen.append(c)
                    self.list_of_creatures.append(c)
                    self.lineage.add_new_item(c, self.creatures[i+ind])

        self.creatures = next_gen

    def report(self, iteration_number:int):
        pass

    def execute(self):
        for i in range(self.iterations):
            random.shuffle(self.creatures)
            self.iterate(i)
            self.report()


if __name__ == '__main__':
    sample_creature:Creature = Creature.generate_random_creature()
    print(sample_creature)
    for attr, val in vars(sample_creature.alele).items():
        print(f'{attr} -> {val}')

    print('\n--------\n')
    new_creature:Creature = sample_creature.create_imperfect_copy()
    for attr, val in vars(new_creature.alele).items():
        print(f'{attr} \t -> {getattr(sample_creature.alele, attr)} \t{val}')


