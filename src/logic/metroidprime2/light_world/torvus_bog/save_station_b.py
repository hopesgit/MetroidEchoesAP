from BaseClasses import MultiWorld, ItemClassification
from Utils import condition_or, condition_and
from logic.metroidprime2 import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_boost_ball, has_missile_count

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusBog_SaveStationB(MetroidPrime2Region):
    name="Save Station B"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
