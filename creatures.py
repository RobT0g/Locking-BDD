from dataclasses import dataclass, asdict
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
    
    def get_number_of_attributes(self) -> int:
        return len(vars(self).items())

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

        # Gain or lose aleles
        alele_gain = random.randint(-self.max_alele_loss, self.max_alele_gain)
        if self.number_of_aleles + alele_gain < new_creature.baseline_number_of_aleles:
            alele_gain = new_creature.baseline_number_of_aleles - self.number_of_aleles

        new_creature.number_of_aleles = self.number_of_aleles + alele_gain
        for i in range(abs(alele_gain)):
            attr_changed = random.randint(0, number_of_attr-1)
            setattr(new_creature.alele, attributes[attr_changed][0], getattr(new_creature.alele, attributes[attr_changed][0]) + (-1 if alele_gain< 0 else 1))

        # Change aleles
        alele_change = random.randint(0, self.max_alele_change)
        for i in range(alele_change):
            swap = [random.randint(0, number_of_attr-1) for j in range(2)]

            setattr(new_creature.alele, attributes[swap[0]][0], getattr(new_creature.alele, attributes[swap[0]][0])+1)
            setattr(new_creature.alele, attributes[swap[1]][0], getattr(new_creature.alele, attributes[swap[1]][0])-1)

        return new_creature

    
if __name__ == '__main__':
    sample_creature:Creature = Creature.generate_random_creature()
    for attr, val in vars(sample_creature.alele).items():
        print(f'{attr} -> {val}')

    print('\n--------\n')
    new_creature:Creature = sample_creature.create_imperfect_copy()
    for attr, val in vars(new_creature.alele).items():
        print(f'{attr} -> {val}')


