from dataclasses import dataclass, asdict
import random

@dataclass
class Alele_List:
    HEALTH:int=0
    ATTACK:int=0
    DEFENSE:int=0
    INTIMIDATION:int=0
    PEACE:int=0
    WAR:int=0
    RETALIATION:int=0
    FEAR:int=0
    PURSUIT:int=0
    SPEED:int=0
    
    def __int__(self):
        self.HEALTH = 0
        self.ATTACK = 0
        self.DEFENSE = 0
        self.INTIMIDATION = 0
        self.PEACE = 0
        self.WAR = 0
        self.RETALIATION = 0
        self.FEAR = 0
        self.PURSUIT = 0
        self.SPEED = 0

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
    
    def create_custom_alele(values:tuple[int]) -> 'Alele_List':
        a = Alele_List()

def distribute_integer(total, n) -> list:
    cuts = sorted(random.sample(range(total + 1), n - 1))
    cuts = [0] + cuts + [total]
    
    return [cuts[i+1] - cuts[i] for i in range(n)]


def generate_random_alele(number_of_aleles:int, baseline_val:int) -> Alele_List:
    alele = Alele_List()

    number_of_attr = alele.get_number_of_aleles()
    distribution = distribute_integer(number_of_aleles, number_of_attr)
    
    alele.increment_aleles(distribution, baseline_val)
    return alele
