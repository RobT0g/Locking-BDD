from dataclasses import dataclass, asdict

@dataclass
class Alele_List:
    VISION:int = 0
    SMELL:int = 0
    WING:int = 0
    LEG:int = 0
    DRAG:int = 0
    PEACE:int = 0
    WAR:int = 0
    SIZE:int = 0
    MEAT:int = 0
    PLANT:int = 0


alele_cost = Alele_List(
    VISION  = 20,
    SMELL   = 20,
    WING    = 50,
    LEG     = 30,
    DRAG    = 20,
    PEACE   = 1,
    WAR     = 1,
    SIZE    = 5,
    MEAT    = 5,
    PLANT   = 5
)

if __name__ == '__main__':
    print(getattr(alele_cost, 'VISION'))

    for attr, val in vars(alele_cost).items():
        print(f'{attr} -> {val}')