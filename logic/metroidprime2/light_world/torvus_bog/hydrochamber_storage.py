from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_boost_ball, has_missile_count, \
    can_activate_dark_portal, can_use_screw_attack
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class HydrochamberStorage(MetroidPrime2Region):
    name="Hydrochamber Storage"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Lower Door)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Gravity Boost)",
                can_access=lambda state, player: True,
                parent=self
            ),
            MetroidPrime2Location(
                name="Collected Item",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Hydrochamber Storage | Collected Item",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]
