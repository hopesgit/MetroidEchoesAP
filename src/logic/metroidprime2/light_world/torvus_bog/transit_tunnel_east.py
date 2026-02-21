"""Morph Ball puzzle room connecting Training Chamber and Catacombs.
Air jets in this room can lift the Morph Ball if the player doesn't have Bombs."""

from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_and
from ... import can_lay_bomb
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusBog_TransitTunnelEast_CatacombsSide(MetroidPrime2Region):
    name="Transit Tunnel East"
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

class TorvusBog_TransitTunnelEast_TrainingChamberSide(MetroidPrime2Region):
    """Has the Bomb Slot as well as the pickup."""
    name="Transit Tunnel East"
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
