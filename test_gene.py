from gene import *
import pytest

fields = [
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
generated_values = [
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
sample_genes = []

for values in generated_values:
    new_gene = gene_blueprint.copy()

    for ind, attr in enumerate(new_gene):
        new_gene[list(new_gene.keys())[ind]] = values[ind]

    sample_genes.append(new_gene) 

@pytest.mark.parametrize('sample_genes', [sample_genes])
def test_has_correct_attr(sample_genes):
    for gene in sample_genes:
        for f in fields:
            assert f in gene, f'Attribute {f} not present in gene {gene}'

@pytest.mark.parametrize('gene, expected_values', [(sample_genes[i], generated_values[i]) for i in range(len(sample_genes))])
def test_has_correct_values(gene, expected_values):
    for attr_id in range(len(expected_values)):
        assert gene[fields[attr_id]] == expected_values[attr_id], f'Value for {fields[attr_id]} ({attr_id}) does not match expected {expected_values}'

@pytest.mark.parametrize('baseline_value', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_can_generate_random_gene(baseline_value):
    new_gene = generate_random_gene(10, baseline_value)
    assert new_gene    

    for key in new_gene:
        assert new_gene[key] >= baseline_value
