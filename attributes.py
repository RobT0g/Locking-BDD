from dataclasses import dataclass, asdict
from aleles import *

@dataclass
class AttributeList:
    speed:Alele_List = Alele_List(
        WING    = 3,
        LEG     = 2,
        DRAG    = 1
    )



