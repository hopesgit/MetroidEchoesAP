from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class GroveAccess(MetroidPrime2Region):
    name="Grove Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Upper Door Ledge)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        )
    ]
