from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal, \
    can_lay_bomb_or_pb, can_use_screw_attack, can_use_boost_ball, can_use_darkburst, can_use_sonic_boom
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class UndergroundTunnel_Tunnel(MetroidPrime2Region):
    name="Underground Tunnel"
    desc="Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Tunnel (After Falls)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: state.has("Morph Ball", player),
                parent=self
            )
        ]


class UndergroundTunnel_AfterFalls(MetroidPrime2Region):
    name="Underground Tunnel"
    desc="Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Tunnel (Tunnel)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Underground Tunnel | Instant Morph to enter Tunnel"),
                    state.has("Morph Ball", player)
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Underground Tunnel | Wall Boost to enter Tunnel"),
                    can_use_boost_ball(state, player)
                ]),
                # I have a suspicion that Screw Attack (probably NSJ) would also work here, but haven't seen evidence yet
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Center)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        )
    ]
