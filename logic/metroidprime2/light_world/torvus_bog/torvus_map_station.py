from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import can_activate_dark_portal, can_lay_bomb, can_use_boost_ball, has_trick_enabled
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusMapStation(MetroidPrime2Region):
    name="Torvus Map Station"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Behind Translator Gate)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
