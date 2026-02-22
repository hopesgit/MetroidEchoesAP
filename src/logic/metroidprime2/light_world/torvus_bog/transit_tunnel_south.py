"""Morph Ball puzzle room connecting Gathering Hall and Catacombs."""

from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_and
from ... import can_lay_bomb
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


def can_progress_room(state, player) -> bool:
    return condition_and([
        state.has('Gravity Boost', player),
        can_lay_bomb(state, player)
    ])


class TransitTunnelSouth_CatacombsSide(MetroidPrime2Region):
    name = "Transit Tunnel South"
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


class TransitTunnelSouth_GatheringHallSide(MetroidPrime2Region):
    name = "Transit Tunnel South"
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


class TransitTunnelSouth_MorphBallPuzzle(MetroidPrime2Region):
    name = "Transit Tunnel South"
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

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_and([
                can_lay_bomb(state, player),
                state.has('Gravity Boost', player)
            ])
        )
