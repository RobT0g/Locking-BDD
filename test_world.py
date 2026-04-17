import pytest
from creature import Creature
from world import *

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
sample_creatures = [ Creature() for i in range(len(sample_aleles))]

for ind, alele_set in enumerate(sample_aleles):
    c = sample_creatures[ind]

    for alele_ind, a in enumerate(alele_set):
        sample_creatures[ind].alele.set_alele_by_index(alele_ind, a, False)

sample_world = World()

sample_world.iterations = 20
sample_world.number_of_creatures = 20
sample_world.creatures = sample_creatures.copy()
sample_world.list_of_creatures = sample_creatures.copy()
sample_world.lineage = []
sample_world.action_manager = Actions()
sample_world.world_report = ''

sample_world.lineage.set_root('BASE')

for c in sample_world.creatures:
    sample_world.lineage.add_new_item(c, 'BASE')


@pytest.mark.parametrize('sample_world', sample_world)
def test_fighters(sample_world):
    assert sample_world

