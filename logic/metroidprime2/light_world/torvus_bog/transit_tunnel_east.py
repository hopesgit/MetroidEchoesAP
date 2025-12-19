from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb, can_lay_pb, can_use_screw_attack, can_use_darkburst, can_use_sonic_boom
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class _TransitTunnelEast(MetroidPrime2Region):
    """Morph Ball puzzle room connecting Training Chamber and Catacombs.
    Air jets in this room can lift the Morph Ball if the player doesn't have Bombs."""
    name="Transit Tunnel East"


class TransitTunnelEast_CatacombsSide(_TransitTunnelEast):
    desc="Catacombs Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel East Entrance)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel East (Training Chamber Side)",
            rule=lambda state, player: True
        )
    ]

class TransitTunnelEast_TrainingChamberSide(_TransitTunnelEast):
    """Has the Bomb Slot as well as the pickup."""
    desc="Training Chamber Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (East Caged Area)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel East (Catacombs Side)",
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Energy Tank)",
                can_access=lambda state, player: condition_and([
                    can_lay_bomb(state, player),
                    state.has('Gravity Boost', player)
                ]),
                parent=self
            ),
        ]
