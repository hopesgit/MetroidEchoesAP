from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class TransitTunnelWest_SouthSide(MetroidPrime2Region):
    name="Transit Tunnel West"
    desc="South Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel West (North Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (North Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]


class TransitTunnelWest_NorthSide(MetroidPrime2Region):
    name="Transit Tunnel West"
    desc="North Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel West (South Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (West Gated Area)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        )
    ]
