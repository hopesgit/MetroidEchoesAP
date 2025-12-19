from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb, can_lay_pb, can_use_screw_attack, can_use_darkburst, can_use_sonic_boom
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


def can_progress_room(state, player) -> bool:
    return condition_and([
        state.has('Gravity Boost', player),
        can_lay_bomb(state, player)
    ])


class _TransitTunnelSouth(MetroidPrime2Region):
    """Morph Ball puzzle room connecting Gathering Hall and Catacombs."""
    name = "Transit Tunnel South"


class TransitTunnelSouth_CatacombsSide(_TransitTunnelSouth):
    desc="Catacombs Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel South Entrance)",
            rule=lambda state, player: True,
            door=DoorCover.Annihilator
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel South (Morph Ball Puzzle)",
            rule=lambda state, player: can_progress_room(state, player)
        )
    ]


class TransitTunnelSouth_GatheringHallSide(_TransitTunnelSouth):
    desc="Gathering Hall Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (South Door Ledge)",
            rule=lambda state, player: True,
            door=DoorCover.Annihilator
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel South (Morph Ball Puzzle)",
            rule=lambda state, player: can_progress_room(state, player)
        )
    ]


class TransitTunnelSouth_MorphBallPuzzle(_TransitTunnelSouth):
    desc = "Morph Ball Puzzle"
    exits_= [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel South (Catacombs Side)",
            rule=lambda state, player: can_progress_room(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel South (Gathering Hall Side)",
            rule=lambda state, player: can_progress_room(state, player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: condition_and([
                    can_lay_bomb(state, player),
                    state.has('Gravity Boost', player)
                ]),
                parent=self
            ),
        ]
