from dataclasses import dataclass, asdict
from tree import *
import random
import math
from alele_list import *
from creature import *
from actions import *
from tabulate import tabulate

class World:
    iterations:int = 20
    number_of_creatures = 20
    creatures:list[Creature] = [Creature.generate_random_creature() for i in range(number_of_creatures)]
    list_of_creatures:list[Creature] = creatures.copy()
    lineage:ItemTree = []
    action_manager:Actions = Actions()

    def __init__(self):
        self.lineage = ItemTree()
        self.lineage.set_root('BASE')

        for c in self.creatures:
            self.lineage.add_new_item(c, 'BASE')

    def calculate(self, creatures:list[Creature], attribute:str) -> list[int]:
        return self.action_manager.get_paired_attribute(creatures, attribute)

    def fight(self, creature_ids:list[int]) -> tuple[bool, int]:
        fighters = [self.creatures[i] for i in creature_ids]
        
        # Will they fight?
        engage_status = self.calculate(fighters, 'engage')
        engage_status = [True, True]

        if all(engage_status):
            # Both want to fight
            hits_to_kill = self.action_manager.get_both_hits_to_kill(fighters)

            if hits_to_kill[0] >= hits_to_kill[1]:
                # Fighter 1 won
                return (True, creature_ids[0])

            else:
                # Fighter 2 won
                return (True, creature_ids[1])

        elif any(engage_status):
            # Only one of them want to fight
            pass

        else:
            # Neither wants to fight
            pass


    def iterate(self, iteration_number:int, report:bool=False):
        next_gen = []
        for i in range(0, self.number_of_creatures, 2):
            result = self.fight([i, i+1])

            if report:
                self.report_fight(*self.fight)

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

    def report_fight(self, won:bool, players:list[Creature]):
        headers = ['Attribute', 'Winner', 'Loser']
        data = []
        if not won:
            headers[1] = 'Player'
            headers[2] = 'Player'
        
        for attr in players[0].alele.get_list_of_aleles():
            data.append((attr, getattr(players[0].alele, attr), getattr(players[1].alele, attr)))
        
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def execute(self):
        for i in range(self.iterations):
            random.shuffle(self.creatures)
            self.iterate(i, i == 0 or i == self.iterations-1)


if __name__ == '__main__':
    w = World()
    w.execute()
    