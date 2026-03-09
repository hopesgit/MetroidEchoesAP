from BaseClasses import MultiWorld, ItemClassification
from ... import has_trick_enabled, can_lay_bomb, can_lay_bomb_or_pb, can_use_screw_attack, can_use_boost_ball
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or, condition_and


class TempleAccess_Upper(MetroidPrime2Region):
    name = "Temple Access"
    desc="Upper"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Arena)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Access (Pickup Tube)",
            rule=lambda state, player: condition_or([
                can_lay_bomb_or_pb(state, player),
                can_use_screw_attack(state, player)
            ]) # this check can be a point of no return if you're missing bombs...
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Bridge)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
    ]


class TempleAccess_PickupTube(MetroidPrime2Region):
    name = "Temple Access"
    desc="Pickup Tube"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel)",
            rule= lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Energy Tank)",
            can_access=lambda state, player: True
        )


class TempleAccess_LowerGreatBridgeEntrance(MetroidPrime2Region):
    name = "Temple Access"
    desc="Lower Great Bridge Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (North Path)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel)",
            rule=lambda state, player: True
        )
    ]


class TempleAccess_LowerTorvusTempleEntrance(MetroidPrime2Region):
    name = "Temple Access"
    desc="Lower Torvus Temple Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel)",
            rule=lambda state, player: True
        )
    ]


class TempleAccess_MorphBallTunnel(MetroidPrime2Region):
    name = "Temple Access"
    desc="Morph Ball Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Lower Great Bridge Entrance)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Temple Access | Wall Boost"),
                    can_use_boost_ball(state, player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Lower Torvus Temple Entrance)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Temple Access | Wall Boost"),
                    can_use_boost_ball(state, player)
                ])
            ])
        )
    ]