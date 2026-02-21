from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_or, condition_and
from ... import has_trick_enabled, can_use_screw_attack, has_oob_kit, can_use_seeker_launcher, has_missile_count
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusTemple_Arena(MetroidPrime2Region):
    name = "Torvus Temple"
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


class TorvusTemple_Underground(MetroidPrime2Region):
    name = "Torvus Temple"
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
            rule=lambda state, player: condition_or([
                can_use_seeker_launcher(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Temple | Open Seeker Door without Seeker Missiles"),
                    has_missile_count(state, player, 2),
                    can_use_screw_attack(state, player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground Transport Entrance)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Out of Bounds)",
            rule=lambda state, player: condition_and([
                has_oob_kit(state, player),
                has_trick_enabled(state, player, "Torvus Bog - Torvus Temple | Out of Bounds")
            ])
        )
    ]


class TorvusTemple_UndergroundTransportEntrance(MetroidPrime2Region):
    name = "Torvus Temple"
    desc="Underground Transport Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Upper)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: state.has("Torvus Bog - Torvus Temple | Pirates Dead")
            # the laser barrier preventing access to the Super Missiles also blocks the lower tunnel
        )
    ]


class TorvusTemple_Upper(MetroidPrime2Region):
    name = "Torvus Temple"
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


# pretty hesitant about including this one
class TorvusTemple_OutOfBounds(MetroidPrime2Region):
    name = "Torvus Temple"
    desc = "Out of Bounds"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Arena)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transport to Agon Wastes",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            rule=lambda state, player: True
        ),
    ]
