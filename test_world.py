import pytest
from creature import Creature
from world import *
from tree import *

list_of_aleles = [
    'HEALTH',
    'ATTACK',
    'DEFENSE',
    'INTIMIDATION',
    'PEACE',
    'WAR',
    'RETALIATION',
    'FEAR',
    'PURSUIT',
    'SPEED'
]
sample_aleles = [
    (5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
    (6, 1, 8, 5, 4, 1, 7, 8, 5, 5),
    (5, 9, 7, 2, 1, 5, 3, 3, 3, 6),
    (2, 7, 1, 3, 4, 1, 3, 4, 1, 8),
    (5, 6, 3, 5, 5, 8, 9, 1, 3, 8),
    (8, 5, 3, 6, 1, 5, 5, 6, 8, 4),
    (4, 5, 5, 3, 4, 3, 4, 2, 7, 6),
    (1, 1, 6, 9, 1, 7, 1, 3, 6, 9),
    (6, 5, 6, 4, 8, 2, 1, 9, 1, 5),
    (9, 5, 8, 8, 7, 4, 4, 4, 8, 5)
]
a = Alele_List()
sample_creatures = [ Creature() for i in range(len(sample_aleles))]
for ind, alele_set in enumerate(sample_aleles):
    for alele_ind, a in enumerate(alele_set):
        #print(f'Setting {ind} {list_of_aleles[alele_ind]} to {a}')
        sample_creatures[ind].alele.set_alele_by_index(alele_ind, a, False)
    
    #print(sample_creatures[ind].alele)
    
sample_world = Old_World()

sample_world.iterations = 20
sample_world.number_of_creatures = len(sample_aleles)
sample_world.creatures = sample_creatures.copy()
sample_world.list_of_creatures = sample_creatures.copy()
sample_world.lineage = ItemTree()
sample_world.action_manager = Actions()
sample_world.world_report = ''

sample_world.lineage.set_root('BASE')


for c in sample_world.creatures:
    sample_world.lineage.add_new_item(c, 'BASE')
    print(c.alele)


@pytest.mark.parametrize('sample_world', [sample_world])
def test_fighters(sample_world):
    assert sample_world
    results = [[0, 0], 
               [0, 1],
[0, 2],
[3, 0],
[4, 0],
[5, 0],
[6, 0],
[7, 0],
[0, 8],
[0, 9],
[0, 1],
[1, 1],
[2, 1],
[3, 1],
[4, 1],
[1, 5],
[6, 1],
[7, 1],
[1, 8],
[1, 9],
[0, 2],
[2, 1],
[2, 2],
[3, 2],
[4, 2],
[5, 2],
[6, 2],
[7, 2],
[8, 2],
[2, 9],
[3, 0],
[3, 1],
[3, 2],
[3, 3],
[3, 4],
[3, 5],
[3, 6],
[7, 3],
[3, 8],
[3, 9],
[4, 0],
[4, 1],
[4, 2],
[3, 4],
[4, 4],
[4, 5],
[4, 6],
[7, 4],
[4, 8],
[4, 9],
[5, 0],
[1, 5],
[5, 2],
[3, 5],
[5, 4],
[5, 5],
[5, 6],
[7, 5],
[5, 8],
[5, 9],
[6, 0],
[6, 1],
[6, 2],
[3, 6],
[4, 6],
[6, 5],
[6, 6],
[7, 6],
[6, 8],
[6, 9],
[7, 0],
[7, 1],
[7, 2],
[7, 3],
[7, 4],
[7, 5],
[7, 6],
[7, 7],
[7, 8],
[7, 9],
[0, 8],
[8, 1],
[8, 2],
[3, 8],
[4, 8],
[5, 8],
[6, 8],
[7, 8],
[8, 8],
[8, 9],
[0, 9],
[1, 9],
[2, 9],
[3, 9],
[4, 9],
[5, 9],
[6, 9],
[7, 9],
[8, 9],
[9, 9],]

    for i in range(len(sample_world.creatures)):
        for j in range(len(sample_world.creatures)):
            r = results[i*10+j]
            w = sample_world.fight([i, j])
            assert w == (True, r[0], r[1]), f'Tested {i} vs {j}; Actual result: {w}. Expected: {r}'
            
