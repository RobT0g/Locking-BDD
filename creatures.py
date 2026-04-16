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

    def __init__(self, number_of_aleles:int, baseline_val:int):
        number_of_attr = len(vars(self).items())
        print(number_of_attr)
        distribution = self.distribute_integer(number_of_aleles, number_of_attr)
        
        for ind, key in enumerate(vars(self).keys()):
            setattr(self, key, distribution[ind]+baseline_val)


    def distribute_integer(total, n):
        cuts = sorted(random.sample(range(total + 1), n - 1))
        cuts = [0] + cuts + [total]
        
        return [cuts[i+1] - cuts[i] for i in range(n)]

class Creature:
    baseline_number_of_aleles:int = 40
    max_random_aleles:int = 10
    baseline_alele_val:int = 5

    def __init__(self):
        self.number_of_aleles = self.baseline_number_of_aleles + random.randint(0, self.max_random_aleles)
        self.aleles = Alele_List(self.number_of_aleles, self.baseline_alele_val)

    


    
if __name__ == '__main__':
    sample_creature = Creature()
    for attr, val in vars(sample_creature.aleles).items():
        print(f'{attr} -> {val}')
