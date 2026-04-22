from aleles import *

class Gene:
    def __init__(self, aleles:Alele_List):
        if not aleles:
            self.aleles = Alele_List()
        else:
            self.aleles = aleles

    def get_weighted_calc(self, weight_to_calc:Alele_List):
        total = 0
        
        for attr, val in vars(self.aleles).items():
            total += val * getattr(weight_to_calc, attr)

        return total

if __name__ == '__main__':
    pass
