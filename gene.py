from dataclasses import dataclass, asdict
import random

gene_blueprint = {
    'HEALTH': 0,
    'ATTACK': 0,
    'DEFENSE': 0,
    'INTIMIDATION': 0,
    'PEACE': 0,
    'WAR': 0,
    
    'INITIATIVE': 0,
    
    'PURSUIT': 0,
    'SPEED': 0
}

gene_fields = list(gene_blueprint.keys())

def distribute_integer(total, n) -> list:
    cuts = sorted(random.sample(range(total + 1), n - 1))
    cuts = [0] + cuts + [total]
    
    return [cuts[i+1] - cuts[i] for i in range(n)]


def generate_random_gene(number_of_aleles:int, baseline_val:int) -> dict[str, int]:
    new_gene = gene_blueprint.copy()
    distribution = distribute_integer(number_of_aleles, len(new_gene.keys()))

    for key, val in enumerate(distribution):
        new_gene[gene_fields[key]] = baseline_val + val

    return new_gene
