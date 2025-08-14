from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal, \
    can_lay_bomb_or_pb, can_use_screw_attack, can_use_boost_ball
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class _TempleAccess(MetroidPrime2Region):
    name="Temple Access"


class TempleAccess_Upper(_TempleAccess):
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


class TempleAccess_PickupTube(_TempleAccess):
    desc="Pickup Tube"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel)",
            rule= lambda state, player: True
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


class TempleAccess_LowerGreatBridgeEntrance(_TempleAccess):
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


class TempleAccess_LowerTorvusTempleEntrance(_TempleAccess):
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


class TempleAccess_MorphBallTunnel(_TempleAccess):
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
