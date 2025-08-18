from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_boost_ball, has_missile_count, \
    can_activate_dark_portal, can_use_screw_attack, can_use_charged_power_beam, can_use_spider_ball
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class TrainingAccess(MetroidPrime2Region):
    name="Training Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (South Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
