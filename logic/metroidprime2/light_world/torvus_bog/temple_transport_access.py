from BaseClasses import MultiWorld, ItemClassification
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class TorvusBog_TempleTransportAccess(MetroidPrime2Region):
    name = "Temple Transport Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transport to Temple Grounds",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Beach)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
