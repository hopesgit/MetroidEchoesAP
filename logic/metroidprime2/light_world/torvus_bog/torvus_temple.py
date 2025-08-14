from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal, \
    can_lay_bomb_or_pb, can_use_screw_attack, can_use_boost_ball
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class _TorvusTemple(MetroidPrime2Region):
    name="Torvus Temple"


class TorvusTemple_Arena(_TorvusTemple):
    desc="Arena"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bug - Plaza Access (Upper)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            door=DoorCover.EmeraldTranslator,
            rule=lambda state, player: state.has("Torvus Bog - Torvus Temple | Item Collected")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Upper)",
            rule=lambda state, player: state.has("Torvus Bog - Torvus Temple | Pirates Dead")
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pirates Dead",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Torvus Temple | Pirates Dead",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
            MetroidPrime2Location(
                name="Item Collected",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Torvus Temple | Item Collected",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
            MetroidPrime2Location(
                name="Pickup (Super Missile)",
                can_access=lambda state, player: True,
                parent=self
            )
        ]


class TorvusTemple_Underground(_TorvusTemple):
    desc="Underground"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Access (Lower Torvus Temple Entrance)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transport to Agon Wastes",
            door=DoorCover.Seeker,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Tunnel (Tunnel)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground Transport Entrance)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]


class TorvusTemple_UndergroundTransportEntrance(_TorvusTemple):
    desc="Underground Transport Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Upper)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True
        )
    ]


class TorvusTemple_Upper(_TorvusTemple):
    desc="Upper"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Arena)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Controller Access",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True
        )
    ]
