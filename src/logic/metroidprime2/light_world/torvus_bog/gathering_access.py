from BaseClasses import MultiWorld, ItemClassification
from Utils import condition_or, condition_and
from logic.metroidprime2 import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_boost_ball, has_missile_count, \
    can_activate_dark_portal, can_use_screw_attack, can_use_charged_power_beam, can_use_spider_ball

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class GatheringAccess(MetroidPrime2Region):
    name="Gathering Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Upper Door Ledge)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (West Door Ledge)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        )
    ]
