from dataclasses import dataclass, asdict
import math
from creature import *

@dataclass
class Actions:
    engage = [(0, 'WAR', 2), (0, 'PEACE', -1), (1, 'INTIMIDATION', -1)]
    engage_min = None

    damage = [(0, 'ATTACK', 1), (1, 'DEFENSE', -1)]
    damage_min = 1

    def get_attribute_total(self, creatures:list[Creature], attribute:str) -> int:
        result = 0
        try:
            attribute_cal = getattr(self, attribute)
            
            for cel in attribute_cal:
                result += getattr(creatures[cel[0]].alele, cel[1])*cel[2]

        except: print('INCORRECT ATTRIBUTE NAME')

        if min_val:=getattr(self, attribute + '_min') is not None:
            if min_val > result: result = min_val
        
        return result
    
    def get_paired_attribute(self, creatures:list[Creature], attribute:str) -> list[int]:
        return [self.get_attribute_total(creatures, attribute), self.get_attribute_total([creatures[1], creatures[0]], attribute)]

    def get_number_of_hits_to_kill(self, creatures:list[Creature]) -> int:
        damage = self.get_attribute_total(creatures, 'damage')
        return math.ceil(getattr(creatures[1].alele, 'HEALTH')/damage)
    
    def get_both_hits_to_kill(self, creatures:list[Creature]) -> list[int]:
        return [self.get_number_of_hits_to_kill(creatures), self.get_number_of_hits_to_kill([creatures[1], creatures[0]])]

