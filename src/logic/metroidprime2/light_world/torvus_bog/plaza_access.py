from BaseClasses import MultiWorld, ItemClassification
from ... import has_trick_enabled, can_lay_bomb, can_use_screw_attack, can_use_boost_ball
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and


class _PlazaAccess(MetroidPrime2Region):
    name = "Plaza Access"


class PlazaAccess_ForgottenBridgeEntrance(MetroidPrime2Region):
    name = "Plaza Access"
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


class PlazaAccess_HalfPipe(MetroidPrime2Region):
    name = "Plaza Access"
    desc="Half-Pipe"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Maze)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: can_use_boost_ball(state, player)
        )


class PlazaAccess_Maze(MetroidPrime2Region):
    name = "Plaza Access"
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


class PlazaAccess_MorphBallTunnelForgottenBridgeSide(MetroidPrime2Region):
    name = "Plaza Access"
    desc="Morph Ball Tunnel Forgotten Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel Forgotten Bridge Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Maze)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination= "Torvus Bog - Plaza Access (Half-Pipe)",
            rule=lambda state, player: condition_and([
                can_lay_bomb(state, player),
                can_use_screw_attack(state, player),
                has_trick_enabled(state, player, "Torvus Bog - Plaza Access | Out of Bounds")
            ])
        )
    ]

class PlazaAccess_MorphBallTunnelTorvusPlazaSide(MetroidPrime2Region):
    name = "Plaza Access"
    desc="Morph Ball Tunnel Torvus Plaza Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel Torvus Plaza Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Maze)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
    ]


class PlazaAccess_TorvusPlazaEntrance(MetroidPrime2Region):
    name = "Plaza Access"
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
