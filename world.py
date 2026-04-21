from tabulate import tabulate
import matplotlib.pyplot as plt

import json

from dataclasses import dataclass, asdict
import random
import math

from tree import *
from gene import *
from creature import *
from actions import *

class World:
    def __init__(self, name:str):
        self.name = name
        self.iterations:            int = 400
        self.number_of_creatures:   int = 100

        self.creatures:             list[Creature] = [Creature.generate_random_creature() for i in range(self.number_of_creatures)]
        self.list_of_creatures:     list[Creature] = self.creatures.copy()
        
        self.action_manager:        Actions = Actions()
        self.world_report:          str = ''

        self.lineage:               ItemTree = ItemTree()
        self.lineage.set_root('BASE')

        self.generations = [self.creatures.copy()]
        self.strategies = []

        for c in self.creatures:
            self.lineage.add_new_item(c, 'BASE')

    def calculate(self, creatures:list[Creature], attribute:str) -> list[int]:
        return self.action_manager.get_paired_attribute(creatures, attribute)

    def fight(self, creature_ids:list[int]) -> tuple[bool, int, int]:
        fighters = [self.creatures[i] for i in creature_ids]
        hits_to_kill = self.action_manager.get_both_hits_to_kill(fighters)

        if hits_to_kill[0] <= hits_to_kill[1]:
            # Fighter 1 won
            return (True, creature_ids[0], creature_ids[1])

        else:
            # Fighter 2 won
            return (True, creature_ids[1], creature_ids[0])

    def run_encounter(self, creature_ids:list[int]) -> tuple[bool, int, int]:
        fighters = [self.creatures[i] for i in creature_ids]
        
        # Will they fight?
        engage_status = [i > 0 for i in self.calculate(fighters, 'engage')]
        #engage_status = [True, True]

        if all(engage_status):
            # Both want to fight
            self.strategies[-1]['basic_fight'] += 1
            return self.fight(creature_ids)

        elif any(engage_status):
            # Only one of them want to fight
            if engage_status[1]:
                creature_ids = [creature_ids[1], creature_ids[0]]
                fighters = [fighters[1], fighters[0]]

            will_pursuit = self.calculate(fighters, 'will_pursuit')[0]
            can_escape = self.calculate([fighters[1], fighters[0]], 'can_escape')[0]

            if will_pursuit <= 0 or can_escape > 1:
                # No fight
                self.strategies[-1]['escape'] += 1
                return (False, fighters[0], fighters[1])

            # Attacker catch up
            self.strategies[-1]['no_escape'] += 1
            return self.fight(creature_ids)

        else:
            # Neither wants to fight
            self.strategies[-1]['no_fight'] += 1
            return (False, fighters[0], fighters[1])

    def iterate(self, iteration_number:int, report:bool=False):
        next_gen = []
        self.world_report += f'\n --- Current Iteration is {iteration_number} ---\n'
        self.strategies.append({'basic_fight':0, 'escape':0, 'no_escape':0, 'no_fight':0})

        for i in range(0, self.number_of_creatures, 2):
            result = self.run_encounter([i, i+1])
            current_report = ''#self.report_fight(result[0], [self.creatures[result[1]], self.creatures[result[2]]])
            self.world_report += current_report + '\n'

            if report:
                print(current_report)

            if result[0]:
                winner = self.creatures[result[1]]
                
                for i in range(2):
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

        self.generations.append(next_gen)
        self.creatures = next_gen
        random.shuffle(self.creatures)

    def report_fight(self, won:bool, players:list[Creature]) -> str:
        headers = ['Attribute', 'Winner', 'Loser']
        data = []
        if not won:
            headers[1] = 'Player'
            headers[2] = 'Player'
        
        for attr in gene_fields:
            data.append((attr, players[0].genes[attr], players[1].genes[attr]))
        
        report = tabulate(data, headers=headers, tablefmt="grid")
        return report

    def execute(self):
        for i in range(self.iterations):
            random.shuffle(self.creatures)
            self.iterate(i, False)
        
        with open('report.txt', 'w') as file:
            file.writelines(self.world_report)

    def analyze_trends(self):
        attribute_trends = {}
        for attr in gene_fields:
            attribute_trends[attr] = []

            for ind in range(len(self.generations)):
                if ind%10 != 0:
                    continue

                gen = self.generations[ind]
                avg_field_value = 0

                for c in gen:
                    avg_field_value += c.genes[attr]

                avg_field_value = (avg_field_value/self.number_of_creatures)
                attribute_trends[attr].append(avg_field_value)
        
        with open("trends.json", "w") as final_file:
            json.dump(attribute_trends, final_file, indent=4)
        
        colors = plt.cm.get_cmap('tab10', 10)
        plt.figure(1)
        for attr in attribute_trends:
            plt.plot(attribute_trends[attr], label=attr, color=colors(list(attribute_trends.keys()).index(attr)), linewidth=2)

        plt.xlabel('Index/Time')
        plt.ylabel('Value')
        plt.title('Comparison of Multiple Data Series')

        plt.legend()
        plt.savefig(f'results/{self.name}_multi_line_plot.png')
        
        plt.figure(2)
        analyze_st = {'basic_fight':[], 'escape':[], 'no_escape':[], 'no_fight':[]}
        for attr in analyze_st:
            for gen in self.strategies:
                analyze_st[attr].append(gen[attr])
                
            plt.plot(analyze_st[attr], label=attr, color=colors(list(analyze_st.keys()).index(attr)), linewidth=2)

        plt.xlabel('Index/Time')
        plt.ylabel('Value')
        plt.title('Comparison of Multiple Data Series')

        plt.legend()
        plt.savefig(f'results/{self.name}_strategies.png')


if __name__ == '__main__':
    w = World('test1')
    w.execute()
    w.analyze_trends()
