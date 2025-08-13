from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class _PlazaAccess(MetroidPrime2Region):
    name = "Plaza Access"


class PlazaAccess_ForgottenBridgeEntrance(_PlazaAccess):
    desc = "Forgotten Bridge Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel Forgotten Bridge Side)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]


class PlazaAccess_HalfPipe(_PlazaAccess):
    desc="Half-Pipe"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Maze)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Energy Tank)",
                can_access=lambda state, player: True,
                parent=self
            ),
        ]


class PlazaAccess_Maze(_PlazaAccess):
    desc="Maze"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Half-Pipe)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel Torvus Plaza Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel Forgotten Bridge Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
    ]


class PlazaAccess_MorphBallTunnelForgottenBridgeSide(_PlazaAccess):
    desc="Morph Ball Tunnel Forgotten Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel Forgotten Bridge Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Maze)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
    ]

class PlazaAccess_MorphBallTunnelTorvusPlazaSide(_PlazaAccess):
    desc="Morph Ball Tunnel Torvus Plaza Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel Torvus Plaza Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ), MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Maze)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
    ]


class PlazaAccess_TorvusPlazaEntrance(_PlazaAccess):
    desc="Torvus Plaza Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Entrance)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel Torvus Plaza Side)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]
