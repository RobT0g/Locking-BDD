from tabulate import tabulate

from dataclasses import dataclass, asdict
import random
import math

from tree import *
from gene import *
from creature import *
from actions import *

class World:
    def __init__(self):
        self.iterations:            int = 20
        self.number_of_creatures:   int = 20

        self.creatures:             list[Creature] = [Creature.generate_random_creature() for i in range(self.number_of_creatures)]
        self.list_of_creatures:     list[Creature] = self.creatures.copy()
        
        self.action_manager:        Actions = Actions()
        self.world_report:          str = ''
        self.lineage:               ItemTree = ItemTree()
        
        self.lineage.set_root('BASE')

        for c in self.creatures:
            self.lineage.add_new_item(c, 'BASE')

    def calculate(self, creatures:list[Creature], attribute:str) -> list[int]:
        return self.action_manager.get_paired_attribute(creatures, attribute)

    def fight(self, creature_ids:list[int]) -> tuple[bool, int, int]:
        fighters = [self.creatures[i] for i in creature_ids]
        
        # Will they fight?
        engage_status = self.calculate(fighters, 'engage')
        engage_status = [True, True]

        if all(engage_status):
            # Both want to fight
            hits_to_kill = self.action_manager.get_both_hits_to_kill(fighters)
            print(hits_to_kill)

            if hits_to_kill[0] >= hits_to_kill[1]:
                # Fighter 1 won
                return (True, creature_ids[0], creature_ids[1])

            else:
                # Fighter 2 won
                return (True, creature_ids[1], creature_ids[0])

        elif any(engage_status):
            # Only one of them want to fight
            pass

        else:
            # Neither wants to fight
            pass

    def iterate(self, iteration_number:int, report:bool=False):
        next_gen = []
        self.world_report += f'\n --- Current Iteration is {iteration_number} ---\n'

        for i in range(0, self.number_of_creatures, 2):
            result = self.fight([i, i+1])
            current_report = self.report_fight(result[0], [self.creatures[result[1]], self.creatures[result[2]]])
            self.world_report += current_report + '\n'

            if report:
                print(current_report)

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

    def report_fight(self, won:bool, players:list[Creature]) -> str:
        headers = ['Attribute', 'Winner', 'Loser']
        data = []
        if not won:
            headers[1] = 'Player'
            headers[2] = 'Player'
        
        for attr in players[0].genes.get_list_of_aleles():
            data.append((attr, getattr(players[0].genes, attr), getattr(players[1].genes, attr)))
        
        report = tabulate(data, headers=headers, tablefmt="grid")
        return report

    def execute(self):
        for i in range(self.iterations):
            random.shuffle(self.creatures)
            self.iterate(i, i == 0 or i == self.iterations-1)
        
        with open('report.txt', 'w') as file:
            file.writelines(self.world_report)


if __name__ == '__main__':
    w = World()
    w.execute()
